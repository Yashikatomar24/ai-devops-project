from fastapi import FastAPI
import joblib
from pydantic import BaseModel

app = FastAPI()

# Load model
model = joblib.load("model.pkl")

# Define input format
class InputData(BaseModel):
    features: list

@app.get("/")
def home():
    return {"message": "AI Model API is running"}

@app.post("/predict")
def predict(data: InputData):
    prediction = model.predict([data.features])
    return {"prediction": int(prediction[0])}