import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split # type: ignore
from sklearn.feature_extraction.text import TfidfVectorizer # type: ignore
from sklearn.naive_bayes import MultinomialNB # type: ignore
from sklearn.metrics import accuracy_score, classification_report # type: ignore
import joblib # type: ignore

# Example dataset (replace this with a real dataset)
data = pd.DataFrame({
    'text': [
        "Congratulations, you've won!", 
        "Your account has been compromised", 
        "Hello, how are you?", 
        "Important message regarding your bank account",
        "Get rich quick with this simple trick!", 
        "Reminder: Your bank statement is ready."
    ],
    'label': [1, 1, 0, 1, 1, 0]  # 1 = Scam, 0 = Safe (fixed label for bank message)
})

# Text preprocessing and feature extraction
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(data['text'])
y = data['label']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a classifier
model = MultinomialNB()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Save the model and vectorizer
joblib.dump(model, 'scam_detection_model.pkl')  # Save the trained model
joblib.dump(vectorizer, 'vectorizer.pkl')  # Save the vectorizer

print("Model and vectorizer saved successfully!")


