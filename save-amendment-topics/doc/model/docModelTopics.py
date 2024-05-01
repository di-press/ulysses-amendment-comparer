from collections.abc import MutableMapping
from flask_restplus import Resource, fields
from flask import request
from server.instance import server

from repository.repositoryModelTopics import RepositoryModelTopics
from adapter.adapterModelTopics import outputJsonModelTopics, outputJsonAllModelTopics


class DocModelTopics(Resource):
    repository = RepositoryModelTopics(server.engine)
    resource_fields = server.api.model('Model', {
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example="PL-100"),
        'topic_id': fields.String(example="T1"),
        'terms': fields.String(example="Pensão, Militares"),
        'configuration': fields.String(example="PL+Emendas")
    })

    @server.api.doc(responses={200: 'OK', 404: 'Não há nenhum registro salvo.', 500: 'Erro na API.'},
                    description='Essa rota retorna todos registros salvos.')
    def get(self):
        data = DocModelTopics.repository.getAllModelTopics()
        return outputJsonAllModelTopics(data), 200

    @server.api.doc(responses={201: 'OK', 400: 'Parâmetros inválidos.', 500: 'Erro na API.'},
                    description='Essa rota salva um registro.')
    @server.api.expect(resource_fields)
    @server.api.marshal_list_with(resource_fields)
    def post(self):
        payload = request.json
        projectLaw = payload['projectLaw']
        topic_id = payload['topic_id']
        terms = payload['terms']
        configuration = payload['configuration']
        result = DocModelTopics.repository.addModelTopics(
            projectLaw=projectLaw, topic_id=topic_id, terms=terms, configuration=configuration)

        return result, 201

    @server.api.doc(responses={202: 'OK', 400: 'Parâmetros inválidos.', 500: 'Erro na API.'},
                    description='Essa rota exclui um registro.')
    @server.api.expect(server.api.model('DeleteModelTopics', {'id': fields.Integer(example=1)}))
    def delete(self):
        payload = request.json
        id = payload['id']
        result = DocModelTopics.repository.deleteModelTopics(id)

        if result is not None:
            return outputJsonModelTopics(result), 202
        return {"message": "Registro não encontrado."}, 404


class DocModelTopicsId(Resource):
    resource_fields = server.api.model('Model', {
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example="PL-100"),
        'topic_id': fields.String(example="T1"),
        'terms': fields.String(example="Pensão, Militares"),
        'configuration': fields.String(example="PL+Emendas")
    })

    @server.api.doc(responses={200: 'OK', 400: 'Parâmetro inválido.', 500: 'Erro na API.'},
                    description='Essa rota retorna um registro.')
    def get(self, id):
        dado = DocModelTopics.repository.getModelTopics(id)
        if dado is not None:
            return outputJsonModelTopics(dado), 200
        else:
            return {"message": "Registro não encontrado."}, 404
