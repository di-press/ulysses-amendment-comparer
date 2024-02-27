from flask_restplus import Resource,fields
from flask import request
from server.instance import server


from repository.repositoryFeedbackConsultant import RepositoryFeedbackConsultant
from adapter.adapterFeedbackConsultant import outputJsonFeedbackConsultants,outputJsonFeedbackConsultant

class DocFeedbackConsultant(Resource):
    repository = RepositoryFeedbackConsultant(server.engine)
    resource_fields = server.api.model('Consultant',{
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw':fields.String(example="PL-100"),
        'amendment':fields.String(example="Emenda-1"),
        'topic':fields.String(example="Pensão"),
        'matConsultant': fields.String(example="123456789")

    })



    @server.api.doc(responses={200:'OK',404:'Não há registro salvos',500:'Erro na API'},
             description='Essa rota retorna todos registros salvos pelo consultor')
    def get(self):
        data = DocFeedbackConsultant.repository.getFeedbackConsultants()
        return outputJsonFeedbackConsultants(data),200

    @server.api.doc(responses={201:'OK',400:'Parâmetros inválidos',500:'Erro na API'},
             description='Essa rota salva os registros gerados pelo consultor')
    @server.api.expect(resource_fields)
    @server.api.marshal_list_with(resource_fields)
    def post(self):
        payload = request.json
        amendment = payload['amendment']
        projectLaw = payload['projectLaw']
        topic = payload['topic']
        matConsultant = payload['matConsultant']
        result = DocFeedbackConsultant.repository.addFeedbackConsultant(projectLaw=projectLaw,amendment=amendment,topic=topic,matConsultant=matConsultant)
        return result,201

    @server.api.doc(responses={202: 'OK', 400: 'Parâmetros inválidos', 500: 'Erro na API'},
             description='Essa rota exlui um registro gerado pelo consultor')
    @server.api.expect(server.api.model('DeleteConsultant',{'id':fields.Integer(example=1)}))
    def delete(self):
        payload = request.json
        id = payload['id']
        result = DocFeedbackConsultant.repository.deleteFeedbackConsultant(id)
        if result is not None:
            return outputJsonFeedbackConsultant(result),202
        else:
            return {"message": "Registro não encontrado"}, 404

class DocFeedbackConsultantId(Resource):
    resource_fields = server.api.model('Consultant', {
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example="PL-100"),
        'amendment': fields.String(example="Emenda-1"),
        'topic': fields.String(example="Pensão"),
        'matConsultant': fields.String(example="123456789")

    })

    @server.api.doc(responses={200: 'OK', 400: 'Parâmetro inválido', 500: 'Erro na API'},
                    description='Essa rota retorna um registro salvo pelo Consultor')
    def get(self,id):
        dado = DocFeedbackConsultant.repository.getFeedbackConsultant(id)
        if dado is not None:
            return outputJsonFeedbackConsultant(dado),200
        else:
            return {"message":"Registro não encontrado"},404

class DocFeedbackConsultantBatch(Resource):
    resource_consultant = server.api.model('Consultant', {
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example="PL-100"),
        'amendment': fields.String(example="Emenda-1"),
        'topic': fields.String(example="Pensão"),
        'matConsultant': fields.String(example="123456789")

    })
    resource_fields = server.api.model('feedbackBatch',{
        "feedbacks":fields.List(fields.Nested(resource_consultant))
    })

    @server.api.doc(responses={201: 'OK', 400: 'Parâmetros inválidos', 500: 'Erro na API'},
                    description='Essa rota salva uma lista de feedbacks gerado pelo Consultor')
    @server.api.expect(resource_fields)
    @server.api.marshal_list_with(resource_fields)
    def post(self):
        payload = request.json
        feedbacks = payload['feedbacks']
        result = DocFeedbackConsultant.repository.addFeedbackConsultantBatch(feedbacks)

        return result, 201









