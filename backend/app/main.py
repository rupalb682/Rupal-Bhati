from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

# Standard absolute imports (assumes your terminal is running inside the 'app' directory)
import models
import schemas
import database
from database import engine, get_db

# Create database tables automatically on startup
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Smart Interview & Learning API")

# Enable CORS so your frontend can communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to the Smart Interview Question and Learning System API"}

# --- QUESTION ENDPOINTS ---

@app.post("/questions/", response_model=schemas.QuestionResponse, status_code=201)
def create_question(question: schemas.QuestionCreate, db: Session = Depends(get_db)):
    db_question = models.Question(**question.model_dump())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question