import sys
import os
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Add the src directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

def test_model_training():
    """Test that the model can be trained"""
    iris = load_iris()
    X, y = iris.data, iris.target
    
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X, y)
    
    # Test prediction
    prediction = model.predict([[5.1, 3.5, 1.4, 0.2]])
    assert prediction[0] in [0, 1, 2]  # Valid iris class
    
    # Test model accuracy
    accuracy = model.score(X, y)
    assert accuracy > 0.9  # Should have good accuracy on training data

def test_prediction_format():
    """Test that predictions are in expected format"""
    iris = load_iris()
    X, y = iris.data, iris.target
    
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X, y)
    
    # Test single prediction
    single_pred = model.predict([[5.1, 3.5, 1.4, 0.2]])
    assert len(single_pred) == 1
    assert isinstance(single_pred[0], (int, np.integer))
    
    # Test prediction probabilities
    proba = model.predict_proba([[5.1, 3.5, 1.4, 0.2]])
    assert proba.shape == (1, 3)  # 1 sample, 3 classes
    assert np.isclose(np.sum(proba), 1.0)  # Probabilities should sum to 1