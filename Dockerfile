# Use official Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the sensor simulator script
COPY sensor_simulator.py .

# Expose port if your simulator serves data (optional)
EXPOSE 5000

# Command to run the simulator
CMD ["python", "sensor_simulator.py"]
