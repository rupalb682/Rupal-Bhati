from pydantic import BaseModel
from typing import Optional

# Schemas for Questions
class QuestionBase(BaseModel):
    title: str
    topic: str
    difficulty: str
    description: str
    sample_answer: str

class QuestionCreate(QuestionBase):
    pass

class QuestionResponse(QuestionBase):
    id: int
    class Config:
        from_attributes = True

# Schemas for Answer Submissions
class AnswerSubmit(BaseModel):
    question_id: int
    user_answer: str

class SubmissionResponse(BaseModel):
    id: int
    question_id: int
    user_answer: str
    score: int
    feedback: str
    class Config:
        from_attributes = True