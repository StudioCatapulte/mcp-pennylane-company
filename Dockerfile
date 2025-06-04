FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Set Python path to include the app directory
ENV PYTHONPATH=/app

# Create a non-root user
RUN useradd -m -u 1000 mcp && chown -R mcp:mcp /app
USER mcp

# Expose the default HTTP port
EXPOSE 8000

# Default command (can be overridden by docker-compose or docker run)
CMD ["python", "src/server.py", "--transport", "streamable-http", "--host", "0.0.0.0", "--port", "8000"] 