
from flask import Flask, request, render_template
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Load dataset
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names

# Safe HTML field names
HTML_FEATURE_NAMES = [name.replace(" ", "_").replace("(", "").replace(")", "") for name in feature_names]

FEATURE_RANGES = {html_name: (np.min(X[:, i]), np.max(X[:, i]))
                  for i, html_name in enumerate(HTML_FEATURE_NAMES)}

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X, y)

# Initialize Flask app
app = Flask(__name__)

# Flower image paths (relative to static folder)
FLOWER_IMAGES = {
    'setosa': '/static/images/setosa.jpg',
    'versicolor': '/static/images/versicolor.jpeg',
    'virginica': '/static/images/virginica.jpg'
}

@app.route("/", methods=["GET"])
def index():
    """Display the main form"""
    fields = list(zip(HTML_FEATURE_NAMES, feature_names))
    return render_template(
        'index.html', 
        fields=fields,
        ranges=FEATURE_RANGES,
        prediction=None
    )

@app.route("/predict", methods=["POST"])
def predict():
    """Handle prediction requests"""
    features = []
    warning_messages = []
    
    # Process form inputs
    for html_name, display_name in zip(HTML_FEATURE_NAMES, feature_names):
        try:
            val = float(request.form[html_name])
            min_val, max_val = FEATURE_RANGES[html_name]
            if val < min_val:
                warning_messages.append(f"{display_name} is below minimum ({min_val:.1f})")
            elif val > max_val:
                warning_messages.append(f"{display_name} is above maximum ({max_val:.1f})")
            features.append(val)
        except (ValueError, KeyError):
            warning_messages.append(f"{display_name} is invalid or missing")
            features.append(0.0)
    
    # Make prediction
    features_np = np.array([features])
    prediction_idx = model.predict(features_np)[0]
    prediction_label = target_names[prediction_idx]
    probs = model.predict_proba(features_np)[0]
    confidences = {target_names[i]: probs[i] for i in range(len(target_names))}
    
    # Prepare response
    warning_text = " | ".join(warning_messages) if warning_messages else None
    fields = list(zip(HTML_FEATURE_NAMES, feature_names))
    
    return render_template(
        'index.html',
        prediction=prediction_idx,
        label=prediction_label,
        confidences=confidences,
        warning=warning_text,
        fields=fields,
        ranges=FEATURE_RANGES,
        flower_images=FLOWER_IMAGES
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)
