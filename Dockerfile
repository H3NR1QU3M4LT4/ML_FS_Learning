# Use an official Python runtime as the base image
FROM python:3.8-slim

# Set the working directory
WORKDIR /Learning

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Run the application
CMD ["python", "PySparkProject/main.py"]
