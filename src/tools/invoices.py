"""MCP tools for managing Pennylane customer invoices."""

import json
from typing import Any, Dict, List, Optional
from datetime import date
from pydantic import Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# Tool: List invoices
@mcp.tool()
async def pennylane_invoices_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of invoices to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter by status, date, customer, or amount (e.g., 'status eq draft', 'date gt 2024-01-01', 'customer_id eq 123')"),
    sort: str = Field("-date", description="Sort order: '-date' (newest first), 'date' (oldest first), '-amount' (highest amount first)")
) -> Dict[str, Any]:
    """List customer invoices from Pennylane.
    
    Returns paginated list of customer invoices with status, amounts, and payment information.
    Essential for invoice management, tracking payments, and financial reporting.
    
    Available filters:
    - status: draft, paid, late, upcoming, etc.
    - date: Invoice date comparisons (gt, lt, eq with YYYY-MM-DD format)
    - customer_id: Filter by specific customer
    - amount: Invoice amount comparisons
    
    Args:
        cursor: Pagination cursor for retrieving next page of results
        limit: Number of invoices to return per page (max 100)
        filter: Filter expression to narrow results
        sort: Sort order for the invoice list
    
    Example: Use 'status eq late' to find overdue invoices,
    or 'date gt 2024-01-01 and status eq draft' for recent draft invoices.
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
        
        response = await api_client.get("customer_invoices", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get invoice details
@mcp.tool()
async def pennylane_invoices_get(
    invoice_id: int = Field(..., description="Invoice ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific customer invoice."""
    try:
        response = await api_client.get(f"customer_invoices/{invoice_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create invoice
@mcp.tool()
async def pennylane_invoices_create(
    customer_id: int = Field(..., description="Customer ID who will receive this invoice"),
    invoice_lines: List[Dict[str, Any]] = Field(..., description="Invoice line items with product_id, quantity, label, unit_price, vat_rate"),
    draft: bool = Field(True, description="Create as draft (true) for editing, or finalized (false) for immediate sending"),
    date: Optional[str] = Field(None, description="Invoice date in YYYY-MM-DD format (defaults to today)"),
    deadline: Optional[str] = Field(None, description="Payment due date in YYYY-MM-DD format (auto-calculated from payment terms if not provided)"),
    currency: str = Field("EUR", description="Invoice currency code (EUR, USD, GBP, etc.)"),
    language: str = Field("fr_FR", description="Invoice language: fr_FR (French) or en_GB (English)"),
    label: Optional[str] = Field(None, description="Invoice description or subject line (e.g., 'Services for January 2024')"),
    external_reference: Optional[str] = Field(None, description="Your internal reference, order number, or project code"),
    discount_type: Optional[str] = Field(None, description="Discount type: 'absolute' (fixed amount) or 'relative' (percentage)"),
    discount_value: Optional[float] = Field(None, description="Discount amount (in currency units) or percentage (0-100)"),
    pdf_invoice_subject: Optional[str] = Field(None, description="Email subject when sending the invoice"),
    pdf_invoice_free_text: Optional[str] = Field(None, description="Additional text to include in the PDF invoice"),
    special_mention: Optional[str] = Field(None, description="Special legal mentions or notes on the invoice"),
    customer_invoice_template_id: Optional[int] = Field(None, description="Customer invoice template ID (use default template if not provided)")
) -> Dict[str, Any]:
    """Create a new customer invoice in Pennylane.
    
    Creates a customer invoice for goods or services delivered. Can be created as draft
    for review and editing, or finalized for immediate sending and payment processing.
    
    Invoice lines structure:
    Each line should contain:
    - product_id: ID of existing product (optional if all other fields provided)
    - quantity: Number of units (required)
    - label: Line description (required)  
    - raw_currency_unit_price: Price per unit excluding VAT as string (required if no product_id)
    - unit: Unit of measurement (required, e.g., 'hour', 'piece', 'day')
    - vat_rate: VAT rate code (required, e.g., 'FR_200' for 20%)
    - discount_type: 'absolute' or 'relative' (optional)
    - discount_value: Discount amount or percentage (optional)
    
    Args:
        customer_id: Target customer for this invoice
        invoice_lines: Array of products/services being invoiced
        draft: Whether to create as editable draft (true) or final invoice (false)
        date: Invoice issue date (defaults to today)
        deadline: Payment due date (calculated from customer terms if not specified)
        currency: Currency for amounts and display
        language: Language for invoice PDF and emails
        label: Overall invoice description
        external_reference: Link to your internal systems (PO number, project code)
        discount_type/value: Apply invoice-level discount
        pdf_invoice_subject: Subject line for invoice emails
        pdf_invoice_free_text: Additional content for invoice PDF
        special_mention: Legal or regulatory text
        customer_invoice_template_id: Customer invoice template ID (use default template if not provided)
        
    Example: Create a draft invoice using product ID 9566835 for 5 hours of consulting.
    Invoice line: {"product_id": 9566835, "quantity": 5, "label": "Consulting", "unit": "hour", "raw_currency_unit_price": "150.00", "vat_rate": "FR_200"}
    """
    try:
        # DEBUG: Test with minimal structure first
        if customer_id == 999999:  # Special test mode
            data = {
                "currency": currency,
                "language": language,
                "discount": {
                    "type": "relative",
                    "value": "0.0"
                },
                "draft": draft
            }
        else:
            # Build normal invoice data
            data = {
                "customer_id": customer_id,
                "draft": draft,
                "currency": currency,
                "language": language,
            }
            
            # Process invoice_lines to ensure correct structure
            processed_lines = []
            for line in invoice_lines:
                processed_line = {}
                
                # Ensure quantity is an integer
                if "quantity" in line:
                    processed_line["quantity"] = int(line["quantity"])
                
                # Copy other fields as strings
                if "label" in line:
                    processed_line["label"] = str(line["label"])
                if "raw_currency_unit_price" in line:
                    processed_line["raw_currency_unit_price"] = str(line["raw_currency_unit_price"])
                if "unit" in line:
                    processed_line["unit"] = str(line["unit"])
                if "vat_rate" in line:
                    processed_line["vat_rate"] = str(line["vat_rate"])
                
                # Optional fields
                if "product_id" in line:
                    processed_line["product_id"] = int(line["product_id"])
                
                processed_lines.append(processed_line)
            
            data["invoice_lines"] = processed_lines
            
            # Always add discount structure (seems required by API schema)
            if discount_type and discount_value is not None:
                data["discount"] = {
                    "type": discount_type,
                    "value": str(discount_value)
                }
            else:
                # Default discount to 0% relative
                data["discount"] = {
                    "type": "relative",
                    "value": "0.0"
                }
        
        # Add date and deadline - REQUIRED fields!
        if date:
            data["date"] = date
        else:
            # Default to today
            from datetime import date as date_module
            data["date"] = date_module.today().strftime("%Y-%m-%d")
            
        if deadline:
            data["deadline"] = deadline
        else:
            # Default to 30 days from date
            from datetime import datetime, timedelta
            invoice_date = datetime.strptime(data["date"], "%Y-%m-%d")
            data["deadline"] = (invoice_date + timedelta(days=30)).strftime("%Y-%m-%d")
        
        # Add optional fields if provided
        if label:
            data["label"] = label
        if pdf_invoice_subject:
            data["pdf_invoice_subject"] = pdf_invoice_subject
        if pdf_invoice_free_text:
            data["pdf_invoice_free_text"] = pdf_invoice_free_text
        if special_mention:
            data["special_mention"] = special_mention
        if external_reference:
            data["external_reference"] = external_reference
        
        # Add customer invoice template ID if provided
        if customer_invoice_template_id:
            data["customer_invoice_template_id"] = customer_invoice_template_id
        
        # DEBUG: Log the data structure being sent
        print(f"DEBUG: Sending invoice data: {data}")
        
        response = await api_client.post("customer_invoices", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Update draft invoice
@mcp.tool()
async def pennylane_invoices_update(
    invoice_id: int = Field(..., description="Invoice ID"),
    customer_id: Optional[int] = Field(None, description="Customer ID"),
    invoice_lines: Optional[List[Dict[str, Any]]] = Field(None, description="Updated invoice lines"),
    date: Optional[str] = Field(None, description="Invoice date (ISO 8601)"),
    deadline: Optional[str] = Field(None, description="Payment deadline (ISO 8601)"),
    label: Optional[str] = Field(None, description="Invoice label/description"),
    discount_type: Optional[str] = Field(None, description="Discount type: 'absolute' or 'relative'"),
    discount_value: Optional[float] = Field(None, description="Discount value"),
    pdf_invoice_subject: Optional[str] = Field(None, description="Email subject"),
    pdf_invoice_free_text: Optional[str] = Field(None, description="Free text for PDF"),
    special_mention: Optional[str] = Field(None, description="Special mention"),
    external_reference: Optional[str] = Field(None, description="External reference")
) -> Dict[str, Any]:
    """Update a draft customer invoice. Only draft invoices can be updated."""
    try:
        # Build update data with only provided fields
        data = {}
        
        if customer_id is not None:
            data["customer_id"] = customer_id
        if invoice_lines is not None:
            data["invoice_lines"] = invoice_lines
        if date is not None:
            data["date"] = date
        if deadline is not None:
            data["deadline"] = deadline
        if label is not None:
            data["label"] = label
        if discount_type and discount_value is not None:
            data["discount"] = {
                "type": discount_type,
                "value": str(discount_value)
            }
        if pdf_invoice_subject is not None:
            data["pdf_invoice_subject"] = pdf_invoice_subject
        if pdf_invoice_free_text is not None:
            data["pdf_invoice_free_text"] = pdf_invoice_free_text
        if special_mention is not None:
            data["special_mention"] = special_mention
        if external_reference is not None:
            data["external_reference"] = external_reference
        
        if not data:
            return {"error": "No fields to update"}
        
        response = await api_client.put(f"customer_invoices/{invoice_id}", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Finalize invoice
@mcp.tool()
async def pennylane_invoices_finalize(
    invoice_id: int = Field(..., description="Invoice ID"),
    invoice_number: Optional[str] = Field(None, description="Custom invoice number (auto-generated if not provided)")
) -> Dict[str, Any]:
    """Finalize a draft invoice. This action cannot be undone."""
    try:
        data = {}
        if invoice_number:
            data["invoice_number"] = invoice_number
        
        response = await api_client.put(f"customer_invoices/{invoice_id}/finalize", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Mark invoice as paid
@mcp.tool()
async def pennylane_invoices_mark_paid(
    invoice_id: int = Field(..., description="Invoice ID"),
    payment_date: Optional[str] = Field(None, description="Payment date (ISO 8601, defaults to today)")
) -> Dict[str, Any]:
    """Mark a finalized invoice as paid."""
    try:
        data = {}
        if payment_date:
            data["payment_date"] = payment_date
        
        response = await api_client.put(f"customer_invoices/{invoice_id}/mark_as_paid", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Send invoice by email
@mcp.tool()
async def pennylane_invoices_send_email(
    invoice_id: int = Field(..., description="Invoice ID"),
    emails: List[str] = Field(..., description="List of recipient email addresses (if empty, sends to customer's default emails)"),
    subject: Optional[str] = Field(None, description="Email subject (ignored by API - uses default)"),
    message: Optional[str] = Field(None, description="Email message body (ignored by API - uses default)"),
    copy_user: bool = Field(True, description="Send a copy to the current user (ignored by API)")
) -> Dict[str, Any]:
    """Send a customer invoice by email.
    
    Note: The API only supports specifying recipient emails. Subject, message, and copy_user
    are ignored by the API which uses its own defaults.
    """
    try:
        # API only accepts 'recipients' field
        data = {
            "recipients": emails
        }
        
        response = await api_client.post(f"customer_invoices/{invoice_id}/send_by_email", json_data=data)
        
        # API returns 204 No Content on success
        if response == {} or response is None:
            return {
                "success": True,
                "message": f"Invoice {invoice_id} is being sent by email to {', '.join(emails) if emails else 'customer default emails'}"
            }
        
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Delete draft invoice
@mcp.tool()
async def pennylane_invoices_delete(
    invoice_id: int = Field(..., description="Invoice ID")
) -> Dict[str, Any]:
    """Delete a draft invoice. Only draft invoices can be deleted."""
    try:
        response = await api_client.delete(f"customer_invoices/{invoice_id}")
        return {"success": True, "message": f"Invoice {invoice_id} deleted successfully"}
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get invoice templates
@mcp.tool()
async def pennylane_invoices_templates_list() -> Dict[str, Any]:
    """List available customer invoice templates."""
    try:
        response = await api_client.get("customer_invoice_templates")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Import invoice with file
@mcp.tool()
async def pennylane_invoices_import(
    file_path: str = Field(..., description="Path to the invoice file (PDF, image, etc.)"),
    customer_id: Optional[int] = Field(None, description="Customer ID to associate with invoice"),
    date: Optional[str] = Field(None, description="Invoice date (ISO 8601)"),
    amount: Optional[float] = Field(None, description="Invoice amount including tax"),
    external_reference: Optional[str] = Field(None, description="External reference for tracking")
) -> Dict[str, Any]:
    """Import an invoice from a file (PDF, image, etc.)."""
    try:
        # Read file
        with open(file_path, 'rb') as f:
            files = {'file': (file_path.split('/')[-1], f, 'application/octet-stream')}
            
            data = {}
            if customer_id:
                data["customer_id"] = str(customer_id)
            if date:
                data["date"] = date
            if amount is not None:
                data["amount"] = str(amount)
            if external_reference:
                data["external_reference"] = external_reference
            
            response = await api_client.post("customer_invoices/import", files=files, data=data)
            return response
    except FileNotFoundError:
        return {"error": f"File not found: {file_path}"}
    except Exception as e:
        return {"error": f"Error importing invoice: {str(e)}"} 