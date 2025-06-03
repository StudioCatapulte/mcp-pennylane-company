"""Basic tests for MCP Pennylane server."""

import pytest
from unittest.mock import patch, MagicMock


def test_server_import():
    """Test that the server module can be imported."""
    from src import server
    assert hasattr(server, 'mcp')
    assert hasattr(server, 'initialize')
    assert hasattr(server, 'cleanup')


def test_server_info_tool():
    """Test the server info tool."""
    from src.server import pennylane_server_info
    # This should work without API key
    import asyncio
    result = asyncio.run(pennylane_server_info())
    
    assert isinstance(result, dict)
    assert 'name' in result
    assert 'version' in result
    assert 'api_base_url' in result
    assert 'authentication_method' in result
    assert 'api_configured' in result


@patch('src.config.settings')
def test_config_loading(mock_settings):
    """Test that configuration is properly loaded."""
    mock_settings.pennylane_api_key = "test_key"
    mock_settings.pennylane_base_url = "https://test.api.url"
    mock_settings.use_oauth = False
    
    from src.config import settings
    # Settings should be accessible 