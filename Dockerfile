# Base image with Python
FROM python:3.10-slim

# Install system dependencies for Appium and Android automation
RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    openjdk-11-jdk \
    android-sdk \
    && apt-get clean

# Set environment variables for Java & Android
ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV ANDROID_HOME=/opt/android-sdk
ENV PATH=$PATH:$ANDROID_HOME/tools:$ANDROID_HOME/platform-tools

# Create directory for Android SDK
RUN mkdir -p /opt/android-sdk

# Optional: Install Appium via npm (if running server inside container)
# RUN apt-get install -y nodejs npm && npm install -g appium

# Set working directory
WORKDIR /app

# Copy project files into container
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Default command to run your test script
# Replace 'test_app.py' with your actual script
CMD ["python", "login.py"]
