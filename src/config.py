"""Configuration for the Pennylane MCP server."""

import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings
from typing import Optional

# Load environment variables from .env file only if it exists
# This ensures Docker env vars take precedence
env_path = Path(".env")
if env_path.exists():
    load_dotenv(override=False)  # Don't override existing env vars


class Settings(BaseSettings):
    """Application settings."""

    # MCP Server Settings
    mcp_server_name: str = Field(
        default="Pennylane MCP",
        description="Name of the MCP server"
    )
    mcp_server_version: str = Field(
        default="0.2.0",
        description="Version of the MCP server"
    )
    
    # Pennylane API Settings
    pennylane_api_key: Optional[str] = Field(
        default=None,
        alias="PENNYLANE_API_KEY",  # Explicit environment variable name
        description="Pennylane API key for authentication"
    )
    pennylane_base_url: str = Field(
        default="https://app.pennylane.com/api/external/v2",
        alias="PENNYLANE_BASE_URL",
        description="Base URL for Pennylane API"
    )
    
    # OAuth Settings
    use_oauth: bool = Field(
        default=False,
        alias="PENNYLANE_USE_OAUTH",
        description="Whether to use OAuth authentication"
    )
    oauth_client_id: Optional[str] = Field(
        default=None,
        alias="PENNYLANE_OAUTH_CLIENT_ID",
        description="OAuth client ID for partner authentication"
    )
    oauth_client_secret: Optional[str] = Field(
        default=None,
        alias="PENNYLANE_OAUTH_CLIENT_SECRET",
        description="OAuth client secret for partner authentication"
    )
    oauth_redirect_uri: Optional[str] = Field(
        default=None,
        alias="PENNYLANE_OAUTH_REDIRECT_URI",
        description="OAuth redirect URI"
    )
    oauth_scope: str = Field(
        default="accounting customer_invoices suppliers",
        alias="PENNYLANE_OAUTH_SCOPE",
        description="OAuth scopes to request"
    )
    
    # Logging
    log_level: str = Field(
        default="INFO",
        alias="LOG_LEVEL",
        description="Logging level (DEBUG, INFO, WARNING, ERROR)"
    )
    
    # Request Settings
    request_timeout: int = Field(
        default=30,
        alias="PENNYLANE_REQUEST_TIMEOUT",
        description="API request timeout in seconds"
    )
    max_retries: int = Field(
        default=3,
        alias="PENNYLANE_MAX_RETRIES",
        description="Maximum number of API request retries"
    )
    
    class Config:
        # No prefix since we're using explicit aliases
        env_file = ".env"
        env_file_encoding = "utf-8"
        populate_by_name = True  # Allow both field name and alias
    
    @field_validator("pennylane_api_key")
    def validate_api_key(cls, v: Optional[str], info) -> Optional[str]:
        """Validate that either API key or OAuth credentials are provided."""
        # Get OAuth values from the current data being validated
        data = info.data if hasattr(info, 'data') else {}
        oauth_id = data.get("oauth_client_id")
        oauth_secret = data.get("oauth_client_secret")
        
        # Also check environment variables as fallback
        if not oauth_id:
            oauth_id = os.getenv("PENNYLANE_OAUTH_CLIENT_ID")
        if not oauth_secret:
            oauth_secret = os.getenv("PENNYLANE_OAUTH_CLIENT_SECRET")
        
        if not v and not (oauth_id and oauth_secret):
            raise ValueError(
                "Either PENNYLANE_API_KEY or both PENNYLANE_OAUTH_CLIENT_ID and PENNYLANE_OAUTH_CLIENT_SECRET must be provided"
            )
        return v
    
    def should_use_oauth(self) -> bool:
        """Check if OAuth authentication should be used."""
        return bool(self.oauth_client_id and self.oauth_client_secret)


# Global settings instance
settings = Settings() 