# Use the official Python image as the base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Upgrade pip to the latest version
RUN pip install --upgrade pip
# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port that Flask will run on
EXPOSE 8000

# Define environment variable for Flask
# ENV FLASK_APP=app.py

# Command to run on container start
CMD './entrypoint.sh'
# CMD ["flask", "run", "--host=0.0.0.0"]