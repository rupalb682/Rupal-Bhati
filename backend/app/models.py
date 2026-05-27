from sqlalchemy import Column, Integer, String, Text
from database import Base

class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    topic = Column(String, index=True)
    difficulty = Column(String)
    description = Column(Text)
    sample_answer = Column(Text)

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    question_id = Column(Integer)
    user_answer = Column(Text)
    score = Column(Integer)
    feedback = Column(Text)