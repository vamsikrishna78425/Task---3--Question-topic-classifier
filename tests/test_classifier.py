import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from classifier import classify_topic

def test_oop():
    result = classify_topic("What is polymorphism in Java?")
    assert result["topic"] == "OOP"

def test_database():
    result = classify_topic("Explain SQL JOIN types with examples.")
    assert result["topic"] == "Database"

def test_networking():
    result = classify_topic("How does TCP/IP work in networking?")
    assert result["topic"] == "Networking"

def test_ml():
    result = classify_topic("What is gradient descent in machine learning?")
    assert result["topic"] == "Machine Learning"

def test_multi_topic():
    result = classify_topic("How does a neural network use object-oriented class design?")
    assert result["topic"] in ["OOP", "Machine Learning"]

def test_empty():
    result = classify_topic("")
    assert "topic" in result

def test_accuracy():
    test_cases = [
        ("What is polymorphism?", "OOP"),
        ("Explain SQL JOIN.", "Database"),
        ("How does TCP work?", "Networking"),
        ("What is gradient descent?", "Machine Learning"),
        ("What is inheritance in Java?", "OOP"),
        ("What is a primary key?", "Database"),
        ("What is DNS resolution?", "Networking"),
        ("Explain neural network training.", "Machine Learning"),
        ("What is method overloading?", "OOP"),
        ("What is database normalization?", "Database"),
    ]
    correct = sum(1 for q, e in test_cases if classify_topic(q)["topic"] == e)
    assert correct / len(test_cases) >= 0.80
