# Your Original Code

## File 1: app.py
from flask import Flask, request, jsonify, render_template
import joblib
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

# Load the trained model and vectorizer
MODEL_FILE = "scam_detection_model.pkl"
VECTORIZER_FILE = "vectorizer.pkl"  # Ensure this matches the saved file name

if not os.path.exists(MODEL_FILE) or not os.path.exists(VECTORIZER_FILE):
    print("Error: Model or vectorizer files not found. Please train and save them first.")
    exit()

model = joblib.load(MODEL_FILE)
vectorizer = joblib.load(VECTORIZER_FILE)

def predict_scam(text):
    """Predicts whether a given text is a scam or not."""
    try:
        text_vectorized = vectorizer.transform([text])
        prediction = model.predict(text_vectorized)[0]
        return "Scam" if prediction == 1 else "Not Scam"
    except Exception as e:
        return f"Error during prediction: {e}"

@app.route('/')
def home():
    """Render the HTML page."""
    return render_template("index.html")

@app.route('/check-scam', methods=['POST'])
def check_scam():
    """API endpoint to check if a text is a scam."""
    data = request.json
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    prediction = predict_scam(text)
    return jsonify({'isScam': prediction == "Scam"})

if __name__ == '__main__':
    app.run(debug=True)


## File 2: train_scam_detection_model.py
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
