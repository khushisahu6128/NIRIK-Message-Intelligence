import re
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize


# Initialize tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    # 1. Convert text to lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r"http\S+|www\S+", "", text)

    # 3. Remove numbers and special characters
    text = re.sub(r"[^a-zA-Z\s]", "", text)

    # 4. Tokenization
    tokens = word_tokenize(text)

    # 5. Remove stop words
    tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # 6. Lemmatization
    tokens = [
        lemmatizer.lemmatize(word)
        for word in tokens
    ]

    # Convert tokens back into a sentence
    return " ".join(tokens)