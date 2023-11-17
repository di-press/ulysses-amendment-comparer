from doc.model.docModelTopics import DocModelTopics, DocModelTopicsId
from doc.model.docConsultantTopics import DocConsultantTopics, DocConsultantTopicsId
from utils.routers import MODEL, CONSULTANT
from collections.abc import MutableMapping

class ControllerDoc:
        
        def __init__(self, api):
                self.api = api
                DocModelTopics.api = self.api

                self.api.add_resource(DocModelTopics, MODEL)
                ns_model = self.api.namespace("Model", description="Rota do modelo")
                ns_model.add_resource(DocModelTopics, '/')
                ns_model.add_resource(DocModelTopicsId, '/<int:id>')

                self.api.add_resource(DocConsultantTopics, CONSULTANT)
                ns_consultant = self.api.namespace("Consultant", description="Rota do consultor")
                ns_consultant.add_resource(DocConsultantTopics, '/')
                ns_consultant.add_resource(DocConsultantTopicsId, '/<int:id>')
