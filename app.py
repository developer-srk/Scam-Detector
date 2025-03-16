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

