from pathlib import Path
import joblib
from src.preprocess import preprocess_text

BASE = Path(__file__).resolve().parents[1]
MODEL_PATH = BASE / "models" / "spam_classifier.pkl"
VECTORIZER_PATH = BASE / "models" / "tfidf_vectorizer.pkl"

if not MODEL_PATH.exists() or not VECTORIZER_PATH.exists():
    raise FileNotFoundError(
        "NIRIK model files were not found. Expected models/spam_classifier.pkl "
        "and models/tfidf_vectorizer.pkl in the project folder."
    )

MODEL = joblib.load(MODEL_PATH)
TFIDF = joblib.load(VECTORIZER_PATH)


def classify_message(message: str):
    """Return (predicted_label, probability_of_that_label)."""
    cleaned = preprocess_text(message)
    features = TFIDF.transform([cleaned])
    prediction = MODEL.predict(features)[0]

    if hasattr(MODEL, "predict_proba"):
        probabilities = MODEL.predict_proba(features)[0]
        classes = list(MODEL.classes_)
        confidence = float(probabilities[classes.index(prediction)])
    else:
        confidence = 0.0

    return str(prediction), confidence
