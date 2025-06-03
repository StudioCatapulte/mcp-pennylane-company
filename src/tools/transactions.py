"""MCP tools for managing Pennylane bank transactions."""

from typing import Any, Dict, List, Optional
from pydantic import Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# === BANK ACCOUNTS ===

# Tool: List bank accounts
@mcp.tool()
async def pennylane_bank_accounts_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)")
) -> Dict[str, Any]:
    """List all bank accounts from Pennylane."""
    try:
        params = {"limit": limit}
        if cursor:
            params["cursor"] = cursor
        
        response = await api_client.get("bank_accounts", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get bank account details
@mcp.tool()
async def pennylane_bank_accounts_get(
    account_id: int = Field(..., description="Bank account ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific bank account."""
    try:
        response = await api_client.get(f"bank_accounts/{account_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === TRANSACTIONS ===

# Tool: List transactions
@mcp.tool()
async def pennylane_transactions_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string (e.g., 'date gt 2024-01-01', 'bank_account_id eq 123', 'amount gt 100')"),
    sort: str = Field("-date", description="Sort field, prefix with - for descending")
) -> Dict[str, Any]:
    """List bank transactions from Pennylane.
    
    Available filters:
    - date: Transaction date comparisons
    - bank_account_id: Filter by bank account
    - amount: Amount comparisons
    - matched: true/false for matched/unmatched transactions
    
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
        
        response = await api_client.get("transactions", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get transaction details
@mcp.tool()
async def pennylane_transactions_get(
    transaction_id: int = Field(..., description="Transaction ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific transaction."""
    try:
        response = await api_client.get(f"transactions/{transaction_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get transaction categories
@mcp.tool()
async def pennylane_transactions_get_categories(
    transaction_id: int = Field(..., description="Transaction ID")
) -> Dict[str, Any]:
    """Get analytical categories assigned to a transaction."""
    try:
        response = await api_client.get(f"transactions/{transaction_id}/categories")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get invoices matched to transaction
@mcp.tool()
async def pennylane_transactions_get_matched_invoices(
    transaction_id: int = Field(..., description="Transaction ID")
) -> Dict[str, Any]:
    """Get invoices that are matched to a specific transaction."""
    try:
        response = await api_client.get(f"transactions/{transaction_id}/matched_invoices")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === TRANSACTION MATCHING ===

# Tool: Match transaction to customer invoice
@mcp.tool()
async def pennylane_transactions_match_customer_invoice(
    invoice_id: int = Field(..., description="Customer invoice ID"),
    transaction_id: int = Field(..., description="Transaction ID to match")
) -> Dict[str, Any]:
    """Match a bank transaction to a customer invoice for payment reconciliation."""
    try:
        data = {"transaction_id": transaction_id}
        
        response = await api_client.post(f"customer_invoices/{invoice_id}/matched_transactions", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Unmatch transaction from customer invoice
@mcp.tool()
async def pennylane_transactions_unmatch_customer_invoice(
    invoice_id: int = Field(..., description="Customer invoice ID"),
    transaction_id: int = Field(..., description="Transaction ID to unmatch")
) -> Dict[str, Any]:
    """Remove the match between a transaction and a customer invoice."""
    try:
        response = await api_client.delete(f"customer_invoices/{invoice_id}/matched_transactions/{transaction_id}")
        return {"success": True, "message": f"Transaction {transaction_id} unmatched from invoice {invoice_id}"}
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Match transaction to supplier invoice
@mcp.tool()
async def pennylane_transactions_match_supplier_invoice(
    invoice_id: int = Field(..., description="Supplier invoice ID"),
    transaction_id: int = Field(..., description="Transaction ID to match")
) -> Dict[str, Any]:
    """Match a bank transaction to a supplier invoice for payment reconciliation."""
    try:
        data = {"transaction_id": transaction_id}
        
        response = await api_client.post(f"supplier_invoices/{invoice_id}/matched_transactions", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Unmatch transaction from supplier invoice
@mcp.tool()
async def pennylane_transactions_unmatch_supplier_invoice(
    invoice_id: int = Field(..., description="Supplier invoice ID"),
    transaction_id: int = Field(..., description="Transaction ID to unmatch")
) -> Dict[str, Any]:
    """Remove the match between a transaction and a supplier invoice."""
    try:
        response = await api_client.delete(f"supplier_invoices/{invoice_id}/matched_transactions/{transaction_id}")
        return {"success": True, "message": f"Transaction {transaction_id} unmatched from invoice {invoice_id}"}
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        } 