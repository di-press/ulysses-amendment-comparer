from sqlalchemy.orm import sessionmaker
from model.models import FeedbackConsultor
from adapter.adapterFeedbackConsultant import outputJsonFeedbackConsultant,outputJsonFeedbackConsultants
from datetime import datetime

class RepositoryFeedbackConsultant:

    def __init__(self,engine):
        self.engine = engine

    def addFeedbackConsultant(self,projectLaw,amendment,topic,matConsultant):
        self.createSession()
        data_atual = datetime.now()
        feedbackConsultor = FeedbackConsultor(projectLaw=projectLaw,amendment=amendment,topic=topic,matConsultant=matConsultant,dataAlteracao=data_atual)
        self.session.add(feedbackConsultor)
        self.session.commit()
        result = outputJsonFeedbackConsultant(feedbackConsultor)
        self.closeSession()
        return result

    def addFeedbackConsultantBatch(self,feedbacks):
        listFeedbacks = []
        data_atual = datetime.now()
        self.createSession()
        for feedback in feedbacks:
            feed = FeedbackConsultor(projectLaw=feedback['projectLaw'],amendment=feedback['amendment'],topic=feedback['topic'],matConsultant=feedback['matConsultant'],dataAlteracao=data_atual)
            listFeedbacks.append(feed)
            self.session.add(feed)
        self.session.commit()
        result = outputJsonFeedbackConsultants(listFeedbacks)
        self.closeSession()
        return {"feedbacks":result}

    def getFeedbackConsultants(self):
        self.createSession()
        result = self.session.query(FeedbackConsultor).all()
        self.closeSession()
        return result

    def getFeedbackConsultant(self,id):
        self.createSession()
        result = self.session.query(FeedbackConsultor).filter_by(id=id).first()
        self.closeSession()
        return result

    def deleteFeedbackConsultant(self,id):
        self.createSession()
        result = self.session.query(FeedbackConsultor).filter_by(id=id).first()
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