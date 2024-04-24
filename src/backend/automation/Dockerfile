# Start from a Python base image
FROM python:3.8-slim

# Install Task
RUN apt-get update && apt-get install -y curl
RUN curl -s https://taskfile.dev/install.sh | sh

# Copy your project files into the Docker image
COPY . /app

# Set the working directory
WORKDIR /app

# Run the task command
CMD ["task", "run"]