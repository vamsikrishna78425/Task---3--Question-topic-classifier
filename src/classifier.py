TOPIC_KEYWORDS = {
    "OOP": [
        "class", "object", "inheritance", "polymorphism",
        "encapsulation", "abstraction", "method", "constructor",
        "interface", "overriding", "overloading", "instance",
        "subclass", "superclass", "access modifier", "oop"
    ],
    "Database": [
        "sql", "query", "table", "join", "index",
        "normalization", "schema", "transaction", "crud",
        "primary key", "foreign key", "database", "nosql",
        "mongodb", "mysql", "postgresql", "select", "insert",
        "update", "delete", "acid", "view", "stored procedure"
    ],
    "Networking": [
        "tcp", "ip", "dns", "http", "socket",
        "protocol", "bandwidth", "router", "firewall",
        "network", "subnet", "osi", "mac address", "udp",
        "packet", "latency", "vpn", "ssl", "tls", "port",
        "https", "ftp", "ssh", "proxy"
    ],
    "Machine Learning": [
        "model", "training", "neural", "dataset",
        "overfitting", "regression", "classification",
        "feature", "gradient", "machine learning", "ml",
        "deep learning", "supervised", "unsupervised",
        "algorithm", "accuracy", "prediction", "epoch",
        "backpropagation", "loss function", "clustering"
    ]
}

PRIORITY_ORDER = ["Machine Learning", "OOP", "Database", "Networking"]


def classify_topic(question: str) -> dict:
    """
    Classify a question into one of four topics:
    OOP, Database, Networking, Machine Learning.
    Returns topic and confidence score.
    """
    question_lower = question.lower()
  
    scores = {topic: 0 for topic in TOPIC_KEYWORDS}
    for topic, keywords in TOPIC_KEYWORDS.items():
        for keyword in keywords:
            if keyword in question_lower:
                scores[topic] += 1

    max_score = max(scores.values())

    if max_score == 0:
        return {
            "topic": "Networking",
            "confidence": "low",
            "scores": scores
        }

    candidates = [t for t, s in scores.items() if s == max_score]
    selected_topic = candidates[0]
    for p in PRIORITY_ORDER:
        if p in candidates:
            selected_topic = p
            break

    confidence = "high" if max_score >= 3 else "medium" if max_score >= 1 else "low"

    return {
        "topic": selected_topic,
        "confidence": confidence,
        "scores": scores
    }
