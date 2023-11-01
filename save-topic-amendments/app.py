from controller.controllerFeedbackModel import ControllerFeedbackModel
from controller.controllerFeedbackConsultant import ControllerFeedbackConsultant
from doc.controller.controllerDoc import ControllerDoc
from utils.initTables import initTables
from server.instance import server



if __name__ == "__main__":
    initTables()
    #Endpoints
    controllerFeedbackModel = ControllerFeedbackModel(app=server.app,engine=server.engine)
    controllerFeedbackConsultant = ControllerFeedbackConsultant(app=server.app,engine=server.engine)
    #Doc
    controllerDoc = ControllerDoc(server.api)
    server.start()
