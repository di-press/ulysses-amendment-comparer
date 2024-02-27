from flask_restplus import Resource, fields
from flask import request, jsonify
from server.instance import server

from repository.repositoryFeedbackModel import RepositoryFeedbackModel
from adapter.adapterFeedbackModel import outputJsonFeedbackModel, outputJsonFeedbackModels


class DocFeedbackModel(Resource):
    repository = RepositoryFeedbackModel(server.engine)

    resource_fields = server.api.model('Model', {
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example="PL-100"),
        'amendment': fields.String(example="Emenda-1"),
        'topic': fields.String(example="Pensão"),
        'score_standardized': fields.Float(example=0.90)

    })

    @server.api.doc(responses={200: 'OK', 404: 'Não há registro salvos', 500: 'Erro na API'},
                    description='Essa rota retorna todos registros salvos pela LookForSimilar')
    def get(self):
        data = DocFeedbackModel.repository.getFeedbackModels()
        return outputJsonFeedbackModels(data), 200

    @server.api.doc(responses={201: 'OK', 400: 'Parâmetros inválidos', 500: 'Erro na API'},
                    description='Essa rota salva os registros gerados pela LookForSimilar')
    @server.api.expect(resource_fields)
    @server.api.marshal_list_with(resource_fields)
    def post(self):
        payload = request.json
        amendment = payload['amendment']
        projectLaw = payload['projectLaw']
        topic = payload['topic']
        score_standardized = payload['score_standardized']
        result = DocFeedbackModel.repository.addFeedbackModel(
            score_standardized=score_standardized, amendment=amendment, projectLaw=projectLaw, topic=topic)

        return result, 201

    @server.api.doc(responses={202: 'OK', 400: 'Parâmetros inválidos', 500: 'Erro na API'},
                    description='Essa rota exlui um registro gerado pela LookForSimilar')
    @server.api.expect(server.api.model('DeleteModel', {'id': fields.Integer(example=1)}))
    def delete(self):
        payload = request.json
        id = payload['id']
        result = DocFeedbackModel.repository.deleteFeedbackModel(id)
        if result is not None:
            return outputJsonFeedbackModel(result), 202
        return {"message": "Registro não encontrado"}, 404


class DocFeedbackModelId(Resource):
    resource_fields = server.api.model('Model', {
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example="PL-100"),
        'amendment': fields.String(example="Emenda-1"),
        'topic': fields.String(example="Pensão"),
        'score_standardized': fields.Float(example=0.90)

    })

    @server.api.doc(responses={200: 'OK', 400: 'Parâmetro inválido', 500: 'Erro na API'},
                    description='Essa rota retorna um registro gerado pela LookForSimilar')
    def get(self, id):
        dado = DocFeedbackModel.repository.getFeedbackModel(id)
        if dado is not None:
            return outputJsonFeedbackModel(dado), 200
        else:
            return {"message": "Registro não encontrado"}, 404


class DocFeedbackModelBatch(Resource):
    resource_model = server.api.model("Model", {
        'id': fields.Integer(readonly=True, example=1),
        'projectLaw': fields.String(example="PL-100"),
        'amendment': fields.String(example="Emenda-1"),
        'topic': fields.String(example="Pensão"),
        'score_standardized': fields.Float(example=0.90)})

    resource_fields = server.api.model('ModelBatch', {
        "models": fields.List(fields.Nested(resource_model))
    })

    @server.api.doc(responses={201: 'OK', 400: 'Parâmetros inválidos', 500: 'Erro na API'},
                    description='Essa rota salva uma lista de registros gerados pela LookForSimilar')
    @server.api.expect(resource_fields)
    @server.api.marshal_list_with(resource_fields)
    def post(self):
        payload = request.json
        models = payload['models']
        result = DocFeedbackModel.repository.addFeedbackModelBatch(models)

        return result, 201
