# Use the official Python image as the base image
FROM python:3.9-slim-buster

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the container
COPY . .

# Expose port 8000
EXPOSE 8000

# Run the command to start the server
CMD ["python", "manage.py", "runserver", "gunicorn", "oc_lettings_site.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4"]
