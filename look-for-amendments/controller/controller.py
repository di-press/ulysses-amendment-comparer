from flask import request,jsonify
from model.bm25L import BM25L
from model.preprocessamento import preprocess
import pandas as pd
from util.util import PATCH_TOPIC,QUANT_TOPIC
from util.routers import SEARCH


class Controller:
    topics = pd.read_csv(PATCH_TOPIC).to_numpy()
    bm25 = BM25L([preprocess(topico) for topico in topics])

    def __init__(self,app):
        self.app = app


        #rotas
        self.app.add_url_rule(rule=SEARCH,view_func=self.search,methods=['POST'])
        self.app.add_url_rule(rule=SEARCH+"/batch", view_func=self.searchs, methods=['POST'])



    def hello(self):
        return "Hello"
    def search(self):
        if request.is_json:
            dados = request.get_json()
            if 'query' in dados:
                query = dados['query']
                preProcessQuery = preprocess(query)
                top_k = QUANT_TOPIC if 'top_k' not in dados else dados['top_k']
                result = Controller.bm25.get_top_n(preProcessQuery,Controller.topics,n=top_k)
                return jsonify({'topics':result})
            else:
                return "Erro, parametro de busca não informado",400

    def searchs(self):
        if request.is_json:
            dados = request.get_json()
            if 'querys' in dados:
                querys = dados['querys']
                top_k = QUANT_TOPIC if 'top_k' not in dados else dados['top_k']
                listResult = []
                for query in querys:
                    preProcessQuery = preprocess(query)
                    result = Controller.bm25.get_top_n(preProcessQuery, Controller.topics, n=top_k)
                    listResult.append({'query': query, 'topics': result})

                return jsonify({'result': listResult, 'top_k': top_k}), 200
            else:
                return "Erro, parametro de busca não informado", 400










