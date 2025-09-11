FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code
COPY src/ src/

# Copy the trained model
COPY src/irish_module.pkl ./irish_module.pkl

# Expose Flask port
EXPOSE 5000

# Run Flask app
CMD ["python", "src/inference/app.py"]
