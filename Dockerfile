# Base image
FROM python:3.9.9-buster

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the source code into the container
COPY . .

# Expose the port
EXPOSE 8000

# Set the command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]