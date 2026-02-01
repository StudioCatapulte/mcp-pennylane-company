"""MCP tools for managing Pennylane file attachments."""

from typing import Any, Dict, Optional
from pydantic import Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# === FILE ATTACHMENTS ===

# Tool: Upload file attachment
@mcp.tool()
async def pennylane_files_upload(
    file_path: str = Field(..., description="Path to the file to upload"),
    description: Optional[str] = Field(None, description="File description")
) -> Dict[str, Any]:
    """Upload a file attachment to Pennylane."""
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path.split('/')[-1], f, 'application/octet-stream')}
            
            data = {}
            if description:
                data["description"] = description
            
            response = await api_client.post("file_attachments", files=files, data=data)
            return response
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Error uploading file: {str(e)}"}


# Tool: List file attachments
@mcp.tool()
async def pennylane_files_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string"),
    sort: str = Field("-created_at", description="Sort field")
) -> Dict[str, Any]:
    """List file attachments from Pennylane."""
    try:
        params = {
            "limit": limit,
            "sort": sort,
        }
        if cursor:
            params["cursor"] = cursor
        if filter:
            params["filter"] = filter
        
        response = await api_client.get("file_attachments", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === LEDGER ATTACHMENTS ===

# Tool: Upload ledger attachment
@mcp.tool()
async def pennylane_ledger_attachments_upload(
    file_path: str = Field(..., description="Path to the file to upload"),
    ledger_entry_id: Optional[int] = Field(None, description="Ledger entry ID to attach to"),
    description: Optional[str] = Field(None, description="File description")
) -> Dict[str, Any]:
    """Upload a file attachment for ledger entries."""
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path.split('/')[-1], f, 'application/octet-stream')}
            
            data = {}
            if ledger_entry_id:
                data["ledger_entry_id"] = str(ledger_entry_id)
            if description:
                data["description"] = description
            
            response = await api_client.post("ledger_attachments", files=files, data=data)
            return response
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Error uploading file: {str(e)}"}


# Tool: List ledger attachments
@mcp.tool()
async def pennylane_ledger_attachments_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string (e.g., 'ledger_entry_id eq 123')")
) -> Dict[str, Any]:
    """List ledger attachments from Pennylane."""
    try:
        params = {"limit": limit}
        if cursor:
            params["cursor"] = cursor
        if filter:
            params["filter"] = filter
        
        response = await api_client.get("ledger_attachments", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === INVOICE APPENDICES ===

# Tool: Upload customer invoice appendix
@mcp.tool()
async def pennylane_invoices_upload_appendix(
    invoice_id: int = Field(..., description="Customer invoice ID"),
    file_path: str = Field(..., description="Path to the file to upload"),
    description: Optional[str] = Field(None, description="File description")
) -> Dict[str, Any]:
    """Upload an appendix file to a customer invoice."""
    try:
        with open(file_path, 'rb') as f:
            files = {'file': (file_path.split('/')[-1], f, 'application/octet-stream')}
            
            data = {}
            if description:
                data["description"] = description
            
            response = await api_client.post(f"customer_invoices/{invoice_id}/appendices", files=files, data=data)
            return response
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Error uploading appendix: {str(e)}"}


# Tool: List customer invoice appendices
@mcp.tool()
async def pennylane_invoices_list_appendices(
    invoice_id: int = Field(..., description="Customer invoice ID")
) -> Dict[str, Any]:
    """List appendix files attached to a customer invoice."""
    try:
        response = await api_client.get(f"customer_invoices/{invoice_id}/appendices")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        } 