"""Shared MCP server instance to avoid circular imports."""

from contextlib import asynccontextmanager
import logging

from fastmcp import FastMCP

from src.config import settings

logger = logging.getLogger(__name__)


# Lifespan context manager for initialization and cleanup
@asynccontextmanager
async def lifespan(mcp: FastMCP):
    """Manage server lifecycle."""
    from src.utils.api_client import api_client
    
    logger.info(f"Starting {settings.mcp_server_name} v{settings.mcp_server_version}")
    
    # Test API connection
    try:
        # Test with the /me endpoint
        result = await api_client.get("me")
        logger.info(f"Connected to Pennylane API as: {result.get('email', 'Unknown')}")
    except Exception as e:
        logger.warning(f"Could not verify API connection: {e}")
    
    yield
    
    # Cleanup
    await api_client.close()
    logger.info("Server shutdown complete")


# Create FastMCP server instance with lifespan
mcp = FastMCP(
    name=settings.mcp_server_name,
    version=settings.mcp_server_version,
    lifespan=lifespan,
) 