from repository.repositoryFeedbackConsultant import RepositoryFeedbackConsultant
from flask import request, jsonify

from adapter.adapterFeedbackConsultant import outputJsonFeedbackConsultant,outputJsonFeedbackConsultants
from utils.routers import CONSULTANT

class ControllerFeedbackConsultant:

    def __init__(self,app,engine):
        self.engine = engine
        self.repositoryFeedbackConsultant = RepositoryFeedbackConsultant(self.engine)

        self.app = app

        self.app.add_url_rule(rule=CONSULTANT, view_func=self.addFeedbackConsultant, methods=['POST'])
        self.app.add_url_rule(rule=CONSULTANT+"/batch", view_func=self.addFeedbackConsultantBatch, methods=['POST'])
        self.app.add_url_rule(rule=CONSULTANT, view_func=self.getFeedbackConsultants, methods=['GET'])
        self.app.add_url_rule(rule=CONSULTANT+"/<int:id>", view_func=self.getFeedbackConsultant, methods=['GET'])
        self.app.add_url_rule(rule=CONSULTANT, view_func=self.deleteFeedbackConsultant, methods=['DELETE'])



    def addFeedbackConsultant(self):
        if request.is_json:
            dados = request.get_json()
            if 'projectLaw' in dados and 'amendment' in dados and 'topic' in dados and 'matConsultant' in dados:
                projectLaw = dados['projectLaw']
                topic = dados['topic']
                amendment = dados['amendment']
                matConsultant = dados['matConsultant']
                result = self.repositoryFeedbackConsultant.addFeedbackConsultant(
                    projectLaw= projectLaw,
                    topic= topic,
                    amendment= amendment,
                    matConsultant=matConsultant
                    )

                if result is not None:
                    return jsonify(result),201
            else:
                jsonify({"message":"parametros incorretos"}), 500
        return 500

    def addFeedbackConsultantBatch(self):
        if request.is_json:
            dados = request.get_json()
            if "feedbacks" in dados:
                models = dados['feedbacks']
                result = self.repositoryFeedbackConsultant.addFeedbackConsultantBatch(models)

                if result is not None:
                    return jsonify(result),201
        return 500

    def getFeedbackConsultants(self):
        result = self.repositoryFeedbackConsultant.getFeedbackConsultants()
        if result is not None:
            return jsonify(outputJsonFeedbackConsultants(result)), 200
        return jsonify({"message":"Registro não encontrado"}),404

    def getFeedbackConsultant(self,id):
        result = self.repositoryFeedbackConsultant.getFeedbackConsultant(id)
        if result is not None:
            return jsonify(outputJsonFeedbackConsultant(result)), 200
        return jsonify({"message":"Registro não encontrado"}),404

    def deleteFeedbackConsultant(self):
        if request.is_json:
            dados = request.get_json()
            if "id" in dados:
                result = self.repositoryFeedbackConsultant.deleteFeedbackConsultant(dados['id'])
                if result is not None:
                    return jsonify(outputJsonFeedbackConsultant(result)), 202
                return jsonify({"message":"Registro não encontrado"}),404