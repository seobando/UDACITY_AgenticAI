FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# Install additional system dependencies if needed
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        git \
        curl \
        wget \
        vim \
        nano \
    && apt-get autoremove -y && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Install Python development tools
RUN pip install --upgrade pip setuptools wheel

# Set environment variables
ENV PYTHONPATH=/workspaces/Agentic\ AI
ENV PYTHONUNBUFFERED=1

# Create workspace directory
WORKDIR /workspaces 