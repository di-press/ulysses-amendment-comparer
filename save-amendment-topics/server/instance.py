from flask import Flask
from sqlalchemy import create_engine
from utils.config import PATH, HOST, PORT
from flask_restplus import Api
from utils.infoAPI import *

class Instance:
    def __init__(self,host,port,debug):
        self.app = Flask(__name__)
        self.host = host
        self.port = port
        self.debug = debug
        self.engine = create_engine(PATH)
        self.api = Api(self.app,version=VERSION,title=TITLE,description=DESCRIPTION)


    def start(self):
        self.app.run(self.host, self.port, debug=self.debug)

server = Instance(HOST, PORT, True)
