from flask_restplus import Resource,fields
from flask import request

from controller.controller import Controller
from model.preprocessamento import preprocess
from server.instance import server
from util.util import QUANT_TOPIC


class DocApi(Resource):
    resource_fields = server.api.model('Search', {
        'query': fields.String(required=True,example="Solicito algo relacionado a pensão"),
        'top_k': fields.Integer(example=2)

    })

    @server.api.doc(responses={201: 'OK', 400: 'Parâmetros inválidos', 500: 'Erro na API'},
                    description='Essa rota retorna uma lista de tópicos relacionados a uma consulta')
    @server.api.expect(resource_fields)
    def post(self):
        payload = request.json
        query = payload['query']
        preProcessQuery = preprocess(query)
        top_k = QUANT_TOPIC if 'top_k' not in payload else payload['top_k']
        result = Controller.bm25.get_top_n(preProcessQuery, Controller.topics, n=top_k)

        return {'topics': result},200


class DocApiBatch(Resource):
    resource_query = server.api.model('SearchDTO', {
        'query': fields.String(required=True, example="Solicito algo relacionado a pensão"),


    })
    resource_querys = server.api.model('SearchBatch', {
        'querys':fields.List(fields.Nested(resource_query)),
        'top_k': fields.Integer(example=2)
    })

    @server.api.doc(responses={201: 'OK', 400: 'Parâmetros inválidos', 500: 'Erro na API'},
                    description='Essa rota retorna uma lista de tópicos relacionados a cada consulta solicitada')
    @server.api.expect(resource_querys)
    def post(self):
        payload = request.json
        querys = payload['querys']
        top_k = QUANT_TOPIC if 'top_k' not in payload else payload['top_k']
        listResult = []
        for query in querys:
            preProcessQuery = preprocess(query)
            result = Controller.bm25.get_top_n(preProcessQuery, Controller.topics, n=top_k)
            listResult.append({'query':query,'topics':result})

        return {'result': listResult,'top_k':top_k}, 200


