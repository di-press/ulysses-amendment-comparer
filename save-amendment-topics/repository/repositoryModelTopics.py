from sqlalchemy.orm import sessionmaker
from model.models import ModelTopics
from adapter.adapterModelTopics import outputJsonModelTopics


class RepositoryModelTopics:

    def __init__(self,engine):
        self.engine = engine

    def addModelTopics(self,projectLaw,topic_id,terms,configuration):
        self.createSession()
        model_topics = ModelTopics(projectLaw=projectLaw,topic_id=topic_id,terms=terms,configuration=configuration)
        self.session.add(model_topics)
        self.session.commit()
        result = outputJsonModelTopics(model_topics)
        self.closeSession()
        return result

    def getAllModelTopics(self):
        self.createSession()
        result = self.session.query(ModelTopics).all()
        self.closeSession()
        return result

    def getModelTopics(self,id):
        self.createSession()
        result = self.session.query(ModelTopics).filter_by(id=id).first()
        self.closeSession()
        return result

    def deleteModelTopics(self,id):
        self.createSession()
        result = self.session.query(ModelTopics).filter_by(id=id).first()
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