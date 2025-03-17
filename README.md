# Scam Detection API

## Overview
This project is a **Flask-based API** for detecting scam messages using a **Naïve Bayes model** trained on text data. It provides an endpoint to analyze text input and determine whether it is a potential scam.

This project was created as part of a **state-level hackathon**.

## Features
- **Train a scam detection model** using `train_scam_detection_model.py`
- **Test the model** using `test_scam_detection.py`
- **Deploy a Flask API** for scam detection (`app.py`)
- **Predict scam messages via API** (`/check-scam` endpoint)

## File Structure
- `app.py` - Flask application to serve the scam detection API
- `train_scam_detection_model.py` - Script to train and save the model
- `test_scam_detection.py` - Script to test predictions with sample text
- `scam_detection_model.pkl` - Saved trained model
- `vectorizer.pkl` - Saved text vectorizer

## Installation
### Prerequisites
Ensure you have **Python 3.x** installed along with the required dependencies:

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install the necessary packages manually:
```bash
pip install flask joblib scikit-learn pandas numpy
```

## Usage
### 1. Train the Model
To train a new model, run:
```bash
python train_scam_detection_model.py
```

This will generate `scam_detection_model.pkl` and `vectorizer.pkl`.

### 2. Test the Model
Run the test script:
```bash
python test_scam_detection.py
```

### 3. Start the Flask API
Run the Flask app:
```bash
python app.py
```

The API will be available at: `http://127.0.0.1:5000/`

### 4. Use the Scam Detection API
Send a **POST request** to `/check-scam` with a JSON payload:
```json
{
  "text": "Congratulations, you've won a lottery!"
}
```
Response:
```json
{
  "isScam": true
}
```

## API Endpoints
| Method | Endpoint     | Description           |
|--------|-------------|-----------------------|
| `GET`  | `/`         | Serve the homepage    |
| `POST` | `/check-scam` | Predict if text is a scam |

## Logging & Error Handling
- The application logs errors if the model or vectorizer is missing.
- Handles missing input and returns appropriate HTTP error codes.

## Future Improvements
- Improve dataset and model accuracy
- Add support for more ML algorithms
- Create a web-based UI for scam detection

## License
This project is open-source and can be modified freely.
