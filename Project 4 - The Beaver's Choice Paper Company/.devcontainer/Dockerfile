FROM mcr.microsoft.com/devcontainers/python:1-3.11-bullseye

# --- [1] Install dependencies and build SQLite >= 3.35 ---
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
        build-essential \
        wget \
        libreadline-dev \
        libsqlite3-dev \
        zlib1g-dev \
        curl \
        git \
        vim \
        nano \
    && rm -rf /var/lib/apt/lists/*

# Build SQLite from source (version 3.45.0 or later)
RUN wget https://www.sqlite.org/2024/sqlite-autoconf-3450000.tar.gz && \
    tar xzf sqlite-autoconf-3450000.tar.gz && \
    cd sqlite-autoconf-3450000 && \
    ./configure --prefix=/usr/local && \
    make -j$(nproc) && \
    make install && \
    cd .. && rm -rf sqlite-autoconf-3450000*

# Make sure system uses updated SQLite
ENV LD_LIBRARY_PATH="/usr/local/lib:$LD_LIBRARY_PATH"
ENV PATH="/usr/local/bin:$PATH"

# --- [2] Upgrade pip & Python tools ---
RUN pip install --upgrade pip setuptools wheel

# --- [3] Set Python environment ---
ENV PYTHONPATH=/workspaces/Agentic\ AI
ENV PYTHONUNBUFFERED=1

WORKDIR /workspaces