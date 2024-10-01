# Use the base image from Apache Airflow
FROM apache/airflow:2.0.1

# Switch to root user to install system dependencies
USER root

# Install required build tools and PostgreSQL libraries
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Switch back to the airflow user
USER airflow

# Copy the requirements.txt file into the container
COPY requirements.txt /requirements.txt

# Install Python dependencies from requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

# Upgrade pip to the latest version (optional but recommended)
RUN pip install --upgrade pip
