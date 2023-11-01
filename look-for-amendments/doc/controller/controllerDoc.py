from doc.model.DocApi import DocApi,DocApiBatch
from util.routers import SEARCH


class ControllerDoc:

    def __init__(self,api):
        self.api = api

        self.api.add_resource(DocApi,SEARCH)
        ns_api = self.api.namespace("search",description="Rota da busca")
        ns_api.add_resource(DocApi,'/')
        ns_api.add_resource(DocApiBatch, '/batch')


