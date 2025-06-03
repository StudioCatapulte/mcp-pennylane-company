"""API client for Pennylane API."""

import asyncio
from typing import Any, Dict, Optional
from urllib.parse import urljoin

import httpx
from pydantic import BaseModel

from src.config import settings


class PennylaneAPIError(Exception):
    """Base exception for Pennylane API errors."""

    def __init__(self, message: str, status_code: Optional[int] = None, response: Optional[dict] = None):
        super().__init__(message)
        self.status_code = status_code
        self.response = response


class PennylaneAPIClient:
    """Async HTTP client for Pennylane API."""

    def __init__(self):
        """Initialize the API client."""
        self.base_url = settings.pennylane_base_url
        self._client: Optional[httpx.AsyncClient] = None
        
    @property
    def headers(self) -> dict:
        """Get request headers with authentication."""
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        
        if settings.pennylane_api_key and not settings.use_oauth:
            headers["Authorization"] = f"Bearer {settings.pennylane_api_key}"
        
        return headers
    
    async def _get_client(self) -> httpx.AsyncClient:
        """Get or create the HTTP client."""
        if self._client is None or self._client.is_closed:
            self._client = httpx.AsyncClient(
                base_url=self.base_url,
                headers=self.headers,
                timeout=httpx.Timeout(settings.api_timeout),
            )
        return self._client
    
    async def _handle_response(self, response: httpx.Response) -> dict:
        """Handle API response and errors."""
        try:
            response_data = response.json() if response.content else {}
        except Exception:
            response_data = {}
        
        if response.status_code >= 400:
            error_message = response_data.get("error", f"API error: {response.status_code}")
            raise PennylaneAPIError(
                message=error_message,
                status_code=response.status_code,
                response=response_data
            )
        
        return response_data
    
    async def _request(
        self,
        method: str,
        endpoint: str,
        params: Optional[dict] = None,
        json_data: Optional[dict] = None,
        files: Optional[dict] = None,
        **kwargs
    ) -> dict:
        """Make an API request with retries."""
        client = await self._get_client()
        url = endpoint if endpoint.startswith("http") else f"/{endpoint.lstrip('/')}"
        
        for attempt in range(settings.api_max_retries):
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json_data,
                    files=files,
                    **kwargs
                )
                return await self._handle_response(response)
            
            except httpx.TimeoutException:
                if attempt == settings.api_max_retries - 1:
                    raise PennylaneAPIError("Request timeout")
                await asyncio.sleep(2 ** attempt)
            
            except httpx.RequestError as e:
                if attempt == settings.api_max_retries - 1:
                    raise PennylaneAPIError(f"Request error: {str(e)}")
                await asyncio.sleep(2 ** attempt)
    
    async def get(self, endpoint: str, params: Optional[dict] = None, **kwargs) -> dict:
        """Make a GET request."""
        return await self._request("GET", endpoint, params=params, **kwargs)
    
    async def post(self, endpoint: str, json_data: Optional[dict] = None, files: Optional[dict] = None, **kwargs) -> dict:
        """Make a POST request."""
        return await self._request("POST", endpoint, json_data=json_data, files=files, **kwargs)
    
    async def put(self, endpoint: str, json_data: Optional[dict] = None, **kwargs) -> dict:
        """Make a PUT request."""
        return await self._request("PUT", endpoint, json_data=json_data, **kwargs)
    
    async def delete(self, endpoint: str, **kwargs) -> dict:
        """Make a DELETE request."""
        return await self._request("DELETE", endpoint, **kwargs)
    
    async def close(self):
        """Close the HTTP client."""
        if self._client:
            await self._client.aclose()
    
    async def __aenter__(self):
        """Async context manager entry."""
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()


# Global client instance
api_client = PennylaneAPIClient() 