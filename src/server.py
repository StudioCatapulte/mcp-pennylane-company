"""Main FastMCP server for Pennylane integration."""

import argparse
import logging
from typing import Optional

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

# Optional health check endpoint for HTTP deployments
@mcp.custom_route("/health", methods=["GET"])
async def health_check(request):
    """Health check endpoint for HTTP deployments."""
    from starlette.responses import JSONResponse
    return JSONResponse({
        "status": "healthy",
        "server": settings.mcp_server_name,
        "version": settings.mcp_server_version,
    })

# Import all components after server is created - this registers everything
from src.tools import *
from src.resources import *
from src.prompts import *

def parse_arguments():
    """Parse command line arguments for server configuration."""
    parser = argparse.ArgumentParser(
        description=f"{settings.mcp_server_name} - MCP server for Pennylane accounting"
    )
    
    # Transport selection
    parser.add_argument(
        "--transport",
        choices=["stdio", "streamable-http", "sse"],
        default="stdio",
        help="Transport protocol to use (default: stdio)"
    )
    
    # HTTP-specific options
    parser.add_argument(
        "--host",
        default="127.0.0.1",
        help="Host to bind to for HTTP transports (default: 127.0.0.1)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port to bind to for HTTP transports (default: 8000)"
    )
    
    parser.add_argument(
        "--path",
        default="/mcp",
        help="URL path for streamable-http transport (default: /mcp)"
    )
    
    parser.add_argument(
        "--sse-path",
        default="/sse",
        help="URL path for SSE transport (default: /sse)"
    )
    
    parser.add_argument(
        "--log-level",
        choices=["debug", "info", "warning", "error", "critical"],
        default=None,
        help="Override log level from settings"
    )
    
    return parser.parse_args()

def run_server(args: Optional[argparse.Namespace] = None):
    """Run the MCP server with the specified configuration."""
    if args is None:
        args = parse_arguments()
    
    # Override log level if specified
    if args.log_level:
        logging.getLogger().setLevel(getattr(logging, args.log_level.upper()))
    
    # Prepare kwargs for run() based on transport
    run_kwargs = {"transport": args.transport}
    
    if args.transport in ["streamable-http", "sse"]:
        run_kwargs.update({
            "host": args.host,
            "port": args.port,
        })
        
        if args.transport == "streamable-http":
            run_kwargs["path"] = args.path
            logger.info(
                f"Starting {settings.mcp_server_name} in Streamable HTTP mode "
                f"at http://{args.host}:{args.port}{args.path}"
            )
            logger.info(f"Health check available at http://{args.host}:{args.port}/health")
        else:  # sse
            run_kwargs["path"] = args.sse_path
            logger.info(
                f"Starting {settings.mcp_server_name} in SSE mode "
                f"at http://{args.host}:{args.port}{args.sse_path}"
            )
    else:  # stdio
        logger.info(f"Starting {settings.mcp_server_name} in STDIO mode")
    
    # Run the server
    mcp.run(**run_kwargs)

if __name__ == "__main__":
    run_server() 