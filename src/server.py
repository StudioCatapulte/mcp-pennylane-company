"""Main FastMCP server for Pennylane integration."""

import logging

from src.config import settings
from src.mcp_instance import mcp

# Configure logging
logging.basicConfig(level=getattr(logging, settings.log_level))
logger = logging.getLogger(__name__)

# Server metadata tool
@mcp.tool()
async def pennylane_server_info() -> dict:
    """Get information about the Pennylane MCP server.
    
    Returns server version and configuration status.
    """
    return {
        "name": settings.mcp_server_name,
        "version": settings.mcp_server_version,
        "api_base_url": settings.pennylane_base_url,
        "authentication_method": "oauth" if settings.use_oauth else "api_key",
        "api_configured": bool(settings.pennylane_api_key or settings.use_oauth),
    }

# Import tools after server is created - this registers all tools
from src.tools import *

if __name__ == "__main__":
    # Run the server
    mcp.run(transport="stdio") 