from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from classifier import classify_topic

app = FastAPI(
    title="Question Topic Classifier",
    description="Classifies questions into topics: OOP, Database, Networking, Machine Learning",
    version="1.0.0"
)

class QuestionInput(BaseModel):
    question: str

class TopicResponse(BaseModel):
    topic: str
    confidence: str
    scores: dict

@app.get("/")
def root():
    return {"message": "Question Topic Classifier API is running"}

@app.post("/classify", response_model=TopicResponse)
def classify(input: QuestionInput):
    if not input.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    result = classify_topic(input.question)
    return result

@app.get("/topics")
def get_topics():
    return {
        "topics": ["OOP", "Database", "Networking", "Machine Learning"]
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
