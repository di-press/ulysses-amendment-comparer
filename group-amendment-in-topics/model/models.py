from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,VARCHAR,DateTime,Float


Base = declarative_base()


class FeedbackModelo(Base):

    __tablename__ = "feedback_model"

    id = Column(Integer, primary_key=True)
    projectLaw = Column(VARCHAR)
    amendment = Column(VARCHAR)
    topic = Column(VARCHAR)
    score_standardized = Column(Float)


class FeedbackConsultor(Base):

    __tablename__ = "feedback_consultant"
    id = Column(Integer, primary_key=True)
    projectLaw = Column(VARCHAR)
    amendment = Column(VARCHAR)
    topic = Column(VARCHAR)
    matConsultant = Column(VARCHAR)
    dataAlteracao = Column(DateTime)
    #score_normalizado

