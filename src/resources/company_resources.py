"""Company resources for Pennylane MCP server."""

import logging
from typing import Optional
from datetime import datetime, date
import json

from src.mcp_instance import mcp
from src.utils.api_client import api_client

logger = logging.getLogger(__name__)


@mcp.resource("pennylane://company/info")
async def get_company_info() -> str:
    """Get current company information and settings.
    
    Returns JSON with company details, fiscal year info, and configuration.
    """
    try:
        # Get user profile (contains company info)
        user_info = await api_client.get("me")
        
        # Try to get fiscal years (may not be available in all accounts)
        try:
            fiscal_years = await api_client.get("company/fiscal_years", params={"per_page": 5})
            fiscal_years_data = fiscal_years.get("fiscal_years", [])
        except:
            fiscal_years_data = []
        
        result = {
            "company": {
                "email": user_info.get("email"),
                "currency": user_info.get("currency", "EUR"),
                "country": user_info.get("country_alpha2", "FR"),
            },
            "fiscal_years": [
                {
                    "id": fy.get("id"),
                    "start": fy.get("starts_at"),
                    "end": fy.get("ends_at"),
                    "status": fy.get("status"),
                }
                for fy in fiscal_years_data
            ],
            "retrieved_at": datetime.utcnow().isoformat(),
        }
        
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error fetching company info: {e}")
        return json.dumps({"error": str(e)}, indent=2)


@mcp.resource("pennylane://chart_of_accounts/{account_prefix}")
async def get_chart_of_accounts(account_prefix: Optional[str] = None) -> str:
    """Get the company's chart of accounts.
    
    Args:
        account_prefix: Optional prefix to filter accounts (e.g., "411" for customers, "401" for suppliers)
    
    Returns JSON with ledger accounts organized by type.
    """
    try:
        params = {"limit": 100, "sort": "number"}
        
        # Use JSON format for filter if prefix is specified
        if account_prefix and account_prefix != "all":
            filter_json = json.dumps([{
                "field": "number",
                "operator": "start_with",
                "value": account_prefix
            }])
            params["filter"] = filter_json
        
        accounts = await api_client.get("ledger_accounts", params=params)
        
        # Group accounts by type based on number prefix
        grouped = {
            "assets": [],
            "liabilities": [],
            "equity": [],
            "revenue": [],
            "expenses": [],
            "customers": [],
            "suppliers": [],
            "banks": [],
            "other": [],
        }
        
        for account in accounts.get("ledger_accounts", []):
            num = account.get("number", "")
            if num.startswith("411"):
                grouped["customers"].append(account)
            elif num.startswith("401"):
                grouped["suppliers"].append(account)
            elif num.startswith("512"):
                grouped["banks"].append(account)
            elif num.startswith("1"):
                grouped["assets"].append(account)
            elif num.startswith("2") or num.startswith("3") or num.startswith("4"):
                grouped["liabilities"].append(account)
            elif num.startswith("5"):
                grouped["equity"].append(account)
            elif num.startswith("6"):
                grouped["expenses"].append(account)
            elif num.startswith("7"):
                grouped["revenue"].append(account)
            else:
                grouped["other"].append(account)
        
        # Clean up empty groups
        result = {k: v for k, v in grouped.items() if v}
        result["total_accounts"] = sum(len(v) for v in result.values())
        result["filter"] = account_prefix or "all"
        result["retrieved_at"] = datetime.utcnow().isoformat()
        
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error fetching chart of accounts: {e}")
        return json.dumps({"error": str(e)}, indent=2)


@mcp.resource("pennylane://journals")
async def get_journals_list() -> str:
    """Get all accounting journals.
    
    Returns JSON with available journals and their configuration.
    """
    try:
        journals = await api_client.get("journals")
        
        result = {
            "journals": [
                {
                    "id": j.get("id"),
                    "label": j.get("label"),
                    "code": j.get("code"),
                    "deletable": j.get("deletable", False),
                }
                for j in journals.get("journals", [])
            ],
            "count": len(journals.get("journals", [])),
            "retrieved_at": datetime.utcnow().isoformat(),
        }
        
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error fetching journals: {e}")
        return json.dumps({"error": str(e)}, indent=2)


@mcp.resource("pennylane://customers/recent/{limit}")
async def get_recent_customers(limit: int = 10) -> str:
    """Get recently created or updated customers.
    
    Args:
        limit: Maximum number of customers to return (default: 10)
    
    Returns JSON with customer list including contact and billing info.
    """
    try:
        customers = await api_client.get("customers", params={"limit": limit, "sort": "-id"})
        
        result = {
            "customers": [
                {
                    "id": c.get("id"),
                    "type": c.get("customer_type"),
                    "name": c.get("name") if c.get("customer_type") == "company" else f"{c.get('first_name', '')} {c.get('last_name', '')}".strip(),
                    "billing_address": c.get("billing_address"),
                    "emails": c.get("emails", []),
                    "payment_conditions": c.get("payment_conditions"),
                    "reference": c.get("reference"),
                    "vat_number": c.get("vat_number"),
                }
                for c in customers.get("customers", [])
            ],
            "count": len(customers.get("customers", [])),
            "total_available": customers.get("total_count", 0),
            "retrieved_at": datetime.utcnow().isoformat(),
        }
        
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error fetching customers: {e}")
        return json.dumps({"error": str(e)}, indent=2)


@mcp.resource("pennylane://products/catalog/{limit}")
async def get_products_catalog(limit: int = 20) -> str:
    """Get product catalog with pricing and VAT information.
    
    Args:
        limit: Maximum number of products to return (default: 20)
    
    Returns JSON with product list including pricing and configuration.
    """
    try:
        products = await api_client.get("products", params={"limit": limit, "sort": "-id"})
        
        result = {
            "products": [
                {
                    "id": p.get("id"),
                    "label": p.get("label"),
                    "reference": p.get("reference"),
                    "description": p.get("description"),
                    "unit": p.get("unit"),
                    "currency": p.get("currency"),
                    "price_before_tax": p.get("price_before_tax"),
                    "vat_rate": p.get("vat_rate"),
                    "ledger_account_id": p.get("ledger_account_id"),
                }
                for p in products.get("products", [])
            ],
            "count": len(products.get("products", [])),
            "total_available": products.get("total_count", 0),
            "retrieved_at": datetime.utcnow().isoformat(),
        }
        
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error fetching products: {e}")
        return json.dumps({"error": str(e)}, indent=2)


@mcp.resource("pennylane://invoices/recent/{invoice_type}/{limit}")
async def get_recent_invoices(invoice_type: str = "customer", limit: int = 10) -> str:
    """Get recent invoices with status and payment information.
    
    Args:
        invoice_type: Type of invoices - "customer" or "supplier" (default: "customer")
        limit: Maximum number of invoices to return (default: 10)
    
    Returns JSON with invoice list including amounts and status.
    """
    try:
        endpoint = "customer_invoices" if invoice_type == "customer" else "supplier_invoices"
        invoices = await api_client.get(endpoint, params={"limit": limit, "sort": "-date"})
        
        invoice_key = "customer_invoices" if invoice_type == "customer" else "supplier_invoices"
        
        result = {
            "invoice_type": invoice_type,
            "invoices": [
                {
                    "id": inv.get("id"),
                    "number": inv.get("invoice_number"),
                    "date": inv.get("date"),
                    "deadline": inv.get("deadline"),
                    "status": inv.get("status"),
                    "customer_name": inv.get("customer", {}).get("name") if invoice_type == "customer" else inv.get("supplier", {}).get("name"),
                    "amount_including_tax": inv.get("amount"),
                    "amount_before_tax": inv.get("amount_before_tax"),
                    "currency": inv.get("currency"),
                    "payment_status": inv.get("payment_status"),
                }
                for inv in invoices.get(invoice_key, [])
            ],
            "count": len(invoices.get(invoice_key, [])),
            "retrieved_at": datetime.utcnow().isoformat(),
        }
        
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error fetching invoices: {e}")
        return json.dumps({"error": str(e)}, indent=2)


@mcp.resource("pennylane://analytics/categories")
async def get_analytics_categories() -> str:
    """Get analytical categories and category groups.
    
    Returns JSON with category hierarchy for analytics.
    """
    try:
        # Get category groups
        groups = await api_client.get("category_groups")
        
        # Get categories for each group
        result = {
            "category_groups": []
        }
        
        for group in groups.get("category_groups", []):
            categories = await api_client.get(f"category_groups/{group['id']}/categories")
            
            group_data = {
                "id": group.get("id"),
                "label": group.get("label"),
                "categories": [
                    {
                        "id": cat.get("id"),
                        "label": cat.get("label"),
                        "direction": cat.get("direction"),
                    }
                    for cat in categories.get("categories", [])
                ],
                "category_count": len(categories.get("categories", [])),
            }
            result["category_groups"].append(group_data)
        
        result["total_groups"] = len(result["category_groups"])
        result["retrieved_at"] = datetime.utcnow().isoformat()
        
        return json.dumps(result, indent=2, ensure_ascii=False)
    except Exception as e:
        logger.error(f"Error fetching analytics categories: {e}")
        return json.dumps({"error": str(e)}, indent=2) 