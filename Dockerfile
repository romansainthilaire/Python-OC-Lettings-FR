# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Install the PostgreSQL development package and build tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libpq-dev \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expose port 8000 for the Django app
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]