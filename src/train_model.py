import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from preprocess import preprocess_text


# Load dataset
df = pd.read_csv(
    "data/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)

# Preprocess messages
df["clean_message"] = df["message"].apply(preprocess_text)


# Separate input and target
X = df["clean_message"]
y = df["label"]


# Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# Create TF-IDF vectorizer
tfidf = TfidfVectorizer()


# Learn vocabulary from training data and transform it
X_train_tfidf = tfidf.fit_transform(X_train)


# Transform test data using the same vocabulary
X_test_tfidf = tfidf.transform(X_test)


# Display results
print("Training messages:", len(X_train))
print("Testing messages:", len(X_test))

print("Training TF-IDF shape:", X_train_tfidf.shape)
print("Testing TF-IDF shape:", X_test_tfidf.shape)



from sklearn.linear_model import LogisticRegression


# Create Logistic Regression model
model = LogisticRegression(max_iter=1000)

# Train the model
model.fit(X_train_tfidf, y_train)

# Make predictions on test data
y_pred = model.predict(X_test_tfidf)

# Display some predictions
print("\nFirst 10 predictions:")
print(y_pred[:10])

print("\nActual labels:")
print(y_test.iloc[:10].values)


from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


# Calculate evaluation metrics
accuracy = accuracy_score(y_test, y_pred)

precision = precision_score(
    y_test,
    y_pred,
    pos_label="spam"
)

recall = recall_score(
    y_test,
    y_pred,
    pos_label="spam"
)

f1 = f1_score(
    y_test,
    y_pred,
    pos_label="spam"
)

cm = confusion_matrix(
    y_test,
    y_pred,
    labels=["ham", "spam"]
)


# Display results
print("\n--- Model Evaluation ---")
print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1 Score :", f1)

print("\nConfusion Matrix:")
print(cm)




import joblib

# Save trained model
joblib.dump(model, "models/spam_classifier.pkl")

# Save TF-IDF vectorizer
joblib.dump(tfidf, "models/tfidf_vectorizer.pkl")

print("\nModel and TF-IDF vectorizer saved successfully!")