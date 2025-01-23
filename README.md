# Predictive Analysis for Manufacturing Operations

This project is a RESTful API for predictive analysis in manufacturing, capable of predicting machine downtime using simple ML models. The API provides endpoints for uploading data, training a model, and making predictions.

## *Features*
1. Upload a manufacturing dataset via /upload endpoint.
2. Train a machine learning model using the uploaded data via /train endpoint.
3. Predict machine downtime using the /predict endpoint.

---

## *How to Set Up and Run the API*

### *1. Clone the Repository*
```bash
git clone <repository-url>
cd predictive_analysis
```

### *Create and Activate Virtual Environment*
```bash
python -m venv env
env\Scripts\activate      # For Windows
```

### *Install Dependencies*
```bash
pip install -r requirements.txt
```

### *run Flask Application*
```bash
python app.py
```
#it will run automatically on http://127.0.0.1:5000/.

## *API Endpoints*

## *1. Upload Endpoint (POST /upload)*

 Upload a CSV file to train the model.

 Request Body: A CSV file with columns: Machine_ID, Temperature, Run_Time, Downtime_Flag.

# Response:
{
    "message": "Dataset uploaded successfully",
    "columns": ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"]
}

## *2. Train Endpoint (POST /train)*

# Train a machine learning model on the uploaded dataset.

# Response:
{
    "accuracy": 1.0,
    "f1_score": 1.0
}

## *3. Predict Endpoint (POST /predict)*

 Make predictions using the trained model.

# Request Body (JSON):
{
    "Temperature": 80,
    "Run_Time": 120
}

# Response:
{
    "Downtime": "Yes",
    "Confidence": 1.0
}

## *Sample Dataset*

 A sample dataset (sample_data.csv) is included in the data/ folder.

### *Dependencies*

 Flask
 scikit-learn
 joblib
 pandas
 Python 3.9+

## *Testing*

 Use tools like Postman or cURL to test the API endpoints.

## *Author*

# *Tashmeet Kaur Hora*
