import joblib

MODEL_PATH = "models/iris_model.pkl"

def load_model():
    return joblib.load(MODEL_PATH)
