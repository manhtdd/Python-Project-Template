# Use the latest Ubuntu image
FROM ubuntu:latest

# Set the working directory
WORKDIR /app

# Copy the project files to the working directory
COPY . /app

# Update the package list
RUN apt-get update

# Install Python, pip, and git
RUN apt-get install -y python3 python3-pip python3-venv git

# Create a Python virtual environment
RUN python3 -m venv /app/venv

# Activate the virtual environment and install the required Python packages
RUN /bin/bash -c "source /app/venv/bin/activate && pip install -r requirements.txt"

# Set the virtual environment as the default Python environment
ENV VIRTUAL_ENV=/app/venv
ENV PATH="/app/venv/bin:$PATH"