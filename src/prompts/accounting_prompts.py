"""Accounting prompts for Pennylane MCP server."""

from typing import Optional, List
from datetime import date

from fastmcp.prompts.prompt import Message, PromptMessage
from src.mcp_instance import mcp


@mcp.prompt()
def record_transaction_prompt(
    transaction_type: str,
    amount: float,
    description: str,
    date: Optional[str] = None,
    accounts_involved: Optional[str] = None,
) -> List[PromptMessage]:
    """Generate a prompt for recording a financial transaction.
    
    Args:
        transaction_type: Type of transaction (sale, purchase, payment, receipt, transfer, etc.)
        amount: Transaction amount
        description: Description of the transaction
        date: Transaction date (optional, defaults to today)
        accounts_involved: Specific accounts to use (optional)
    
    Returns:
        Prompt messages to guide the recording of the transaction.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I am an expert accounting assistant helping to record transactions in Pennylane.
        
Key principles:
1. Every transaction must balance (debits = credits)
2. Follow the chart of accounts structure
3. Use appropriate VAT rates for the jurisdiction
4. Ensure proper documentation and references

Common account prefixes:
- 411xxx: Customer accounts
- 401xxx: Supplier accounts  
- 512xxx: Bank accounts
- 606xxx: Purchase accounts
- 706xxx: Sales accounts
- 445xxx: VAT accounts

I'll help you record this transaction correctly."""
    )
    
    user_content = f"""Please help me record this {transaction_type} transaction:

Amount: {amount}
Description: {description}
Date: {date or 'today'}
"""
    
    if accounts_involved:
        user_content += f"Accounts to consider: {accounts_involved}\n"
    
    user_content += """
Please:
1. Identify the appropriate ledger accounts
2. Determine the correct debit and credit entries
3. Apply the appropriate VAT treatment
4. Suggest a clear reference and label for the entry
5. Use the appropriate journal for this type of transaction

Format the response as a structured journal entry ready for posting."""
    
    return [assistant_msg, Message(role="user", content=user_content)]


@mcp.prompt()
def reconcile_bank_prompt(
    bank_transaction_description: str,
    amount: float,
    transaction_date: str,
    possible_matches: Optional[str] = None,
) -> List[PromptMessage]:
    """Generate a prompt for bank reconciliation.
    
    Args:
        bank_transaction_description: Description from bank statement
        amount: Transaction amount (positive for receipts, negative for payments)
        transaction_date: Date of the bank transaction
        possible_matches: Any potential matching invoices or entries
    
    Returns:
        Prompt messages to guide bank reconciliation.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I am an expert at bank reconciliation in Pennylane.

My task is to:
1. Analyze bank transactions and identify their nature
2. Match them with existing invoices, bills, or ledger entries
3. Create appropriate ledger entries for unmatched transactions
4. Ensure proper categorization for analytics

Remember:
- Positive amounts are receipts (money in)
- Negative amounts are payments (money out)
- Always check for existing invoices before creating new entries
- Use appropriate analytical categories

I'll help you reconcile this transaction."""
    )
    
    user_content = f"""Please help reconcile this bank transaction:

Bank description: {bank_transaction_description}
Amount: {amount} ({"receipt" if amount > 0 else "payment"})
Date: {transaction_date}
"""
    
    if possible_matches:
        user_content += f"\nPossible matches found: {possible_matches}"
    
    user_content += """

Please determine:
1. What type of transaction this is
2. Whether it matches any existing invoice or bill
3. If no match, what ledger entries should be created
4. Which analytical categories should be applied
5. Any follow-up actions needed"""
    
    return [assistant_msg, Message(role="user", content=user_content)]


@mcp.prompt()
def close_period_prompt(
    period_start: str,
    period_end: str,
    checklist_items: Optional[List[str]] = None,
) -> PromptMessage:
    """Generate a prompt for period closing procedures.
    
    Args:
        period_start: Start date of the period to close
        period_end: End date of the period to close
        checklist_items: Specific items to verify
    
    Returns:
        Prompt message for guiding period closing.
    """
    content = f"""Please guide me through closing the accounting period from {period_start} to {period_end}.

Standard closing checklist:
1. Verify all bank transactions are reconciled
2. Ensure all invoices are recorded
3. Check that all expenses are properly documented
4. Verify VAT calculations and declarations
5. Review and reconcile balance sheet accounts
6. Generate trial balance and verify it balances
"""
    
    if checklist_items:
        content += "\nAdditional items to check:\n"
        for item in checklist_items:
            content += f"- {item}\n"
    
    content += """
Please:
1. List any outstanding items that need attention
2. Suggest the order of tasks to complete
3. Identify any potential issues or discrepancies
4. Recommend any adjusting entries needed"""
    
    return Message(role="user", content=content)


@mcp.prompt()
def ledger_entry_prompt(
    entry_description: str,
    journal_type: Optional[str] = None,
    reference_document: Optional[str] = None,
) -> List[PromptMessage]:
    """Generate a prompt for creating manual ledger entries.
    
    Args:
        entry_description: Description of what needs to be recorded
        journal_type: Type of journal to use (optional)
        reference_document: Reference to supporting documentation
    
    Returns:
        Prompt messages for creating ledger entries.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I'll help you create ledger entries in Pennylane. 

Guidelines:
1. Use the correct account numbers from the chart of accounts
2. Ensure entries balance (total debits = total credits)
3. Include clear descriptions for each line
4. Add appropriate references to source documents
5. Apply analytical categories where relevant

Remember the accounting equation: Assets = Liabilities + Equity
And: Debits increase assets/expenses, Credits increase liabilities/equity/revenue

Let me assist with your ledger entry."""
    )
    
    user_content = f"""Create a ledger entry for: {entry_description}"""
    
    if journal_type:
        user_content += f"\nJournal type: {journal_type}"
    
    if reference_document:
        user_content += f"\nReference document: {reference_document}"
    
    user_content += """

Please provide:
1. The journal to use
2. Each line item with:
   - Account number and name
   - Debit or credit amount
   - Clear description
3. Overall entry reference
4. Any analytical categories to apply"""
    
    return [assistant_msg, Message(role="user", content=user_content)] 