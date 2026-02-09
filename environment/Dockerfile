# Use Ubuntu base image
FROM ubuntu:22.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Update package lists and install basic tools
# NOTE: We intentionally DO NOT install 'make' here - that's what the agent needs to fix
RUN apt-get update && apt-get install -y \
    gcc \
    libc6-dev \
    && rm -rf /var/lib/apt/lists/*

# Create workspace directory
RUN mkdir -p /workspace/src /workspace/build

# Set working directory
WORKDIR /workspace

# Copy the project files into the container
COPY --chown=root:root project_files/Makefile /workspace/
COPY --chown=root:root project_files/src/main.c /workspace/src/
COPY --chown=root:root project_files/build.sh /workspace/

# Make build script executable
RUN chmod +x /workspace/build.sh

# Note: Tests and solutions are NOT copied into the image
# They will be mounted or accessed separately by Harbor