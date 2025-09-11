# Use slim Python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements file and install dependencies
COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire source code
COPY src/ src/

# Copy trained model
COPY models/iris_model.pkl ./iris_model.pkl




# Expose port used by Flask app
EXPOSE 5000

# Run the Flask app
CMD ["python", "src/inference/app.py"]
