from repository.repositoryModelTopics import RepositoryModelTopics
from flask import request, jsonify

from adapter.adapterModelTopics import outputJsonAllModelTopics, outputJsonModelTopics
from utils.routers import MODEL

class ControllerModelTopics:

    def __init__(self,app,engine):
        self.engine = engine
        self.repositoryModelTopics = RepositoryModelTopics(self.engine)

        self.app = app

        self.app.add_url_rule(rule=MODEL, view_func=self.addModelTopics, methods=['POST'])
        self.app.add_url_rule(rule=MODEL, view_func=self.getAllModelTopics, methods=['GET'])
        self.app.add_url_rule(rule=MODEL+"/<int:id>", view_func=self.getModelTopics, methods=['GET'])
        self.app.add_url_rule(rule=MODEL, view_func=self.deleteModelTopics, methods=['DELETE'])

    def addModelTopics(self):
        if request.is_json:
            dados = request.get_json()
            if 'projectLaw' in dados and 'topic_id' in dados and 'terms' in dados and 'configuration' in dados:
                projectLaw = dados['projectLaw']
                topic_id = dados['topic_id']
                terms = dados['terms']
                configuration = dados['configuration']
                result = self.repositoryModelTopics.addModelTopics(
                    projectLaw= projectLaw,
                    topic_id= topic_id,
                    terms= terms,
                    configuration= configuration
                    )

                if result is not None:
                    return jsonify(result),201
        return 500
    
    def addModelTopicsBatch(self):
        if request.is_json:
            dados = request.get_json()
            if "models" in dados:
                models = dados['models']
                result = self.repositoryModelTopics.addModelTopicsBatch(models)

                if result is not None:
                    return jsonify(result), 201
        return 500
    
    def getAllModelTopics(self):
        result = self.repositoryModelTopics.getAllModelTopics()
        if result is not None:
            return jsonify(outputJsonAllModelTopics(result)), 200
        return jsonify({"message":"Registro não encontrado"}),404

    def getModelTopics(self,id):
        result = self.repositoryModelTopics.getModelTopics(id)
        if result is not None:
            return jsonify(outputJsonModelTopics(result)), 200
        return jsonify({"message":"Registro não encontrado"}),404

    def deleteModelTopics(self):
        if request.is_json:
            dados = request.get_json()
            if "id" in dados:
                result = self.repositoryModelTopics.deleteModelTopics(dados['id'])
                if result is not None:
                    return jsonify(outputJsonModelTopics(result)), 202
                return jsonify({"message":"Registro não encontrado"}),404