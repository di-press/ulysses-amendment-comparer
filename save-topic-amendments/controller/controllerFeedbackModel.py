from repository.repositoryFeedbackModel import RepositoryFeedbackModel
from flask import request, jsonify

from adapter.adapterFeedbackModel import outputJsonFeedbackModels, outputJsonFeedbackModel
from utils.routers import MODEL

class ControllerFeedbackModel:

    def __init__(self,app,engine):
        self.engine = engine
        self.repositoryFeedbackModel = RepositoryFeedbackModel(self.engine)

        self.app = app

        self.app.add_url_rule(rule=MODEL, view_func=self.addFeedbackModel, methods=['POST'])
        self.app.add_url_rule(rule=MODEL+"/batch", view_func=self.addFeedbackModelBatch, methods=['POST'])
        self.app.add_url_rule(rule=MODEL, view_func=self.getFeedbackModels, methods=['GET'])
        self.app.add_url_rule(rule=MODEL+"/<int:id>", view_func=self.getFeedbackModel, methods=['GET'])
        self.app.add_url_rule(rule=MODEL, view_func=self.deleteFeedbackModel, methods=['DELETE'])



    def addFeedbackModel(self):
        if request.is_json:
            dados = request.get_json()
            if 'projectLaw' in dados and 'amendment' in dados and 'topic' in dados and 'score_standardized' in dados:
                projectLaw = dados['projectLaw']
                topic = dados['topic']
                amendment = dados['amendment']
                score_standardized = dados['score_standardized']
                result = self.repositoryFeedbackModel.addFeedbackModel(
                    projectLaw= projectLaw,
                    topic= topic,
                    amendment= amendment,
                    score_standardized=score_standardized
                    )

                if result is not None:
                    return jsonify(result),201
        return 500

    def addFeedbackModelBatch(self):
        if request.is_json:
            dados = request.get_json()
            if "models" in dados:
                models = dados['models']
                result = self.repositoryFeedbackModel.addFeedbackModelBatch(models)

                if result is not None:
                    return jsonify(result),201
        return 500

    def getFeedbackModels(self):
        result = self.repositoryFeedbackModel.getFeedbackModels()
        if result is not None:
            return jsonify(outputJsonFeedbackModels(result)), 200
        return jsonify({"message":"Registro não encontrado"}),404

    def getFeedbackModel(self,id):
        result = self.repositoryFeedbackModel.getFeedbackModel(id)
        if result is not None:
            return jsonify(outputJsonFeedbackModel(result)), 200
        return jsonify({"message":"Registro não encontrado"}),404

    def deleteFeedbackModel(self):
        if request.is_json:
            dados = request.get_json()
            if "id" in dados:
                result = self.repositoryFeedbackModel.deleteFeedbackModel(dados['id'])
                if result is not None:
                    return jsonify(outputJsonFeedbackModel(result)), 202
                return jsonify({"message":"Registro não encontrado"}),404