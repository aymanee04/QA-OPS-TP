FROM python:3.13-slim

ENV DEBIAN_FRONTEND=noninteractive

# Install Chromium, Node.js and system dependencies
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    curl \
    wget \
    git \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g newman allure-commandline \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ui-tests/requirements.txt /app/ui-tests/requirements.txt

RUN pip install --no-cache-dir -r /app/ui-tests/requirements.txt

COPY . /app

RUN mkdir -p /app/reports

ENV PYTHONPATH=/app/ui-tests

CMD ["pytest", "ui-tests/tests", "-v"]