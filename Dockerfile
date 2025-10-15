# Use official Python image
FROM python:3.11-slim

# Set environment
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y build-essential libpq-dev --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install pip requirements
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /app/

# Collect static files
ENV DJANGO_SETTINGS_MODULE=divya_classes.settings
RUN python manage.py collectstatic --noinput || true

# Expose port and run gunicorn
EXPOSE 8080
CMD ["gunicorn", "divya_classes.wsgi:application", "--bind", "0.0.0.0:8080", "--workers", "3"]
