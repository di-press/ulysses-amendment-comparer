from doc.model.docFeedbackModel import DocFeedbackModel, DocFeedbackModelId,DocFeedbackModelBatch
from doc.model.docFeedbackConsultant import DocFeedbackConsultant, DocFeedbackConsultantId,DocFeedbackConsultantBatch
from utils.routers import MODEL,CONSULTANT


class ControllerDoc:

    def __init__(self,api):
        self.api = api
        DocFeedbackModel.api = self.api

        self.api.add_resource(DocFeedbackModel, MODEL)
        ns_model = self.api.namespace("Model", description='Rota do modelo')
        ns_model.add_resource(DocFeedbackModel, '/')
        ns_model.add_resource(DocFeedbackModelId,'/<int:id>')
        ns_model.add_resource(DocFeedbackModelBatch,'/batch')

        self.api.add_resource(DocFeedbackConsultant, CONSULTANT)
        ns_consultant = self.api.namespace("Consultant", description='Rota do consultor')
        ns_consultant.add_resource(DocFeedbackConsultant, '/')
        ns_consultant.add_resource(DocFeedbackConsultantId, '/<int:id>')
        ns_consultant.add_resource(DocFeedbackConsultantBatch, '/batch')