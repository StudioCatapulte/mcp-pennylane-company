"""Invoice prompts for Pennylane MCP server."""

from typing import Optional, List, Dict

from fastmcp.prompts.prompt import Message, PromptMessage
from src.mcp_instance import mcp


@mcp.prompt()
def create_invoice_prompt(
    customer_info: str,
    products_services: str,
    invoice_type: str = "standard",
    special_requirements: Optional[str] = None,
) -> List[PromptMessage]:
    """Generate a prompt for creating a customer invoice.
    
    Args:
        customer_info: Information about the customer
        products_services: Description of products/services to invoice
        invoice_type: Type of invoice (standard, recurring, credit_note)
        special_requirements: Any special requirements or conditions
    
    Returns:
        Prompt messages to guide invoice creation.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I am an expert at creating invoices in Pennylane.

Key considerations:
1. Verify customer exists or needs to be created
2. Select appropriate products or create new ones
3. Apply correct VAT rates based on customer type and location
4. Set appropriate payment terms
5. Include all required legal mentions

VAT rules:
- B2B with valid EU VAT number: reverse charge (0% VAT)
- B2C or domestic: standard VAT rate (20% in France)
- Some products/services may have reduced rates
- Export outside EU: 0% VAT

Invoice components:
- Customer details and billing address
- Product/service lines with quantities and prices
- VAT calculation
- Payment terms and due date
- Legal mentions and references

I'll help you create your invoice."""
    )
    
    user_content = f"""Please help me create a {invoice_type} invoice:

Customer information:
{customer_info}

Products/Services to invoice:
{products_services}
"""
    
    if special_requirements:
        user_content += f"\nSpecial requirements:\n{special_requirements}"
    
    user_content += """

Please:
1. Verify if the customer exists or needs to be created
2. List the invoice lines with appropriate products
3. Calculate the correct VAT treatment
4. Suggest payment terms and due date
5. Include any necessary legal mentions
6. Provide the complete invoice data structure"""
    
    user_msg = Message(role="user", content=user_content)
    
    return [assistant_msg, user_msg]


@mcp.prompt()
def process_supplier_invoice_prompt(
    supplier_info: str,
    invoice_details: str,
    expense_type: str,
    has_attachment: bool = False,
) -> List[PromptMessage]:
    """Generate a prompt for processing a supplier invoice.
    
    Args:
        supplier_info: Information about the supplier
        invoice_details: Details from the invoice
        expense_type: Type of expense
        has_attachment: Whether an invoice file is attached
    
    Returns:
        Prompt messages to guide supplier invoice processing.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I am experienced at processing supplier invoices in Pennylane.

Key tasks:
1. Verify or create supplier record
2. Extract key invoice information
3. Assign to correct expense accounts
4. Verify VAT treatment and amounts
5. Apply analytical categories
6. Set up for payment processing

Common expense accounts:
- 606xxx: Purchases of goods
- 611xxx: External services
- 613xxx: Rent and leases
- 615xxx: Maintenance
- 622xxx: Professional fees
- 625xxx: Travel expenses

Remember to:
- Check VAT deductibility
- Verify invoice compliance
- Match with purchase orders if applicable
- Set payment due date

I'll help you process this invoice correctly."""
    )
    
    user_content = f"""Process this supplier invoice:

Supplier: {supplier_info}

Invoice details:
{invoice_details}

Expense type: {expense_type}
Has attachment: {"Yes" if has_attachment else "No"}

Please:
1. Verify supplier exists or create if needed
2. Extract and structure the invoice data
3. Assign appropriate expense accounts
4. Calculate VAT treatment
5. Suggest analytical categories
6. Set payment schedule"""
    
    return [assistant_msg, Message(role="user", content=user_content)]


@mcp.prompt()
def invoice_followup_prompt(
    overdue_days: int,
    customer_name: str,
    invoice_amount: float,
    previous_reminders: Optional[int] = None,
) -> PromptMessage:
    """Generate a prompt for invoice follow-up and collection.
    
    Args:
        overdue_days: Number of days overdue
        customer_name: Name of the customer
        invoice_amount: Outstanding amount
        previous_reminders: Number of previous reminders sent
    
    Returns:
        Prompt message for invoice follow-up.
    """
    content = f"""Please help with collection follow-up for an overdue invoice:

Customer: {customer_name}
Outstanding amount: {invoice_amount}
Days overdue: {overdue_days}
Previous reminders sent: {previous_reminders or 0}

Based on the situation, please:
1. Assess the appropriate follow-up action
2. Draft a suitable reminder message
3. Suggest any accounting entries needed (e.g., doubtful debt provision)
4. Recommend collection strategy
5. Identify if legal action threshold is approaching

Consider:
- Customer payment history
- Size of the debt
- Cost-benefit of collection efforts
- Maintaining customer relationship where appropriate"""
    
    return Message(role="user", content=content)


@mcp.prompt()
def credit_note_prompt(
    original_invoice_ref: str,
    reason: str,
    items_to_credit: str,
    partial_or_full: str = "partial",
) -> List[PromptMessage]:
    """Generate a prompt for creating credit notes.
    
    Args:
        original_invoice_ref: Reference to the original invoice
        reason: Reason for the credit note
        items_to_credit: Items or amounts to credit
        partial_or_full: Whether it's a partial or full credit
    
    Returns:
        Prompt messages for creating credit notes.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I'll help you create credit notes in Pennylane.

Credit note guidelines:
1. Must reference the original invoice
2. Use negative amounts
3. Apply same VAT treatment as original
4. Include clear reason for credit
5. Ensure proper accounting reversal

Common reasons:
- Product return
- Service complaint  
- Pricing error
- Quantity adjustment
- Quality issue
- Cancellation

Let me assist with your credit note."""
    )
    
    user_content = f"""Create a {partial_or_full} credit note:

Original invoice: {original_invoice_ref}
Reason: {reason}
Items to credit:
{items_to_credit}

Please:
1. Verify the original invoice details
2. Calculate the credit amounts
3. Apply correct VAT reversal
4. Create the credit note structure
5. Explain the accounting impact
6. Suggest how to link it to the original invoice"""
    
    return [assistant_msg, Message(role="user", content=user_content)]


@mcp.prompt()
def invoice_analysis_prompt(
    period: str,
    analysis_type: str = "revenue",
    specific_focus: Optional[str] = None,
) -> PromptMessage:
    """Generate a prompt for invoice analysis and reporting.
    
    Args:
        period: Period to analyze (e.g., "2024-Q1", "January 2024")
        analysis_type: Type of analysis (revenue, payment_performance, customer_analysis)
        specific_focus: Specific area to focus on
    
    Returns:
        Prompt message for invoice analysis.
    """
    content = f"""Please analyze invoices for {period}:

Analysis type: {analysis_type}
"""
    
    if specific_focus:
        content += f"Specific focus: {specific_focus}\n"
    
    content += """
Please provide:
1. Key metrics and totals
2. Trends compared to previous periods
3. Top customers/suppliers by value
4. Payment performance statistics
5. Outstanding amounts aging
6. Any concerning patterns
7. Recommendations for improvement

Include:
- Revenue/expense breakdown
- VAT summary
- Customer concentration risk
- Cash flow impact
- Year-over-year comparison where relevant"""
    
    return Message(role="user", content=content) 