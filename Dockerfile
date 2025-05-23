# Use OpenJDK base with Java 11
FROM openjdk:11-slim

# Install Python, pip, curl, and unzip
RUN apt-get update && \
    apt-get install -y python3 python3-pip curl unzip && \
    apt-get clean

# Set Android SDK root path
ENV ANDROID_SDK_ROOT /sdk

# Download and set up Android command line tools
RUN mkdir -p ${ANDROID_SDK_ROOT}/cmdline-tools && \
    curl -o sdk.zip https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip && \
    unzip sdk.zip -d ${ANDROID_SDK_ROOT}/cmdline-tools && \
    mv ${ANDROID_SDK_ROOT}/cmdline-tools/cmdline-tools ${ANDROID_SDK_ROOT}/cmdline-tools/latest && \
    rm sdk.zip

# Add SDK tools to PATH
ENV PATH ${PATH}:${ANDROID_SDK_ROOT}/cmdline-tools/latest/bin

# Install Appium Python client
RUN pip3 install appium-python-client

# Set working directory and copy your code
WORKDIR /app
COPY . .

# Default command to keep container alive or override in Jenkins
CMD ["bash"]
