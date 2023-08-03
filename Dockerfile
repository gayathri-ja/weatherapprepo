# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /weatherapp

# Copy the current directory contents into the container at /app
COPY . /weatherapp

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 for the Flask app
EXPOSE 8080

# Set environment variable for Flask app
ENV PORT=8080

# Run the Flask app
CMD ["python", "app.py"]

