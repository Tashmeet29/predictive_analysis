from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score

app = Flask(__name__)
model = None  # Placeholder for the trained model
dataset = None  # Placeholder for uploaded dataset

# Default Route: Check if server is running
@app.route('/')
def home():
    return "Flask API is running! Use POST methods for upload, train, and predict."

# Upload Endpoint: Accepts a CSV file and loads it into a pandas DataFrame
@app.route('/upload', methods=['POST'])
def upload_data():
    global dataset
    file = request.files['file']  # Get the file from the request
    dataset = pd.read_csv(file)  # Read the file into a pandas DataFrame
    return jsonify({"message": "Dataset uploaded successfully", "columns": list(dataset.columns)})

# Train Endpoint: Trains the model on the uploaded dataset and returns performance metrics
@app.route('/train', methods=['POST'])
def train_model():
    global model, dataset
    if dataset is None:
        return jsonify({"error": "No dataset uploaded"}), 400

    # Select the features (Temperature, Run_Time) and target (Downtime_Flag)
    X = dataset[['Temperature', 'Run_Time']]
    y = dataset['Downtime_Flag']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a decision tree classifier
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Save the trained model
    joblib.dump(model, 'model/model.pkl')

    return jsonify({"accuracy": accuracy, "f1_score": f1})

# Predict Endpoint: Accepts input in JSON format and returns predictions
@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({"error": "Model not trained"}), 400

    data = request.get_json()  # Get JSON data from the request
    X = [[data['Temperature'], data['Run_Time']]]  # Prepare input features for prediction
    prediction = model.predict(X)[0]  # Make the prediction
    confidence = max(model.predict_proba(X)[0])  # Get the confidence score

    return jsonify({"Downtime": "Yes" if prediction == 1 else "No", "Confidence": confidence})

if __name__ == '__main__':
    app.run(debug=True)