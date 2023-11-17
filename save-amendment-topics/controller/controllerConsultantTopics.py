from repository.repositoryConsultantTopics import RepositoryConsultantTopics
from flask import request, jsonify

from adapter.adapterConsultantTopics import outputJsonConsultantTopics,outputJsonAllConsultantTopics
from utils.routers import CONSULTANT

class ControllerConsultantTopics:

    def __init__(self,app,engine):
        self.engine = engine
        self.repositoryConsultantTopics = RepositoryConsultantTopics(self.engine)

        self.app = app

        self.app.add_url_rule(rule=CONSULTANT, view_func=self.addConsultantTopics, methods=['POST'])
        self.app.add_url_rule(rule=CONSULTANT+'/batch', view_func=self.addConsultantTopicsBatch, methods=['POST'])
        self.app.add_url_rule(rule=CONSULTANT, view_func=self.getAllConsultantTopics, methods=['GET'])
        self.app.add_url_rule(rule=CONSULTANT+"/<int:id>", view_func=self.getConsultantTopics, methods=['GET'])
        self.app.add_url_rule(rule=CONSULTANT, view_func=self.deleteConsultantTopics, methods=['DELETE'])

    def addConsultantTopics(self):
        if request.is_json:
            dados = request.get_json()
            
            if ('projectLaw' in dados and 'topic_id' in dados and 'topic' in dados and 
                'topic_description' in dados and 'matConsultant' in dados):
                projectLaw = dados['projectLaw']
                topic_id = dados['topic_id']
                topic = dados['topic']
                topic_description = dados['topic_description']
                matConsultant = dados['matConsultant']
                result = self.repositoryConsultantTopics.addConsultantTopics(
                    projectLaw= projectLaw,
                    topic_id= topic_id,
                    topic= topic,
                    topic_description= topic_description,
                    matConsultant=matConsultant
                    )

                if result is not None:
                    return jsonify(result),201
            else:
                jsonify({"message":"parametros incorretos"}), 500
        return 500

    def addConsultantTopicsBatch(self):
        if request.is_json():
            dados = request.get_json()
            if "topics" in dados:
                topics = dados["topics"]
                result = self.repositoryConsultantTopics.addConsultantTopicsBatch(topics)
                if result is not None:
                    return jsonify(result), 201
        return 500

    def getAllConsultantTopics(self):
        result = self.repositoryConsultantTopics.getAllConsultantTopics()
        if result is not None:
            return jsonify(outputJsonAllConsultantTopics(result)), 200
        return jsonify({"message":"Registro não encontrado"}),404

    def getConsultantTopics(self,id):
        result = self.repositoryConsultantTopics.getConsultantTopics(id)
        if result is not None:
            return jsonify(outputJsonConsultantTopics(result)), 200
        return jsonify({"message":"Registro não encontrado"}),404

    def deleteConsultantTopics(self):
        if request.is_json:
            dados = request.get_json()
            if "id" in dados:
                result = self.repositoryConsultantTopics.deleteConsultantTopics(dados['id'])
                if result is not None:
                    return jsonify(outputJsonConsultantTopics(result)), 202
                return jsonify({"message":"Registro não encontrado"}),404
