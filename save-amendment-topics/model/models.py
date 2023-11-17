from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,VARCHAR,DateTime


Base = declarative_base()


class ModelTopics(Base):

    __tablename__ = "model_topics"

    id = Column(Integer, primary_key=True)
    projectLaw = Column(VARCHAR)
    topic_id = Column(VARCHAR)
    terms = Column(VARCHAR)
    configuration = Column(VARCHAR)

class ConsultantTopics(Base):

    __tablename__ = "consultant_topics"

    id = Column(Integer, primary_key=True)
    projectLaw = Column(VARCHAR)
    topic_id = Column(VARCHAR)
    topic = Column(VARCHAR)
    topic_description = Column(VARCHAR)
    matConsultant = Column(VARCHAR)
    dataAlteracao = Column(DateTime)

