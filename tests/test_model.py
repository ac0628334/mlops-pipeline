#import os
import joblib
#from src.training.train import train, MODEL_PATH

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))




def test_model_training():
    if os.path.exists(MODEL_PATH):
        os.remove(MODEL_PATH)
    train()
    assert os.path.exists(MODEL_PATH)
    model_bundle = joblib.load(MODEL_PATH)
    assert "model" in model_bundle
