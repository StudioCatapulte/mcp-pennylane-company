"""MCP tools for managing Pennylane customers."""

from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# Pydantic models for request/response validation
class CustomerAddress(BaseModel):
    """Customer address model."""
    address: str
    postal_code: str
    city: str
    country: str = "FR"


class CompanyCustomerCreate(BaseModel):
    """Model for creating a company customer."""
    name: str = Field(..., description="Company name")
    billing_iban: Optional[str] = Field(None, description="IBAN for billing")
    payment_conditions: Optional[str] = Field("30_days", description="Payment conditions: upon_receipt, 15_days, 30_days, 45_days, 60_days, 90_days, custom_days")
    recipient: Optional[str] = Field(None, description="Recipient name")
    phone: Optional[str] = Field(None, description="Phone number")
    reference: Optional[str] = Field(None, description="Customer reference")
    notes: Optional[str] = Field(None, description="Additional notes")
    vat_number: Optional[str] = Field(None, description="VAT number")
    reg_no: Optional[str] = Field(None, description="Registration number")
    emails: Optional[List[str]] = Field(None, description="List of email addresses")
    billing_address: Optional[CustomerAddress] = Field(None, description="Billing address")
    external_reference: Optional[str] = Field(None, description="External reference for tracking")


class IndividualCustomerCreate(BaseModel):
    """Model for creating an individual customer."""
    first_name: str = Field(..., description="First name")
    last_name: str = Field(..., description="Last name")
    gender: Optional[str] = Field(None, description="Gender: Mr, Ms, Mx")
    billing_iban: Optional[str] = Field(None, description="IBAN for billing")
    payment_conditions: Optional[str] = Field("30_days", description="Payment conditions")
    phone: Optional[str] = Field(None, description="Phone number")
    reference: Optional[str] = Field(None, description="Customer reference")
    notes: Optional[str] = Field(None, description="Additional notes")
    emails: Optional[List[str]] = Field(None, description="List of email addresses")
    billing_address: Optional[CustomerAddress] = Field(None, description="Billing address")
    external_reference: Optional[str] = Field(None, description="External reference for tracking")


# Tool: List customers
@mcp.tool()
async def pennylane_customers_list(
    cursor: Optional[str] = None,
    limit: int = 20,
    filter: Optional[str] = None,
    sort: str = "-id"
) -> Dict[str, Any]:
    """List all customers (both company and individual) from Pennylane.
    
    Returns paginated list of customers with their basic information, contact details,
    and billing configuration. Essential for managing customer relationships and invoicing.
    
    Available filters:
    - id: lt, lteq, gt, gteq, eq, not_eq, in, not_in
    - customer_type: eq, not_eq  
    - ledger_account_id: eq, not_eq
    - name: start_with
    - external_reference: start_with, eq, not_eq, in, not_in
    - reg_no: eq, not_eq, in, not_in
    
    Args:
        cursor: Pagination cursor for retrieving next page of results
        limit: Number of customers to return per page
        filter: Filter expression (e.g., 'name start_with ABC' for companies starting with ABC)
        sort: Sort order ('-id' for newest first, 'name' for alphabetical)
    
    Example: Use filter 'customer_type eq company' to get only business customers,
    or 'name start_with Smith' to find customers with names starting with Smith.
    """
    try:
        # Validate limit
        if limit < 1:
            limit = 1
        elif limit > 100:
            limit = 100
            
        params = {
            "limit": limit,
            "sort": sort,
        }
        if cursor:
            params["cursor"] = cursor
        if filter:
            params["filter"] = filter
        
        response = await api_client.get("customers", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get customer details
@mcp.tool()
async def pennylane_customers_get(
    customer_id: int = Field(..., description="Customer ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific customer."""
    try:
        response = await api_client.get(f"customers/{customer_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create company customer
@mcp.tool()
async def pennylane_customers_create_company(
    name: str = Field(..., description="Company legal name (e.g., 'ABC Corporation Ltd', 'Smith & Associates')"),
    billing_address: Optional[Dict[str, str]] = Field(None, description="Billing address with fields: address, postal_code, city, country"),
    vat_number: Optional[str] = Field(None, description="Company VAT number (e.g., 'FR12345678901' for French companies)"),
    reg_no: Optional[str] = Field(None, description="Company registration number (SIRET for France, Company House number for UK)"),
    phone: Optional[str] = Field(None, description="Main company phone number in international format (e.g., '+33123456789')"),
    payment_conditions: Optional[str] = Field("30_days", description="Payment terms: upon_receipt, 15_days, 30_days, 45_days, 60_days, 90_days, custom_days"),
    billing_iban: Optional[str] = Field(None, description="Company bank account IBAN for direct debits"),
    recipient: Optional[str] = Field(None, description="Contact person name for invoices and correspondence"),
    reference: Optional[str] = Field(None, description="Internal customer reference code or number"),
    notes: Optional[str] = Field(None, description="Internal notes about the customer relationship"),
    emails: Optional[List[str]] = Field(None, description="List of email addresses for invoicing and communication"),
    external_reference: Optional[str] = Field(None, description="External system reference (CRM ID, ERP code, etc.)")
) -> Dict[str, Any]:
    """Create a new company customer in Pennylane.
    
    Creates a business customer entity for B2B transactions and invoicing.
    Company customers can have VAT numbers, registration numbers, and multiple contacts.
    
    Args:
        name: Official company name as it appears on legal documents
        billing_address: Company's billing address (required for invoicing)
        vat_number: EU VAT number for B2B transactions (enables reverse charge)
        reg_no: Official company registration (SIRET in France)
        phone: Primary contact number for the company
        payment_conditions: Default payment terms for invoices
        billing_iban: Bank account for direct debit payments
        recipient: Main contact person for invoices
        reference: Your internal customer code/reference
        notes: Any important information about the customer
        emails: Contact emails for sending invoices and communications
        external_reference: Link to external CRM/ERP systems
        
    Example: Create a French company with VAT number, 30-day payment terms,
    and billing contact for automated invoice processing.
    """
    try:
        # Build request data
        data = {
            "name": name,
        }
        
        # Add required billing_address with defaults if not provided
        if billing_address:
            data["billing_address"] = billing_address
        else:
            data["billing_address"] = {
                "address": "",
                "postal_code": "",
                "city": "",
                "country_alpha2": "FR"
            }
        
        # Add optional fields if provided
        optional_fields = {
            "vat_number": vat_number,
            "reg_no": reg_no,
            "phone": phone,
            "payment_conditions": payment_conditions,
            "billing_iban": billing_iban,
            "recipient": recipient,
            "reference": reference,
            "notes": notes,
            "emails": emails,
            "external_reference": external_reference,
        }
        
        for field, value in optional_fields.items():
            if value is not None:
                data[field] = value
        
        response = await api_client.post("company_customers", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create individual customer
@mcp.tool()
async def pennylane_customers_create_individual(
    first_name: str = Field(..., description="Customer's first name"),
    last_name: str = Field(..., description="Customer's last name"),
    billing_iban: Optional[str] = Field(None, description="Personal bank account IBAN for direct debits"),
    payment_conditions: Optional[str] = Field("30_days", description="Payment terms: upon_receipt, 15_days, 30_days, 45_days, 60_days, 90_days"),
    phone: Optional[str] = Field(None, description="Personal phone number in international format (e.g., '+33987654321')"),
    reference: Optional[str] = Field(None, description="Internal customer reference or account number"),
    notes: Optional[str] = Field(None, description="Internal notes about the customer"),
    emails: Optional[List[str]] = Field(None, description="Email addresses for invoicing and communication"),
    billing_address: Optional[Dict[str, str]] = Field(None, description="Personal billing address with fields: address, postal_code, city, country"),
    external_reference: Optional[str] = Field(None, description="External system reference (CRM ID, etc.)")
) -> Dict[str, Any]:
    """Create a new individual customer in Pennylane.
    
    Creates a personal customer entity for B2C transactions and invoicing.
    Individual customers are private persons rather than businesses.
    
    Args:
        first_name: Customer's given name
        last_name: Customer's family name
        billing_iban: Personal bank account for direct debit setup
        payment_conditions: Default payment terms for invoices to this customer
        phone: Personal contact number
        reference: Your internal customer identifier
        notes: Any relevant information about the customer
        emails: Contact emails for invoice delivery
        billing_address: Personal address for billing and correspondence
        external_reference: Link to external CRM or customer management system
        
    Example: Create an individual customer for freelance services with
    email invoicing and 15-day payment terms.
    """
    try:
        # Build request data
        data = {
            "first_name": first_name,
            "last_name": last_name,
        }
        
        # Add required billing_address with defaults if not provided
        if billing_address:
            data["billing_address"] = billing_address
        else:
            data["billing_address"] = {
                "address": "",
                "postal_code": "",
                "city": "",
                "country_alpha2": "FR"
            }
        
        # Add optional fields if provided
        optional_fields = {
            "billing_iban": billing_iban,
            "payment_conditions": payment_conditions,
            "phone": phone,
            "reference": reference,
            "notes": notes,
            "emails": emails,
            "external_reference": external_reference,
        }
        
        for field, value in optional_fields.items():
            if value is not None:
                data[field] = value
        
        response = await api_client.post("individual_customers", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Update company customer
@mcp.tool()
async def pennylane_customers_update_company(
    customer_id: int = Field(..., description="Customer ID"),
    name: Optional[str] = Field(None, description="Company name"),
    billing_iban: Optional[str] = Field(None, description="IBAN for billing"),
    payment_conditions: Optional[str] = Field(None, description="Payment conditions"),
    recipient: Optional[str] = Field(None, description="Recipient name"),
    phone: Optional[str] = Field(None, description="Phone number"),
    reference: Optional[str] = Field(None, description="Customer reference"),
    notes: Optional[str] = Field(None, description="Additional notes"),
    vat_number: Optional[str] = Field(None, description="VAT number"),
    reg_no: Optional[str] = Field(None, description="Registration number"),
    emails: Optional[List[str]] = Field(None, description="List of email addresses"),
    billing_address: Optional[Dict[str, str]] = Field(None, description="Billing address"),
    external_reference: Optional[str] = Field(None, description="External reference")
) -> Dict[str, Any]:
    """Update an existing company customer in Pennylane."""
    try:
        # Build update data with only provided fields
        data = {}
        fields = {
            "name": name,
            "billing_iban": billing_iban,
            "payment_conditions": payment_conditions,
            "recipient": recipient,
            "phone": phone,
            "reference": reference,
            "notes": notes,
            "vat_number": vat_number,
            "reg_no": reg_no,
            "emails": emails,
            "billing_address": billing_address,
            "external_reference": external_reference,
        }
        
        for field, value in fields.items():
            if value is not None:
                data[field] = value
        
        if not data:
            return {"error": "No fields to update"}
        
        response = await api_client.put(f"customers/company/{customer_id}", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Update individual customer
@mcp.tool()
async def pennylane_customers_update_individual(
    customer_id: int = Field(..., description="Customer ID"),
    first_name: Optional[str] = Field(None, description="First name"),
    last_name: Optional[str] = Field(None, description="Last name"),
    billing_iban: Optional[str] = Field(None, description="IBAN for billing"),
    payment_conditions: Optional[str] = Field(None, description="Payment conditions"),
    phone: Optional[str] = Field(None, description="Phone number"),
    reference: Optional[str] = Field(None, description="Customer reference"),
    notes: Optional[str] = Field(None, description="Additional notes"),
    emails: Optional[List[str]] = Field(None, description="List of email addresses"),
    billing_address: Optional[Dict[str, str]] = Field(None, description="Billing address"),
    external_reference: Optional[str] = Field(None, description="External reference")
) -> Dict[str, Any]:
    """Update an existing individual customer in Pennylane."""
    try:
        # Build update data with only provided fields
        data = {}
        fields = {
            "first_name": first_name,
            "last_name": last_name,
            "billing_iban": billing_iban,
            "payment_conditions": payment_conditions,
            "phone": phone,
            "reference": reference,
            "notes": notes,
            "emails": emails,
            "billing_address": billing_address,
            "external_reference": external_reference,
        }
        
        for field, value in fields.items():
            if value is not None:
                data[field] = value
        
        if not data:
            return {"error": "No fields to update"}
        
        response = await api_client.put(f"customers/individual/{customer_id}", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        } 