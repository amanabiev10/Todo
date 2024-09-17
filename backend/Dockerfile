# Dockerfile
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy requirements.txt to the container
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port that the application will run on
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "backend.backend.wsgi:application"]
