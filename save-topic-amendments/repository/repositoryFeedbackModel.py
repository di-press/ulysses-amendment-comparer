from sqlalchemy.orm import sessionmaker
from model.models import FeedbackModelo
from adapter.adapterFeedbackModel import outputJsonFeedbackModel,outputJsonFeedbackModels


class RepositoryFeedbackModel:

    def __init__(self,engine):
        self.engine = engine

    def addFeedbackModel(self,projectLaw,amendment,topic,score_standardized):
        self.createSession()
        feedbackModel = FeedbackModelo(projectLaw=projectLaw,amendment=amendment,topic=topic,score_standardized=score_standardized)
        self.session.add(feedbackModel)
        self.session.commit()
        result = outputJsonFeedbackModel(feedbackModel)
        self.closeSession()
        return result

    def addFeedbackModelBatch(self,models):
        listModels = []
        self.createSession()
        for model in models:
            feedbackModel = FeedbackModelo(projectLaw=model['projectLaw'], amendment=model['amendment'], topic=model['topic'],score_standardized=model['score_standardized'])
            listModels.append(feedbackModel)
            self.session.add(feedbackModel)
        self.session.commit()
        result = outputJsonFeedbackModels(listModels)
        self.closeSession()
        return {"models":result}

    def getFeedbackModels(self):
        self.createSession()
        result = self.session.query(FeedbackModelo).all()
        self.closeSession()
        return result

    def getFeedbackModel(self,id):
        self.createSession()
        result = self.session.query(FeedbackModelo).filter_by(id=id).first()
        self.closeSession()
        return result

    def deleteFeedbackModel(self,id):
        self.createSession()
        result = self.session.query(FeedbackModelo).filter_by(id=id).first()
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