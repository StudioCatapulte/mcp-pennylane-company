# MCP Pennylane - Model Context Protocol Server for Pennylane Accounting

A comprehensive MCP (Model Context Protocol) server that enables LLMs to interact with Pennylane accounting software through tools, resources, and prompts.

## Features

### 🛠️ **85 Tools** - Perform actions in Pennylane
- **Accounting**: Journals, ledger entries, trial balance, fiscal years
- **Invoicing**: Create, send, and manage customer/supplier invoices
- **Banking**: Transaction reconciliation and categorization
- **Analytics**: Categories and analytical reporting
- **File Management**: Document attachments and uploads

### 📊 **7 Resources** - Access structured data
- Company information and settings
- Chart of accounts with smart grouping
- Customer and product catalogs
- Recent invoices and transactions
- Analytics categories hierarchy

### 💬 **14 Prompts** - Guided workflows
- Invoice creation and processing
- Transaction recording and reconciliation
- Financial analysis and reporting
- Period closing procedures
- Cash flow forecasting

## Installation

1. Clone the repository:
```bash
git clone https://github.com/StudioCatapulte/mcp-pennylane-company.git
cd mcp-pennylane-company
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
# For production use:
pip install -r requirements.txt

# For development (includes testing and linting tools):
pip install -r requirements-dev.txt

# For exact reproducible environment:
pip install -r requirements-lock.txt
```

4. Configure environment:
```bash
cp .env.example .env
# Edit .env with your Pennylane API credentials
```

## Configuration

### API Key Authentication
```env
PENNYLANE_API_KEY=your_api_key_here
PENNYLANE_BASE_URL=https://app.pennylane.com/api/external/v2
```

### OAuth Authentication (Advanced)
```env
USE_OAUTH=true
OAUTH_CLIENT_ID=your_client_id
OAUTH_CLIENT_SECRET=your_client_secret
OAUTH_REDIRECT_URI=http://localhost:8000/callback
```

## Usage with Claude Desktop

Add to your Claude Desktop configuration (`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "pennylane": {
      "command": "python",
      "args": ["/path/to/mcp-pennylane-company/src/server.py"],
      "env": {
        "PENNYLANE_API_KEY": "your_api_key_here"
      }
    }
  }
}
```

## Transport Options

The Pennylane MCP server supports multiple transport protocols:

### STDIO Transport (Default)
Best for local tools and Claude Desktop integration:

```bash
# Run with default STDIO transport
python src/server.py

# Or explicitly specify STDIO
python src/server.py --transport stdio
```

### Streamable HTTP Transport
Recommended for web deployments and remote access:

```bash
# Run with Streamable HTTP on default port 8000
python src/server.py --transport streamable-http

# Custom configuration
python src/server.py --transport streamable-http --host 0.0.0.0 --port 9000

# With debug logging
python src/server.py --transport streamable-http --log-level debug
```

**Features:**
- Single endpoint for all communication (`/mcp`)
- Health check endpoint at `/health`
- Bi-directional communication
- Automatic connection upgrades for long-running tasks

### Using the HTTP Client

```python
from fastmcp import Client

# Connect to HTTP server
async with Client("http://localhost:8000/mcp") as client:
    # Call tools
    result = await client.call_tool("pennylane_customers_list", {"limit": 10})
    
    # Read resources
    data = await client.read_resource("pennylane://company/info")
```

See `examples/http_client_example.py` for a complete example.

### Using with FastMCP CLI

```bash
# Run with CLI (overrides any transport in code)
fastmcp run src/server.py --transport streamable-http --port 9000

# Development mode with inspector
fastmcp dev src/server.py
```

## Example Workflows

### Creating an Invoice
```
1. Check customer exists: Use resource pennylane://customers/recent/10
2. Get products: Use resource pennylane://products/catalog/20
3. Get guidance: Use prompt create_invoice_prompt
4. Create invoice: Use tool pennylane_invoices_create
5. Send invoice: Use tool pennylane_invoices_send_email
```

### Recording a Transaction
```
1. Get guidance: Use prompt record_transaction_prompt
2. View accounts: Use resource pennylane://chart_of_accounts/all
3. Select journal: Use resource pennylane://journals
4. Create entry: Use tool pennylane_ledger_entries_create
5. Categorize: Use tool pennylane_ledger_entry_lines_categorize
```

### Financial Analysis
```
1. Set parameters: Use prompt analyze_finances_prompt
2. Get company info: Use resource pennylane://company/info
3. View invoices: Use resource pennylane://invoices/recent/customer/50
4. Generate report: Use prompt generate_report_prompt
5. Export data: Use tool pennylane_export_analytical_ledger_create
```

## Resource Examples

### Company Information
```
pennylane://company/info
Returns: Company settings, fiscal years, currency, country
```

### Chart of Accounts
```
pennylane://chart_of_accounts/411  # Customer accounts only
pennylane://chart_of_accounts/all  # All accounts grouped by type
```

### Recent Data
```
pennylane://customers/recent/20    # Last 20 customers
pennylane://invoices/recent/customer/10  # Last 10 customer invoices
pennylane://products/catalog/50    # 50 products from catalog
```

## Prompt Examples

### Invoice Creation
```python
create_invoice_prompt(
    customer_info="ABC Corp, VAT: FR12345678901",
    products_services="5 hours consulting at 150€/hour",
    invoice_type="standard",
    special_requirements="Net 30 payment terms"
)
```

### Transaction Recording
```python
record_transaction_prompt(
    transaction_type="sale",
    amount=1500.00,
    description="Consulting services - Project X",
    date="2024-01-15"
)
```

### Financial Analysis
```python
analyze_finances_prompt(
    analysis_period="2024-Q1",
    focus_areas=["revenue", "cash_flow"],
    comparison_period="2023-Q4"
)
```

## Architecture

```
src/
├── server.py          # Main MCP server
├── mcp_instance.py    # FastMCP configuration
├── config.py          # Settings management
├── tools/             # 85 API tools
├── resources/         # 7 data resources
├── prompts/           # 14 workflow prompts
└── utils/             # API client and helpers
```

## Development

### Running Tests
```bash
python -m pytest tests/
```

### Adding New Features
1. **Tools**: Add to `src/tools/` following existing patterns
2. **Resources**: Add to `src/resources/` with proper URI scheme
3. **Prompts**: Add to `src/prompts/` with clear parameter descriptions

## API Coverage

| Category | Coverage | Features |
|----------|----------|----------|
| Accounting | ✅ 100% | Journals, entries, accounts, balance |
| Invoicing | ✅ 100% | Customer/supplier invoices, credit notes |
| Banking | ✅ 100% | Transactions, reconciliation, accounts |
| Analytics | ✅ 100% | Categories, groups, categorization |
| Files | ✅ 100% | Attachments, uploads, appendices |
| Exports | ✅ 100% | FEC, analytical ledger |

## Documentation

- [Complete Feature Guide](documentation/MCP_FEATURES.md)
- [API Reference](documentation/api_pennylane_doc/)
- [MCP Protocol Details](documentation/mcp/)

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Support

For issues or questions:
1. Check the [Feature Guide](documentation/MCP_FEATURES.md)
2. Review server logs for detailed errors
3. Ensure API credentials are valid
4. Open an issue on GitHub

---

## Author

**Guillaume Sayer** - [Studio Catapulte](https://catapulte.studio)

---

Built with [FastMCP](https://github.com/jlowin/fastmcp) and the [Model Context Protocol](https://modelcontextprotocol.io) by Anthropic.