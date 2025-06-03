"""MCP tools for managing Pennylane suppliers."""

from typing import Any, Dict, List, Optional
from pydantic import Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# Tool: List suppliers
@mcp.tool()
async def pennylane_suppliers_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string"),
    sort: str = Field("-id", description="Sort field, prefix with - for descending")
) -> Dict[str, Any]:
    """List all suppliers from Pennylane.
    
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
        
        response = await api_client.get("suppliers", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get supplier details
@mcp.tool()
async def pennylane_suppliers_get(
    supplier_id: int = Field(..., description="Supplier ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific supplier."""
    try:
        response = await api_client.get(f"suppliers/{supplier_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create supplier
@mcp.tool()
async def pennylane_suppliers_create(
    name: str = Field(..., description="Supplier name"),
    reg_no: Optional[str] = Field(None, description="Registration number (SIRET/SIREN)"),
    vat_number: Optional[str] = Field(None, description="VAT number"),
    iban: Optional[str] = Field(None, description="IBAN for payments"),
    reference: Optional[str] = Field(None, description="Supplier reference"),
    notes: Optional[str] = Field(None, description="Additional notes"),
    emails: Optional[List[str]] = Field(None, description="List of email addresses"),
    address: Optional[Dict[str, str]] = Field(None, description="Address with fields: street, postal_code, city, country"),
    external_reference: Optional[str] = Field(None, description="External reference for tracking")
) -> Dict[str, Any]:
    """Create a new supplier in Pennylane."""
    try:
        # Build request data
        data = {"name": name}
        
        # Add optional fields if provided
        optional_fields = {
            "reg_no": reg_no,
            "vat_number": vat_number,
            "iban": iban,
            "reference": reference,
            "notes": notes,
            "emails": emails,
            "address": address,
            "external_reference": external_reference,
        }
        
        for field, value in optional_fields.items():
            if value is not None:
                data[field] = value
        
        response = await api_client.post("suppliers", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Update supplier
@mcp.tool()
async def pennylane_suppliers_update(
    supplier_id: int = Field(..., description="Supplier ID"),
    name: Optional[str] = Field(None, description="Supplier name"),
    reg_no: Optional[str] = Field(None, description="Registration number"),
    vat_number: Optional[str] = Field(None, description="VAT number"),
    iban: Optional[str] = Field(None, description="IBAN for payments"),
    reference: Optional[str] = Field(None, description="Supplier reference"),
    notes: Optional[str] = Field(None, description="Additional notes"),
    emails: Optional[List[str]] = Field(None, description="List of email addresses"),
    address: Optional[Dict[str, str]] = Field(None, description="Address"),
    external_reference: Optional[str] = Field(None, description="External reference")
) -> Dict[str, Any]:
    """Update an existing supplier in Pennylane."""
    try:
        # Build update data with only provided fields
        data = {}
        fields = {
            "name": name,
            "reg_no": reg_no,
            "vat_number": vat_number,
            "iban": iban,
            "reference": reference,
            "notes": notes,
            "emails": emails,
            "address": address,
            "external_reference": external_reference,
        }
        
        for field, value in fields.items():
            if value is not None:
                data[field] = value
        
        if not data:
            return {"error": "No fields to update"}
        
        response = await api_client.put(f"suppliers/{supplier_id}", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: List supplier invoices
@mcp.tool()
async def pennylane_supplier_invoices_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string (e.g., 'supplier_id eq 123', 'status eq paid')"),
    sort: str = Field("-date", description="Sort field, prefix with - for descending")
) -> Dict[str, Any]:
    """List supplier invoices from Pennylane.
    
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
        
        response = await api_client.get("supplier_invoices", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get supplier invoice details
@mcp.tool()
async def pennylane_supplier_invoices_get(
    invoice_id: int = Field(..., description="Supplier invoice ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific supplier invoice."""
    try:
        response = await api_client.get(f"supplier_invoices/{invoice_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Update supplier invoice
@mcp.tool()
async def pennylane_supplier_invoices_update(
    invoice_id: int = Field(..., description="Supplier invoice ID"),
    supplier_id: Optional[int] = Field(None, description="Supplier ID"),
    date: Optional[str] = Field(None, description="Invoice date (ISO 8601)"),
    deadline: Optional[str] = Field(None, description="Payment deadline (ISO 8601)"),
    invoice_number: Optional[str] = Field(None, description="Invoice number"),
    amount: Optional[float] = Field(None, description="Total amount including tax"),
    amount_before_tax: Optional[float] = Field(None, description="Amount before tax"),
    currency: Optional[str] = Field(None, description="Currency code"),
    label: Optional[str] = Field(None, description="Invoice description"),
    external_reference: Optional[str] = Field(None, description="External reference")
) -> Dict[str, Any]:
    """Update a supplier invoice."""
    try:
        # Build update data with only provided fields
        data = {}
        
        if supplier_id is not None:
            data["supplier_id"] = supplier_id
        if date is not None:
            data["date"] = date
        if deadline is not None:
            data["deadline"] = deadline
        if invoice_number is not None:
            data["invoice_number"] = invoice_number
        if amount is not None:
            data["amount"] = str(amount)
        if amount_before_tax is not None:
            data["amount_before_tax"] = str(amount_before_tax)
        if currency is not None:
            data["currency"] = currency
        if label is not None:
            data["label"] = label
        if external_reference is not None:
            data["external_reference"] = external_reference
        
        if not data:
            return {"error": "No fields to update"}
        
        response = await api_client.put(f"supplier_invoices/{invoice_id}", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Import supplier invoice with file
@mcp.tool()
async def pennylane_supplier_invoices_import(
    file_path: str = Field(..., description="Path to the invoice file (PDF, image, etc.)"),
    supplier_id: Optional[int] = Field(None, description="Supplier ID to associate with invoice"),
    date: Optional[str] = Field(None, description="Invoice date (ISO 8601)"),
    amount: Optional[float] = Field(None, description="Invoice amount including tax"),
    invoice_number: Optional[str] = Field(None, description="Invoice number"),
    external_reference: Optional[str] = Field(None, description="External reference for tracking")
) -> Dict[str, Any]:
    """Import a supplier invoice from a file (PDF, image, etc.)."""
    try:
        # Read file
        with open(file_path, 'rb') as f:
            files = {'file': (file_path.split('/')[-1], f, 'application/octet-stream')}
            
            data = {}
            if supplier_id:
                data["supplier_id"] = str(supplier_id)
            if date:
                data["date"] = date
            if amount is not None:
                data["amount"] = str(amount)
            if invoice_number:
                data["invoice_number"] = invoice_number
            if external_reference:
                data["external_reference"] = external_reference
            
            response = await api_client.post("supplier_invoices/import", files=files, data=data)
            return response
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Error importing invoice: {str(e)}"}


# Tool: Update supplier invoice payment status
@mcp.tool()
async def pennylane_supplier_invoices_update_payment_status(
    invoice_id: int = Field(..., description="Supplier invoice ID"),
    paid: bool = Field(..., description="Payment status (true for paid, false for unpaid)"),
    payment_date: Optional[str] = Field(None, description="Payment date (ISO 8601, required if paid=true)")
) -> Dict[str, Any]:
    """Update the payment status of a supplier invoice."""
    try:
        data = {"paid": paid}
        if paid and payment_date:
            data["payment_date"] = payment_date
        
        response = await api_client.put(f"supplier_invoices/{invoice_id}/payment_status", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        } 