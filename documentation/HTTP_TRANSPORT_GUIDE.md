# HTTP Transport Guide for Pennylane MCP Server

This guide explains how to use the HTTP transport capabilities of the Pennylane MCP server.

## Overview

The Pennylane MCP server now supports multiple transport protocols:
- **STDIO** (default): For local integrations like Claude Desktop
- **Streamable HTTP**: For web deployments and remote access
- **SSE** (legacy): For backward compatibility

## Quick Start

### Running with HTTP Transport

```bash
# Basic HTTP server on localhost:8000
python src/server.py --transport streamable-http

# Custom host and port
python src/server.py --transport streamable-http --host 0.0.0.0 --port 9000

# With debug logging
python src/server.py --transport streamable-http --log-level debug
```

### Using the Starter Script

```bash
# Make the script executable (first time only)
chmod +x start_server.sh

# Run with HTTP
./start_server.sh -t streamable-http

# Run on all interfaces
./start_server.sh -t streamable-http -h 0.0.0.0

# Run with Docker
./start_server.sh -d
```

## HTTP Endpoints

When running in HTTP mode, the server exposes:
- **`/mcp`**: Main MCP endpoint for all protocol communication
- **`/health`**: Health check endpoint returning server status

## Client Examples

### Python Client

```python
import asyncio
from fastmcp import Client

async def main():
    # Connect to HTTP server
    async with Client("http://localhost:8000/mcp") as client:
        # Get server info
        info = await client.call_tool("pennylane_server_info")
        print(info[0].text)
        
        # List customers
        customers = await client.call_tool("pennylane_customers_list", {"limit": 10})
        print(customers[0].text)
        
        # Read resources
        company = await client.read_resource("pennylane://company/info")
        print(company[0].text)

if __name__ == "__main__":
    asyncio.run(main())
```

### Using with cURL (Health Check)

```bash
# Check server health
curl http://localhost:8000/health

# Response:
# {"status":"healthy","server":"Pennylane MCP","version":"0.2.0"}
```

### Integration with Other Applications

```python
# In a FastAPI/Flask app
import httpx
from fastmcp import Client

async def get_pennylane_data():
    async with Client("http://pennylane-mcp:8000/mcp") as client:
        return await client.call_tool("pennylane_customers_list")
```

## Docker Deployment

### Using Docker Compose (Recommended)

Docker Compose is the easiest way to run the Pennylane MCP server:

```bash
# With environment variable
PENNYLANE_API_KEY=your_key_here docker-compose up -d

# Or using the helper script
chmod +x start_docker_compose.sh
PENNYLANE_API_KEY=your_key_here ./start_docker_compose.sh

# Available commands:
./start_docker_compose.sh up      # Start the server
./start_docker_compose.sh down    # Stop the server
./start_docker_compose.sh logs    # View logs
./start_docker_compose.sh rebuild # Rebuild and restart
./start_docker_compose.sh status  # Check status
```

#### Using a .env file

Create a `.env` file in the project root (recommended for development):
```env
PENNYLANE_API_KEY=your_key_here
# Optional overrides
PENNYLANE_BASE_URL=https://app.pennylane.com/api/external/v2
LOG_LEVEL=INFO
```

Then simply run:
```bash
docker-compose up -d
```

#### Docker Compose Features

- **Health checks**: Automatically monitors server health
- **Auto-restart**: Restarts on failure
- **Port mapping**: Exposes server on port 8000
- **Environment management**: Easy configuration via .env file

### Using Docker Directly

```bash
# Build the image
docker build -t pennylane-mcp .

# Run the container
docker run -p 8000:8000 \
  -e PENNYLANE_API_KEY=your_key_here \
  pennylane-mcp

# Run with custom settings
docker run -p 9000:8000 \
  -e PENNYLANE_API_KEY=your_key_here \
  -e LOG_LEVEL=DEBUG \
  pennylane-mcp \
  python src/server.py --transport streamable-http --host 0.0.0.0 --port 8000
```

**Note:** If you encounter a `ModuleNotFoundError: No module named 'src'` error, make sure to rebuild the Docker image with `docker build -t pennylane-mcp .` to include the latest Dockerfile changes that set the PYTHONPATH correctly.

### Testing Your Docker Setup

After building the image, you can test if the module imports are working correctly:

```bash
# Test the Docker setup
docker run --rm pennylane-mcp python test_docker.py

# Expected output:
# ✓ Successfully imported src.config
# ✓ Successfully imported src.mcp_instance
# All imports successful! Docker setup is working correctly.
```

If you see environment variable issues, the test script will show which environment variables are set.

## Production Deployment

### Security Considerations

1. **API Keys**: Never expose your API keys in logs or responses
2. **HTTPS**: Use a reverse proxy (nginx, traefik) for SSL/TLS
3. **Authentication**: Consider adding authentication middleware for public deployments
4. **Rate Limiting**: Implement rate limiting to prevent abuse

### Example Nginx Configuration

```nginx
server {
    listen 443 ssl;
    server_name mcp.yourdomain.com;
    
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    
    location /mcp {
        proxy_pass http://localhost:8000/mcp;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        
        # For long-running operations
        proxy_read_timeout 300s;
        proxy_connect_timeout 75s;
    }
    
    location /health {
        proxy_pass http://localhost:8000/health;
    }
}
```

### Systemd Service

Create `/etc/systemd/system/pennylane-mcp.service`:

```ini
[Unit]
Description=Pennylane MCP Server
After=network.target

[Service]
Type=simple
User=mcp
WorkingDirectory=/opt/pennylane-mcp
Environment="PATH=/opt/pennylane-mcp/venv/bin"
EnvironmentFile=/opt/pennylane-mcp/.env
ExecStart=/opt/pennylane-mcp/venv/bin/python src/server.py --transport streamable-http --host 127.0.0.1 --port 8000
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## Monitoring

### Health Checks

```bash
# Simple health check script
#!/bin/bash
if curl -f http://localhost:8000/health > /dev/null 2>&1; then
    echo "Pennylane MCP is healthy"
else
    echo "Pennylane MCP is down!"
    exit 1
fi
```

### Logging

The server logs all requests and errors. Set appropriate log levels:
- `debug`: Detailed information for debugging
- `info`: General operational information
- `warning`: Warning messages
- `error`: Error messages only

## Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Find process using port 8000
   lsof -i :8000
   # Kill the process if needed
   kill -9 <PID>
   ```

2. **Connection refused**
   - Check if the server is running: `ps aux | grep server.py`
   - Verify the host/port configuration
   - Check firewall rules

3. **API Key not recognized**
   If you get a validation error about missing API key:
   - Ensure you're using the correct environment variable name: `PENNYLANE_API_KEY`
   - Make sure to rebuild the Docker image after any Dockerfile changes
   - Test with the debug script: `docker run --rm -e PENNYLANE_API_KEY=your_key pennylane-mcp python test_docker.py`
   - Check that no .env file is being copied into the image (we use .dockerignore to prevent this)

4. **Timeout errors**
   - Increase client timeout settings
   - Check API response times
   - Monitor server resources

### Debug Mode

Run with debug logging to see detailed information:
```bash
python src/server.py --transport streamable-http --log-level debug
```

## Performance Tips

1. **Connection Pooling**: Reuse client connections when possible
2. **Async Operations**: Use async/await for concurrent operations
3. **Caching**: Cache frequently accessed resources
4. **Resource Limits**: Set appropriate limits for concurrent connections

## Migration from STDIO

If you're currently using STDIO transport (e.g., with Claude Desktop), you can run both transports simultaneously by:

1. Keep Claude Desktop configuration unchanged (uses STDIO)
2. Run HTTP transport on a different terminal for web access
3. Both will use the same codebase and configuration

## Examples Repository

See the `examples/` directory for more examples:
- `http_client_example.py`: Basic HTTP client usage
- More examples coming soon...

## Support

For issues or questions:
1. Check server logs for error details
2. Verify API credentials and connectivity
3. Test with the health endpoint first
4. Open an issue on GitHub with details 