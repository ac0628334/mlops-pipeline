FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY src/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source and model folders
COPY src/ src/
COPY models/ models/

# Expose Flask port
EXPOSE 5000

# Run Flask app (not uvicorn)
CMD ["python", "src/inference/app.py"]
