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
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    import os

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
