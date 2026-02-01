# Changelog

## [0.2.0] - 2025-01-04

### Added
- **Resources (7 new)**: Structured read-only access to Pennylane data
  - `pennylane://company/info` - Company settings and fiscal years
  - `pennylane://chart_of_accounts/{prefix}` - Chart of accounts with smart grouping
  - `pennylane://journals` - Accounting journals list
  - `pennylane://customers/recent/{limit}` - Recent customers with billing info
  - `pennylane://products/catalog/{limit}` - Product catalog with pricing
  - `pennylane://invoices/recent/{type}/{limit}` - Recent invoices with status
  - `pennylane://analytics/categories` - Analytics category hierarchy

- **Prompts (14 new)**: Guided workflows for common accounting tasks
  - **Accounting**: record_transaction, reconcile_bank, close_period, ledger_entry
  - **Invoicing**: create_invoice, process_supplier_invoice, invoice_followup, credit_note, invoice_analysis  
  - **Analytics**: analyze_finances, categorize_transaction, generate_report, budget_analysis, cash_flow_forecast

- **Documentation**: 
  - Complete feature guide (`documentation/MCP_FEATURES.md`)
  - Enhanced README with workflow examples
  - Test script for resources and prompts

### Fixed
- API filter format now uses proper JSON structure
- Prompt roles changed from "system" to "assistant" for FastMCP compatibility
- Improved error handling for missing API endpoints (fiscal years)
- Fixed TextContent object access in prompts

### Technical
- Resources use FastMCP resource templates with URI parameters
- Prompts return structured PromptMessage lists
- All components properly integrated in server.py

## [0.1.0] - Initial Release

### Added
- **Tools (85)**: Complete coverage of Pennylane API v2
  - Accounting: Journals, ledger entries, trial balance
  - Invoicing: Customer/supplier invoices, products
  - Banking: Transactions, reconciliation
  - Analytics: Categories and categorization
  - Files: Attachments and uploads
  
- Basic OAuth and API key authentication
- Comprehensive error handling
- Environment-based configuration 