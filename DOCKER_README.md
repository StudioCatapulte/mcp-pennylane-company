# Docker Guide for Pennylane MCP Server

This guide provides quick instructions for running the Pennylane MCP server with Docker.

## 🚀 Quick Start with Docker Compose

### 1. Set your API key

```bash
# Option A: Environment variable
export PENNYLANE_API_KEY=your_key_here

# Option B: Create a .env file
echo "PENNYLANE_API_KEY=your_key_here" > .env
```

### 2. Start the server

```bash
# Using docker-compose directly
docker-compose up -d

# Or using the helper script
chmod +x start_docker_compose.sh
./start_docker_compose.sh up
```

### 3. Verify it's running

```bash
# Check status
docker-compose ps

# Test health endpoint
curl http://localhost:8000/health

# View logs
docker-compose logs -f pennylane-mcp
```

## 📋 Helper Script Commands

The `start_docker_compose.sh` script provides convenient commands:

```bash
./start_docker_compose.sh up      # Start the server
./start_docker_compose.sh down    # Stop the server
./start_docker_compose.sh logs    # View logs
./start_docker_compose.sh rebuild # Rebuild and restart
./start_docker_compose.sh status  # Check status
```

## 🔧 Configuration

### Environment Variables

- `PENNYLANE_API_KEY`: Your Pennylane API key (required)
- `PENNYLANE_BASE_URL`: API base URL (default: https://app.pennylane.com/api/external/v2)
- `LOG_LEVEL`: Logging level (default: INFO, options: DEBUG, WARNING, ERROR)

### Ports

- `8000`: HTTP server port (configurable in docker-compose.yml)

## 🛠️ Troubleshooting

### Container keeps restarting

```bash
# Check logs for errors
docker-compose logs --tail 50 pennylane-mcp

# Rebuild the image
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Module import errors

If you see `ModuleNotFoundError: No module named 'src'`:
```bash
# Rebuild with the latest Dockerfile
docker-compose build --no-cache
docker-compose up -d
```

### API key not recognized

Ensure your API key is properly set:
```bash
# Check if the environment variable is set
echo $PENNYLANE_API_KEY

# Or check the .env file
cat .env
```

## 🏭 Production Deployment

For production, consider:

1. **Using a reverse proxy** (nginx) for SSL/TLS
2. **Setting resource limits** in docker-compose.yml
3. **Configuring logging** to external systems
4. **Adding monitoring** with health checks

See the full [HTTP Transport Guide](documentation/HTTP_TRANSPORT_GUIDE.md) for detailed production setup.

## 📚 More Information

- [HTTP Transport Guide](documentation/HTTP_TRANSPORT_GUIDE.md)
- [Main README](README.md)
- [API Documentation](documentation/API_REFERENCE.md) 