from sqlalchemy.orm import sessionmaker
from model.models import ConsultantTopics
from adapter.adapterConsultantTopics import outputJsonConsultantTopics, outputJsonAllConsultantTopics
from datetime import datetime

class RepositoryConsultantTopics:

    def __init__(self,engine):
        self.engine = engine

    def addConsultantTopics(self,projectLaw,topic_id,topic,topic_description,matConsultant):
        self.createSession()
        data_atual = datetime.now()
        consultant_topics = ConsultantTopics(projectLaw=projectLaw,topic_id=topic_id,topic=topic,
                                             topic_description=topic_description,matConsultant=matConsultant,dataAlteracao=data_atual)
        self.session.add(consultant_topics)
        self.session.commit()
        result = outputJsonConsultantTopics(consultant_topics)
        self.closeSession()
        return result

    def getAllConsultantTopics(self):
        self.createSession()
        result = self.session.query(ConsultantTopics).all()
        self.closeSession()
        return result

    def getConsultantTopics(self,id):
        self.createSession()
        result = self.session.query(ConsultantTopics).filter_by(id=id).first()
        self.closeSession()
        return result

    def deleteConsultantTopics(self,id):
        self.createSession()
        result = self.session.query(ConsultantTopics).filter_by(id=id).first()
        if result is not None:
            self.session.delete(result)
            self.session.commit()
            self.closeSession()
            return result
        self.closeSession()
        return None

    def createSession(self):
        self.session = sessionmaker(bind=self.engine)()

    def closeSession(self):
        self.session.close()
