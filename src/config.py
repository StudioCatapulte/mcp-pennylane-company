"""Configuration for MCP Pennylane server."""

import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic import Field, field_validator
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings."""

    # API Configuration
    api_key: str = Field(
        default="",
        description="Pennylane API key for authentication"
    )
    base_url: str = Field(
        default="https://app.pennylane.com/api/external/v2",
        description="Base URL for Pennylane API"
    )
    
    # OAuth Configuration (for partners)
    oauth_client_id: str = Field(
        default="",
        description="OAuth client ID for partner authentication"
    )
    oauth_client_secret: str = Field(
        default="",
        description="OAuth client secret for partner authentication"
    )
    
    # API Settings
    api_timeout: int = Field(
        default=30,
        description="API request timeout in seconds"
    )
    api_max_retries: int = Field(
        default=3,
        description="Maximum number of API request retries"
    )
    
    # MCP Server Settings
    mcp_server_name: str = Field(
        default="Pennylane MCP",
        description="Name of the MCP server"
    )
    mcp_server_version: str = Field(
        default="0.1.0",
        description="Version of the MCP server"
    )
    
    # Logging
    log_level: str = Field(
        default="INFO",
        description="Logging level"
    )
    
    class Config:
        env_prefix = "PENNYLANE_"
        env_file = ".env"
        env_file_encoding = "utf-8"
    
    @field_validator("api_key")
    def validate_api_key(cls, v: str) -> str:
        """Validate that API key is provided."""
        if not v and not os.getenv("PENNYLANE_OAUTH_CLIENT_ID"):
            raise ValueError(
                "Either PENNYLANE_API_KEY or PENNYLANE_OAUTH_CLIENT_ID must be provided"
            )
        return v
    
    @property
    def use_oauth(self) -> bool:
        """Check if OAuth authentication should be used."""
        return bool(self.oauth_client_id and self.oauth_client_secret)
    
    # Add property aliases for backward compatibility
    @property
    def pennylane_api_key(self) -> str:
        """Backward compatibility alias."""
        return self.api_key
    
    @property
    def pennylane_base_url(self) -> str:
        """Backward compatibility alias."""
        return self.base_url
    
    @property
    def pennylane_oauth_client_id(self) -> str:
        """Backward compatibility alias."""
        return self.oauth_client_id
    
    @property
    def pennylane_oauth_client_secret(self) -> str:
        """Backward compatibility alias."""
        return self.oauth_client_secret


# Global settings instance
settings = Settings() 