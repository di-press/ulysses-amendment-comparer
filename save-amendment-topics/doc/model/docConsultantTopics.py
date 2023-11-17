from flask_restplus import Resource,fields
from flask import request
from server.instance import server

from repository.repositoryConsultantTopics import RepositoryConsultantTopics
from adapter.adapterConsultantTopics import outputJsonConsultantTopics, outputJsonAllConsultantTopics

class DocConsultantTopics(Resource):
    repository = RepositoryConsultantTopics(server.engine)
    resource_fields = server.api.model('Consultante',{
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example='PL-100'),
        'topic_id': fields.String(example="T1"),
        'topic': fields.String(example="Pensão"),
        'topic_description': fields.String(example="Tópico relacionado a pensões e afins."),
        'matConsultant': fields.String(example="00001")
    })

    @server.api.doc(responses={200:'OK',404:'Não há nenhum registro salvo.',500:'Erro na API.'},
                    description='Essa rota retorna todos os registros salvos pelo consultor.')
    def get(self):
        data = DocConsultanteTopics.repository.getAllConsultantTopics()
        return outputJsonAllConsultantTopics(data),200
    
    @server.api.doc(responses={201:'OK',400:'Parâmetros inválidos.',500:'Erro na API.'},
                    description='Essa rota salva um registro gerado pelo consultor.')
    @server.api.expect(resource_fields)
    @server.api.marshal_list_with(resource_fields)
    def post(self):
        payload = request.json
        projectLaw = payload['projectLaw']
        topic_id = payload['topic_id']
        topic = payload['topic']
        topic_description = payload['topic_description']
        matConsultant = payload['matConsultant']

        result = DocConsultanteTopics.repository.addConsultantTopics(projectLaw=projectLaw, topic_id=topic_id,topic=topic,
                                                                     topic_description=topic_description,matConsultant=matConsultant)
        
    @server.api.doc(responses={202:'OK',400:'Parâmetros inválidos',500:'Erro na API.'},
                    description='Essa rota exclui um registro gerado pelo consultor.')
    @server.api.expect(server.api.model('DeleteConsultantTopics',{'id': fields.Integer(example=1)}))
    def delete(self):
        payload = request.json
        id = payload['id']
        result = DocConsultanteTopics.repository.deleteConsultantTopics(id)
        
        if result is not None:
            return outputJsonConsultantTopics(result), 202
        else:
            return {"message:" "Registro não encontrado."}, 404
        
class DocConsultantTopicsId(Resource):
    resource_fields = server.api.model('Consultant',{
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example='PL-100'),
        'topic_id': fields.String(example="T1"),
        'topic': fields.String(example="Pensão"),
        'topic_description': fields.String(example="Tópico relacionado a pensões e afins."),
        'matConsultant': fields.String(example="00001")
    })

    @server.api.doc(responses={200: 'OK', 400: 'Parâmetro inválido.', 500: 'Erro na API.'},
                    description='Essa rota retorna um registro salvo pelo Consultor.')
    def get(self, id):
        dado = DocConsultanteTopics.repository.getConsultantTopics(id)
        if dado is not None:
            return outputJsonConsultantTopics(dado), 200
        else:
            return {"message": "Registro não encontrado."}, 404
