"""MCP tools for managing Pennylane analytical categories."""

from typing import Any, Dict, Optional
from pydantic import Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# === CATEGORY GROUPS ===

# Tool: List category groups
@mcp.tool()
async def pennylane_category_groups_list() -> Dict[str, Any]:
    """List all analytical category groups from Pennylane."""
    try:
        response = await api_client.get("category_groups")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get categories in a group
@mcp.tool()
async def pennylane_category_groups_get_categories(
    group_id: int = Field(..., description="Category group ID")
) -> Dict[str, Any]:
    """Get all categories within a specific category group."""
    try:
        response = await api_client.get(f"category_groups/{group_id}/categories")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === CATEGORIES ===

# Tool: List categories
@mcp.tool()
async def pennylane_categories_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string"),
    sort: str = Field("name", description="Sort field")
) -> Dict[str, Any]:
    """List all analytical categories from Pennylane."""
    try:
        params = {
            "limit": limit,
            "sort": sort,
        }
        if cursor:
            params["cursor"] = cursor
        if filter:
            params["filter"] = filter
        
        response = await api_client.get("categories", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get category details
@mcp.tool()
async def pennylane_categories_get(
    category_id: int = Field(..., description="Category ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific analytical category."""
    try:
        response = await api_client.get(f"categories/{category_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create category
@mcp.tool()
async def pennylane_categories_create(
    label: str = Field(..., description="Category name"),
    category_group_id: int = Field(..., description="Category group ID"),
    direction: Optional[str] = Field(None, description="Direction: 'cash_in' or 'cash_out'")
) -> Dict[str, Any]:
    """Create a new analytical category in Pennylane."""
    try:
        data = {
            "label": label,
            "category_group_id": category_group_id,
        }
        
        if direction:
            data["direction"] = direction
        
        response = await api_client.post("categories", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Update category
@mcp.tool()
async def pennylane_categories_update(
    category_id: int = Field(..., description="Category ID"),
    name: Optional[str] = Field(None, description="Category name"),
    code: Optional[str] = Field(None, description="Category code"),
    description: Optional[str] = Field(None, description="Category description"),
    active: Optional[bool] = Field(None, description="Whether the category is active")
) -> Dict[str, Any]:
    """Update an existing analytical category."""
    try:
        data = {}
        
        if name is not None:
            data["name"] = name
        if code is not None:
            data["code"] = code
        if description is not None:
            data["description"] = description
        if active is not None:
            data["active"] = active
        
        if not data:
            return {"error": "No fields to update"}
        
        response = await api_client.put(f"categories/{category_id}", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === CATEGORIZATION ===

# Tool: Categorize customer invoice
@mcp.tool()
async def pennylane_invoices_categorize(
    invoice_id: int = Field(..., description="Customer invoice ID"),
    category_ids: list[int] = Field(..., description="List of category IDs to assign")
) -> Dict[str, Any]:
    """Assign analytical categories to a customer invoice."""
    try:
        data = {"category_ids": category_ids}
        
        response = await api_client.put(f"customer_invoices/{invoice_id}/categories", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get customer invoice categories
@mcp.tool()
async def pennylane_invoices_get_categories(
    invoice_id: int = Field(..., description="Customer invoice ID")
) -> Dict[str, Any]:
    """Get analytical categories assigned to a customer invoice."""
    try:
        response = await api_client.get(f"customer_invoices/{invoice_id}/categories")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Categorize supplier invoice
@mcp.tool()
async def pennylane_supplier_invoices_categorize(
    invoice_id: int = Field(..., description="Supplier invoice ID"),
    category_ids: list[int] = Field(..., description="List of category IDs to assign")
) -> Dict[str, Any]:
    """Assign analytical categories to a supplier invoice."""
    try:
        data = {"category_ids": category_ids}
        
        response = await api_client.put(f"supplier_invoices/{invoice_id}/categories", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get supplier invoice categories
@mcp.tool()
async def pennylane_supplier_invoices_get_categories(
    invoice_id: int = Field(..., description="Supplier invoice ID")
) -> Dict[str, Any]:
    """Get analytical categories assigned to a supplier invoice."""
    try:
        response = await api_client.get(f"supplier_invoices/{invoice_id}/categories")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Link categories to ledger entry line
@mcp.tool()
async def pennylane_ledger_entry_lines_categorize(
    line_id: int = Field(..., description="Ledger entry line ID"),
    category_ids: list[int] = Field(..., description="List of category IDs to assign")
) -> Dict[str, Any]:
    """Link analytical categories to a ledger entry line."""
    try:
        data = {"category_ids": category_ids}
        
        response = await api_client.put(f"ledger_entry_lines/{line_id}/categories", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get ledger entry line categories
@mcp.tool()
async def pennylane_ledger_entry_lines_get_categories(
    line_id: int = Field(..., description="Ledger entry line ID")
) -> Dict[str, Any]:
    """Get analytical categories assigned to a ledger entry line."""
    try:
        response = await api_client.get(f"ledger_entry_lines/{line_id}/categories")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        } 