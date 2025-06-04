# MCP Pennylane Server - Complete Feature Guide

## Overview

The MCP Pennylane server provides comprehensive integration with Pennylane accounting software through the Model Context Protocol (MCP). It exposes tools, resources, and prompts that enable LLMs to interact effectively with your accounting data.

## Components

### 🛠️ Tools (85 available)

Tools allow LLMs to perform actions in Pennylane. They cover all major API endpoints:

#### Accounting Tools
- **Journals**: Create, list, and manage accounting journals
- **Ledger Accounts**: Manage chart of accounts
- **Ledger Entries**: Create and manage journal entries
- **Ledger Entry Lines**: Letter/unletter entries, manage line items
- **Trial Balance**: Get financial position reports
- **Fiscal Years**: List company fiscal years

#### Customer Management
- **Customers**: Create/update company and individual customers
- **Customer Invoices**: Create, send, and manage invoices
- **Products**: Manage product catalog
- **Invoice Templates**: Use custom invoice templates

#### Supplier Management  
- **Suppliers**: Create and manage suppliers
- **Supplier Invoices**: Process and categorize purchases

#### Banking & Transactions
- **Transactions**: List and reconcile bank transactions
- **Bank Accounts**: View connected bank accounts
- **Matching**: Match transactions to invoices

#### Analytics
- **Categories**: Create and manage analytical categories
- **Category Groups**: Organize categories hierarchically
- **Categorization**: Apply categories to transactions and invoices

#### File Management
- **File Attachments**: Upload supporting documents
- **Ledger Attachments**: Attach files to entries
- **Invoice Appendices**: Add documents to invoices

### 📊 Resources (7 available)

Resources provide read-only access to Pennylane data in a structured format:

1. **`pennylane://company/info`**
   - Company settings and configuration
   - Fiscal year information
   - Currency and country settings

2. **`pennylane://chart_of_accounts`**
   - Complete chart of accounts organized by type
   - Filter by account prefix (e.g., "411" for customers)
   - Account balances and details

3. **`pennylane://journals`**
   - List of all accounting journals
   - Journal codes and configuration

4. **`pennylane://customers/recent`**
   - Recently created/updated customers
   - Contact and billing information
   - Payment terms and VAT details

5. **`pennylane://products/catalog`**
   - Product list with pricing
   - VAT rates and units
   - Associated ledger accounts

6. **`pennylane://invoices/recent`**
   - Recent customer or supplier invoices
   - Status and payment information
   - Outstanding amounts

7. **`pennylane://analytics/categories`**
   - Complete category hierarchy
   - Category groups and directions

### 💬 Prompts (11 available)

Prompts provide guided templates for common accounting workflows:

#### Accounting Prompts
1. **`record_transaction_prompt`**
   - Guide for recording any financial transaction
   - Ensures balanced entries with proper VAT

2. **`reconcile_bank_prompt`**
   - Bank reconciliation assistance
   - Match transactions to invoices
   - Create entries for unmatched items

3. **`close_period_prompt`**
   - Period-end closing procedures
   - Checklist and verification steps

4. **`ledger_entry_prompt`**
   - Manual journal entry creation
   - Account selection and balancing

#### Invoice Prompts
5. **`create_invoice_prompt`**
   - Customer invoice creation workflow
   - VAT rules and payment terms
   - Product selection and pricing

6. **`process_supplier_invoice_prompt`**
   - Supplier invoice processing
   - Expense categorization
   - Payment scheduling

7. **`invoice_followup_prompt`**
   - Collection and follow-up strategies
   - Reminder templates
   - Doubtful debt assessment

8. **`credit_note_prompt`**
   - Credit note creation
   - Link to original invoices
   - VAT reversal handling

9. **`invoice_analysis_prompt`**
   - Invoice performance analysis
   - Payment patterns and aging

#### Analytics Prompts
10. **`analyze_finances_prompt`**
    - Comprehensive financial analysis
    - KPIs and trend identification
    - Strategic recommendations

11. **`categorize_transaction_prompt`**
    - Transaction categorization guidance
    - Analytics category selection

12. **`generate_report_prompt`**
    - Financial report generation
    - P&L, Balance Sheet, Cash Flow
    - Management and board reports

13. **`budget_analysis_prompt`**
    - Budget vs actual analysis
    - Variance identification
    - Corrective actions

14. **`cash_flow_forecast_prompt`**
    - Cash flow projections
    - Scenario planning
    - Working capital optimization

## Usage Examples

### Using Tools
```python
# Create a customer invoice
result = await pennylane_invoices_create(
    customer_id=123,
    invoice_lines=[{
        "product_id": 456,
        "quantity": 5,
        "label": "Consulting services",
        "unit": "hour",
        "raw_currency_unit_price": "150.00",
        "vat_rate": "FR_200"
    }],
    draft=True
)
```

### Using Resources
```python
# Get company information
company_info = await get_resource("pennylane://company/info")

# Get chart of accounts for customer accounts
customer_accounts = await get_resource("pennylane://chart_of_accounts", 
                                     account_prefix="411")
```

### Using Prompts
```python
# Get invoice creation guidance
prompt = await get_prompt("create_invoice_prompt", {
    "customer_info": "ABC Company, VAT: FR12345678901",
    "products_services": "5 hours of consulting at 150€/hour",
    "invoice_type": "standard"
})
```

## Best Practices

### For Tools
1. Always check if entities exist before creating duplicates
2. Ensure journal entries balance (debits = credits)
3. Use appropriate VAT rates based on transaction type
4. Include clear descriptions and references

### For Resources
1. Resources are read-only - use them for information retrieval
2. They return JSON formatted data
3. Use filtering parameters when available
4. Data includes timestamps for cache management

### For Prompts
1. Provide complete context in prompt parameters
2. Prompts return structured messages for LLM guidance
3. Use system messages for role definition
4. Follow the workflow suggestions in responses

## Common Workflows

### Creating an Invoice
1. Use `pennylane://customers/recent` resource to find customer
2. Use `pennylane://products/catalog` to select products
3. Use `create_invoice_prompt` for guidance
4. Execute `pennylane_invoices_create` tool
5. Send invoice with `pennylane_invoices_send_email`

### Recording a Transaction
1. Use `record_transaction_prompt` for guidance
2. Check `pennylane://chart_of_accounts` for accounts
3. Select appropriate journal from `pennylane://journals`
4. Create entry with `pennylane_ledger_entries_create`
5. Apply categories with `pennylane_ledger_entry_lines_categorize`

### Bank Reconciliation
1. List transactions with `pennylane_transactions_list`
2. Use `reconcile_bank_prompt` for each transaction
3. Match to invoices or create entries
4. Letter matched items
5. Categorize for analytics

### Financial Analysis
1. Use `analyze_finances_prompt` with period
2. Retrieve data via resources
3. Generate reports with `generate_report_prompt`
4. Export data with `pennylane_export_analytical_ledger_create`

## Error Handling

The server includes comprehensive error handling:
- API errors are caught and returned with context
- Validation errors provide clear messages
- Network issues are logged with retry guidance
- All errors maintain the MCP protocol format

## Configuration

The server uses environment variables:
- `PENNYLANE_API_KEY`: API authentication
- `PENNYLANE_BASE_URL`: API endpoint
- `LOG_LEVEL`: Logging verbosity
- OAuth configuration for advanced auth

## Support

For issues or questions:
1. Check server info with `pennylane_server_info()`
2. Review logs for detailed error messages
3. Ensure API credentials are valid
4. Consult Pennylane API documentation 