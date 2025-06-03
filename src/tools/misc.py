"""MCP tools for Pennylane changelogs and user profile."""

from typing import Any, Dict, Optional
from pydantic import Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# === USER PROFILE ===

# Tool: Get user profile
@mcp.tool()
async def pennylane_user_profile() -> Dict[str, Any]:
    """Get the current user's profile information."""
    try:
        response = await api_client.get("me")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === CHANGELOGS ===

# Tool: Get customer invoices changes
@mcp.tool()
async def pennylane_changelog_customer_invoices(
    since: str = Field(..., description="ISO 8601 datetime to get changes since"),
    cursor: Optional[str] = None,
    limit: int = Field(100, ge=1, le=1000, description="Number of items to return (1-1000)")
) -> Dict[str, Any]:
    """Get changelog events for customer invoices since a specific date."""
    try:
        params = {
            "since": since,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        
        response = await api_client.get("customer_invoices/changes", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get supplier invoices changes
@mcp.tool()
async def pennylane_changelog_supplier_invoices(
    since: str = Field(..., description="ISO 8601 datetime to get changes since"),
    cursor: Optional[str] = None,
    limit: int = Field(100, ge=1, le=1000, description="Number of items to return (1-1000)")
) -> Dict[str, Any]:
    """Get changelog events for supplier invoices since a specific date."""
    try:
        params = {
            "since": since,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        
        response = await api_client.get("supplier_invoices/changes", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get customers changes
@mcp.tool()
async def pennylane_changelog_customers(
    since: str = Field(..., description="ISO 8601 datetime to get changes since"),
    cursor: Optional[str] = None,
    limit: int = Field(100, ge=1, le=1000, description="Number of items to return (1-1000)")
) -> Dict[str, Any]:
    """Get changelog events for customers since a specific date."""
    try:
        params = {
            "since": since,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        
        response = await api_client.get("customers/changes", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get suppliers changes
@mcp.tool()
async def pennylane_changelog_suppliers(
    since: str = Field(..., description="ISO 8601 datetime to get changes since"),
    cursor: Optional[str] = None,
    limit: int = Field(100, ge=1, le=1000, description="Number of items to return (1-1000)")
) -> Dict[str, Any]:
    """Get changelog events for suppliers since a specific date."""
    try:
        params = {
            "since": since,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        
        response = await api_client.get("suppliers/changes", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get products changes
@mcp.tool()
async def pennylane_changelog_products(
    since: str = Field(..., description="ISO 8601 datetime to get changes since"),
    cursor: Optional[str] = None,
    limit: int = Field(100, ge=1, le=1000, description="Number of items to return (1-1000)")
) -> Dict[str, Any]:
    """Get changelog events for products since a specific date."""
    try:
        params = {
            "since": since,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        
        response = await api_client.get("products/changes", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get ledger entry lines changes
@mcp.tool()
async def pennylane_changelog_ledger_entry_lines(
    since: str = Field(..., description="ISO 8601 datetime to get changes since"),
    cursor: Optional[str] = None,
    limit: int = Field(100, ge=1, le=1000, description="Number of items to return (1-1000)")
) -> Dict[str, Any]:
    """Get changelog events for ledger entry lines since a specific date."""
    try:
        params = {
            "since": since,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        
        response = await api_client.get("ledger_entry_lines/changes", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get transactions changes
@mcp.tool()
async def pennylane_changelog_transactions(
    since: str = Field(..., description="ISO 8601 datetime to get changes since"),
    cursor: Optional[str] = None,
    limit: int = Field(100, ge=1, le=1000, description="Number of items to return (1-1000)")
) -> Dict[str, Any]:
    """Get changelog events for bank transactions since a specific date."""
    try:
        params = {
            "since": since,
            "limit": limit,
        }
        if cursor:
            params["cursor"] = cursor
        
        response = await api_client.get("transactions/changes", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        } 