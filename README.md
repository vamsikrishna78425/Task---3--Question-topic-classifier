# Question Topic Classifier

**Task 3 – Question Management Module**
**Intern:** Vamsi Krishna Darla
**Supervisor:** Vasudha Tayade | **Captain:** Ayesha Faquih

---

## Overview
A FastAPI-based classifier that categorizes questions into four topics:
- **OOP** – Object-Oriented Programming
- **Database** – SQL, NoSQL, Schema Design
- **Networking** – TCP/IP, DNS, Protocols
- **Machine Learning** – Models, Training, Neural Networks

---

## Project Structure

src/classifier.py  - Core classification logic
src/main.py        - FastAPI application
tests/test_classifier.py - Test cases
requirements.txt   - Dependencies
README.md          - Project documentation
---

## Setup & Run

Step 1: Install dependencies
pip install -r requirements.txt

Step 2: Run the API server
cd src
python main.py

Server runs at: http://localhost:8000
---

## API Usage

POST /classify

Request:
{
  "question": "What is polymorphism in Java?"
}

Response:
{
  "topic": "OOP",
  "confidence": "high"
}

GET /topics
Returns all available topic categories.
---

## Acceptance Criteria

- Classification accuracy > 80% ✅
- Handles questions spanning multiple topics ✅
- Returns structured JSON output ✅

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pytest

---

## Author

Intern: Vamsi Krishna Darla
Supervisor: Vasudha Tayade
Captain: Ayesha Faquih
Module: Question Management
Task: B4 - Question Categorization by Topic
