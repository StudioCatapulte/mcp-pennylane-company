"""MCP tools for managing Pennylane products."""

from typing import Any, Dict, Optional
from pydantic import Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# Tool: List products
@mcp.tool()
async def pennylane_products_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string"),
    sort: str = Field("-id", description="Sort field, prefix with - for descending")
) -> Dict[str, Any]:
    """List all products from Pennylane.
    
    Returns paginated results with cursor for next page.
    """
    try:
        params = {
            "limit": limit,
            "sort": sort,
        }
        if cursor:
            params["cursor"] = cursor
        if filter:
            params["filter"] = filter
        
        response = await api_client.get("products", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get product details
@mcp.tool()
async def pennylane_products_get(
    product_id: int = Field(..., description="Product ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific product."""
    try:
        response = await api_client.get(f"products/{product_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create product
@mcp.tool()
async def pennylane_products_create(
    label: str = Field(..., description="Product name"),
    price_before_tax: str = Field(..., description="Unit price excluding VAT (as string)"),
    vat_rate: str = Field("FR_200", description="VAT rate code (e.g., 'FR_200' for 20%, 'FR_100' for 10%)"),
    unit: str = Field("piece", description="Unit of measurement (e.g., 'piece', 'hour', 'day', 'kg', 'm')"),
    reference: Optional[str] = Field(None, description="Product reference code"),
    description: Optional[str] = Field(None, description="Product description"),
    external_reference: Optional[str] = Field(None, description="External reference for tracking"),
    currency: str = Field("EUR", description="Currency code (default: EUR)"),
    ledger_account_id: Optional[int] = Field(None, description="Ledger account ID")
) -> Dict[str, Any]:
    """Create a new product in Pennylane."""
    try:
        # Build request data
        data = {
            "label": label,
            "price_before_tax": price_before_tax,
            "vat_rate": vat_rate,
            "unit": unit,
            "currency": currency,
        }
        
        # Add optional fields if provided
        optional_fields = {
            "reference": reference,
            "description": description,
            "external_reference": external_reference,
            "ledger_account_id": ledger_account_id,
        }
        
        for field, value in optional_fields.items():
            if value is not None:
                data[field] = value
        
        response = await api_client.post("products", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Update product
@mcp.tool()
async def pennylane_products_update(
    product_id: int = Field(..., description="Product ID"),
    label: Optional[str] = Field(None, description="Product name"),
    price_before_tax: Optional[str] = Field(None, description="Unit price excluding VAT (as string)"),
    vat_rate: Optional[str] = Field(None, description="VAT rate code (e.g., 'FR_200' for 20%)"),
    unit: Optional[str] = Field(None, description="Unit of measurement"),
    reference: Optional[str] = Field(None, description="Product reference code"),
    description: Optional[str] = Field(None, description="Product description"),
    external_reference: Optional[str] = Field(None, description="External reference"),
    currency: Optional[str] = Field(None, description="Currency code"),
    ledger_account_id: Optional[int] = Field(None, description="Ledger account ID")
) -> Dict[str, Any]:
    """Update an existing product in Pennylane."""
    try:
        # Build update data with only provided fields
        data = {}
        
        if label is not None:
            data["label"] = label
        if price_before_tax is not None:
            data["price_before_tax"] = price_before_tax
        if vat_rate is not None:
            data["vat_rate"] = vat_rate
        if unit is not None:
            data["unit"] = unit
        if reference is not None:
            data["reference"] = reference
        if description is not None:
            data["description"] = description
        if external_reference is not None:
            data["external_reference"] = external_reference
        if currency is not None:
            data["currency"] = currency
        if ledger_account_id is not None:
            data["ledger_account_id"] = ledger_account_id
        
        if not data:
            return {"error": "No fields to update"}
        
        response = await api_client.put(f"products/{product_id}", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        } 