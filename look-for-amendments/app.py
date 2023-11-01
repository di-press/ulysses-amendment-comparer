from controller.controller import Controller
from doc.controller.controllerDoc import ControllerDoc
from server.instance import server
if __name__ == '__main__':
    con = Controller(app=server.app)

    controllerDoc = ControllerDoc(server.api)
    server.start()
