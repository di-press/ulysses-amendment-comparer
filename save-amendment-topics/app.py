from controller.ControllerModelTopics import ControllerModelTopics
from controller.ControllerConsultantTopics import ControllerConsultantTopics
from doc.controller.controllerDoc import ControllerDoc
from utils.initTables import initTables
from server.instance import server

if __name__ == "__main__":
    initTables()

    controllerConsultant = ControllerConsultantTopics(app=server.app,engine=server.engine)
    controllerModel = ControllerModelTopics(app=server.app,engine=server.engine)
    
    controllerDoc = ControllerDoc(server.api)
    server.start()