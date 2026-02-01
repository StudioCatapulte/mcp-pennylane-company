"""MCP tools for managing Pennylane accounting entries."""

from typing import Any, Dict, List, Optional
from pydantic import Field

from src.mcp_instance import mcp
from src.utils.api_client import api_client, PennylaneAPIError


# === JOURNALS ===

# Tool: List journals
@mcp.tool()
async def pennylane_journals_list() -> Dict[str, Any]:
    """List all accounting journals from Pennylane.
    
    Returns all available journals including their ID, label, code, and configuration.
    Useful for discovering available journals before creating ledger entries.
    
    Example usage: Get all journals to see which one to use for sales, purchases, or bank transactions.
    """
    try:
        response = await api_client.get("journals")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get journal details
@mcp.tool()
async def pennylane_journals_get(
    journal_id: int = Field(..., description="Journal ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific accounting journal.
    
    Returns complete journal information including configuration settings and capabilities.
    
    Args:
        journal_id: The unique identifier of the journal to retrieve
        
    Example: Get details for journal ID 123 to check its configuration before use.
    """
    try:
        response = await api_client.get(f"journals/{journal_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create journal
@mcp.tool()
async def pennylane_journals_create(
    label: str = Field(..., description="Journal name (e.g., 'Sales Journal', 'Purchase Journal')"),
    code: str = Field(..., description="Unique journal code, max 5 characters (e.g., 'SALES', 'PURCH')")
) -> Dict[str, Any]:
    """Create a new accounting journal in Pennylane.
    
    Creates a new journal for organizing accounting entries by type or purpose.
    Each journal must have a unique code within the company.
    
    Args:
        label: Descriptive name for the journal (e.g., 'Sales Journal', 'Bank Transactions')
        code: Short unique identifier, max 5 characters (e.g., 'SALES', 'BANK1')
        
    Example: Create a journal for tracking online sales with code 'WEBSALES' and label 'Online Sales Journal'.
    """
    try:
        data = {
            "label": label,
            "code": code,
        }
        
        response = await api_client.post("journals", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === LEDGER ACCOUNTS ===

# Tool: List ledger accounts
@mcp.tool()
async def pennylane_ledger_accounts_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string (e.g., 'number start_with 411' for customer accounts)"),
    sort: str = Field("number", description="Sort field (default: by account number)")
) -> Dict[str, Any]:
    """List all ledger accounts from Pennylane chart of accounts.
    
    Returns the company's chart of accounts with account numbers, names, and balances.
    Essential for creating journal entries and understanding account structure.
    
    Args:
        cursor: Pagination cursor for large result sets
        limit: Number of accounts to return (1-100)
        filter: Filter by account properties (e.g., 'number start_with 411' for customers)
        sort: Sort order, typically by account number
        
    Example: Use filter 'number start_with 411' to get all customer accounts,
    or 'number start_with 401' for supplier accounts.
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
        
        response = await api_client.get("ledger_accounts", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get ledger account details
@mcp.tool()
async def pennylane_ledger_accounts_get(
    account_id: int = Field(..., description="Ledger account ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific ledger account."""
    try:
        response = await api_client.get(f"ledger_accounts/{account_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create ledger account
@mcp.tool()
async def pennylane_ledger_accounts_create(
    number: str = Field(..., description="Account number following chart of accounts (e.g., '411001' for customer, '401001' for supplier)"),
    label: str = Field(..., description="Descriptive account name (e.g., 'Customer ABC Corp', 'Office Supplies')"),
    vat_rate: str = Field("any", description="VAT rate code: 'FR_200' (20%), 'FR_100' (10%), 'FR_55' (5.5%), 'FR_21' (2.1%), 'exempt', or 'any'"),
    country_alpha2: str = Field("FR", description="Country code (FR for France, BE for Belgium, CH for Switzerland)")
) -> Dict[str, Any]:
    """Create a new ledger account in the chart of accounts.
    
    Creates a new account for tracking specific transactions or entities.
    Account numbers should follow the standard chart of accounts structure.
    
    Args:
        number: Account number (e.g., '411001' for customers, '401001' for suppliers, '706001' for sales)
        label: Clear, descriptive name for the account
        vat_rate: VAT treatment for this account (use 'any' for flexible VAT handling)
        country_alpha2: Country code for localization
        
    Example: Create customer account with number '411001', label 'Customer XYZ Ltd', and VAT rate 'FR_200'.
    Common account ranges: 411xxx (customers), 401xxx (suppliers), 512xxx (bank accounts).
    """
    try:
        data = {
            "number": number,
            "label": label,
            "vat_rate": vat_rate,
            "country_alpha2": country_alpha2,
        }
        
        response = await api_client.post("ledger_accounts", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === LEDGER ENTRIES ===

# Tool: List ledger entries
@mcp.tool()
async def pennylane_ledger_entries_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string (e.g., 'date gt 2024-01-01', 'journal_id eq 1')"),
    sort: str = Field("-date", description="Sort field, prefix with - for descending")
) -> Dict[str, Any]:
    """List ledger entries (journal entries) from Pennylane."""
    try:
        params = {
            "limit": limit,
            "sort": sort,
        }
        if cursor:
            params["cursor"] = cursor
        if filter:
            params["filter"] = filter
        
        response = await api_client.get("ledger_entries", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create ledger entry
@mcp.tool()
async def pennylane_ledger_entries_create(
    journal_id: int = Field(..., description="Journal ID where this entry will be recorded"),
    date: str = Field(..., description="Entry date in ISO 8601 format (YYYY-MM-DD)"),
    ledger_entry_lines: List[Dict[str, Any]] = Field(..., description="List of entry lines, each with: ledger_account_id (int), debit (string amount), credit (string amount), label (description)"),
    reference: Optional[str] = Field(None, description="Reference number or document ID (e.g., invoice number, payment reference)"),
    label: Optional[str] = Field(None, description="Overall description of the transaction (e.g., 'Customer payment', 'Office supplies purchase')")
) -> Dict[str, Any]:
    """Create a new ledger entry (journal entry) in Pennylane.
    
    Records a double-entry accounting transaction with balanced debits and credits.
    All entry lines must balance (total debits = total credits).
    
    Args:
        journal_id: Target journal for this entry
        date: Transaction date (YYYY-MM-DD format)
        ledger_entry_lines: Array of accounting lines, each containing:
            - ledger_account_id: Account to post to
            - debit: Debit amount as string (e.g., '100.00') or empty string
            - credit: Credit amount as string (e.g., '100.00') or empty string  
            - label: Description for this line
        reference: External reference (invoice number, payment ID, etc.)
        label: Overall transaction description
        
    Example: Record a €100 sale:
    - Line 1: Customer account (411001) debit €100
    - Line 2: Sales account (706001) credit €100
    
    The sum of all debits must equal the sum of all credits.
    """
    try:
        data = {
            "journal_id": journal_id,
            "date": date,
            "ledger_entry_lines": ledger_entry_lines,
        }
        
        if reference:
            data["reference"] = reference
        if label:
            data["label"] = label
        
        response = await api_client.post("ledger_entries", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Update ledger entry
@mcp.tool()
async def pennylane_ledger_entries_update(
    entry_id: int = Field(..., description="Ledger entry ID"),
    date: Optional[str] = Field(None, description="Entry date (ISO 8601)"),
    ledger_entry_lines: Optional[List[Dict[str, Any]]] = Field(None, description="Updated entry lines"),
    reference: Optional[str] = Field(None, description="Entry reference"),
    label: Optional[str] = Field(None, description="Entry description")
) -> Dict[str, Any]:
    """Update an existing ledger entry."""
    try:
        data = {}
        
        if date is not None:
            data["date"] = date
        if ledger_entry_lines is not None:
            data["ledger_entry_lines"] = ledger_entry_lines
        if reference is not None:
            data["reference"] = reference
        if label is not None:
            data["label"] = label
        
        if not data:
            return {"error": "No fields to update"}
        
        response = await api_client.put(f"ledger_entries/{entry_id}", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === LEDGER ENTRY LINES ===

# Tool: List ledger entry lines
@mcp.tool()
async def pennylane_ledger_entry_lines_list(
    cursor: Optional[str] = None,
    limit: int = Field(20, ge=1, le=100, description="Number of items to return (1-100)"),
    filter: Optional[str] = Field(None, description="Filter string (e.g., 'ledger_account_id eq 411000')"),
    sort: str = Field("-date", description="Sort field")
) -> Dict[str, Any]:
    """List ledger entry lines from Pennylane."""
    try:
        params = {
            "limit": limit,
            "sort": sort,
        }
        if cursor:
            params["cursor"] = cursor
        if filter:
            params["filter"] = filter
        
        response = await api_client.get("ledger_entry_lines", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get ledger entry line details
@mcp.tool()
async def pennylane_ledger_entry_lines_get(
    line_id: int = Field(..., description="Ledger entry line ID")
) -> Dict[str, Any]:
    """Get detailed information about a specific ledger entry line."""
    try:
        response = await api_client.get(f"ledger_entry_lines/{line_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Letter ledger entry lines
@mcp.tool()
async def pennylane_ledger_entry_lines_letter(
    line_ids: List[int] = Field(..., description="List of ledger entry line IDs to letter together"),
    unbalanced_lettering_strategy: str = Field("none", description="Strategy for unbalanced lettering: 'none' or 'partial'")
) -> Dict[str, Any]:
    """Letter (reconcile) multiple ledger entry lines together.
    
    Lettering is used to match related transactions, such as an invoice and its payment.
    The sum of debits and credits for the lines being lettered must be zero.
    """
    try:
        data = {
            "unbalanced_lettering_strategy": unbalanced_lettering_strategy,
            "ledger_entry_lines": [{"id": line_id} for line_id in line_ids]
        }
        
        response = await api_client.post("ledger_entry_lines/lettering", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Unletter ledger entry lines
@mcp.tool()
async def pennylane_ledger_entry_lines_unletter(
    line_ids: List[int] = Field(..., description="List of ledger entry line IDs to unletter"),
    unbalanced_lettering_strategy: str = Field("none", description="Strategy for unbalanced lettering: 'none' or 'partial'")
) -> Dict[str, Any]:
    """Unletter (unreconcile) ledger entry lines."""
    try:
        data = {
            "unbalanced_lettering_strategy": unbalanced_lettering_strategy,
            "ledger_entry_lines": [{"id": line_id} for line_id in line_ids]
        }
        
        response = await api_client.delete("ledger_entry_lines/lettering", json=data)
        return {"success": True, "message": "Lines unlettered successfully"}
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === TRIAL BALANCE ===

# Tool: Get trial balance
@mcp.tool()
async def pennylane_trial_balance_get(
    period_start: str = Field(..., description="Start date (ISO 8601)"),
    period_end: str = Field(..., description="End date (ISO 8601)"),
    page: int = Field(1, ge=1, description="Page number (starting at 1)"),
    per_page: int = Field(20, ge=1, le=1000, description="Number of items per page (1-1000)"),
    is_auxiliary: Optional[bool] = Field(None, description="Whether to include auxiliary accounts or not"),
    level: Optional[int] = Field(None, description="Account level detail (1-6)")
) -> Dict[str, Any]:
    """Get the trial balance for a specific period."""
    try:
        params = {
            "period_start": period_start,
            "period_end": period_end,
            "page": page,
            "per_page": per_page,
        }
        if is_auxiliary is not None:
            params["is_auxiliary"] = is_auxiliary
        if level:
            params["level"] = level
        
        response = await api_client.get("trial_balance", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === FISCAL YEARS ===

# Tool: List fiscal years
@mcp.tool()
async def pennylane_fiscal_years_list(
    page: int = Field(1, ge=1, description="Page number (starting at 1)"),
    per_page: int = Field(20, ge=1, le=100, description="Number of items per page (1-100)")
) -> Dict[str, Any]:
    """List company's fiscal years."""
    try:
        params = {
            "page": page,
            "per_page": per_page,
        }
        
        response = await api_client.get("fiscal_years", params=params)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# === ACCOUNTING EXPORTS ===

# Tool: Create FEC export
@mcp.tool()
async def pennylane_export_fec_create(
    period_start: str = Field(..., description="Start date (ISO 8601)"),
    period_end: str = Field(..., description="End date (ISO 8601)")
) -> Dict[str, Any]:
    """Create a FEC (Fichier des Écritures Comptables) export for French accounting compliance."""
    try:
        data = {
            "period_start": period_start,
            "period_end": period_end,
        }
        
        response = await api_client.post("exports/fecs", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get FEC export status
@mcp.tool()
async def pennylane_export_fec_get(
    export_id: int = Field(..., description="FEC export ID")
) -> Dict[str, Any]:
    """Get the status and download URL of a FEC export."""
    try:
        response = await api_client.get(f"exports/fecs/{export_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Create analytical general ledger export
@mcp.tool()
async def pennylane_export_analytical_ledger_create(
    start_date: str = Field(..., description="Start date (ISO 8601)"),
    end_date: str = Field(..., description="End date (ISO 8601)"),
    include_analytics: bool = Field(True, description="Include analytical categories")
) -> Dict[str, Any]:
    """Create an analytical general ledger export."""
    try:
        data = {
            "start_date": start_date,
            "end_date": end_date,
            "include_analytics": include_analytics,
        }
        
        response = await api_client.post("export/analytical_general_ledger", json_data=data)
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        }


# Tool: Get analytical general ledger export status
@mcp.tool()
async def pennylane_export_analytical_ledger_get(
    export_id: int = Field(..., description="Export ID")
) -> Dict[str, Any]:
    """Get the status and download URL of an analytical general ledger export."""
    try:
        response = await api_client.get(f"export/analytical_general_ledger/{export_id}")
        return response
    except PennylaneAPIError as e:
        return {
            "error": str(e),
            "status_code": e.status_code,
            "details": e.response
        } 