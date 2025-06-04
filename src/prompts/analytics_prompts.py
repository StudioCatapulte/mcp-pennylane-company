"""Analytics prompts for Pennylane MCP server."""

from typing import Optional, List

from fastmcp.prompts.prompt import Message, PromptMessage
from src.mcp_instance import mcp


@mcp.prompt()
def analyze_finances_prompt(
    analysis_period: str,
    focus_areas: Optional[List[str]] = None,
    comparison_period: Optional[str] = None,
) -> List[PromptMessage]:
    """Generate a prompt for comprehensive financial analysis.
    
    Args:
        analysis_period: Period to analyze (e.g., "2024-Q1", "January 2024")
        focus_areas: Specific areas to focus on (revenue, expenses, cash_flow, profitability)
        comparison_period: Previous period for comparison
    
    Returns:
        Prompt messages to guide financial analysis.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I am a financial analyst examining Pennylane accounting data.

My analysis covers:
1. Financial performance metrics
2. Trends and patterns
3. Variances and anomalies
4. Cash flow analysis
5. Profitability by segment
6. Key ratios and indicators

I use analytical categories to provide insights by:
- Business unit/department
- Product/service line
- Customer segment
- Geographic region
- Project/campaign

I present findings with:
- Executive summary
- Detailed analysis
- Visual descriptions (for charts/graphs)
- Actionable recommendations

Let me analyze your financial data."""
    )
    
    user_content = f"""Analyze the financial data for {analysis_period}."""
    
    if focus_areas:
        user_content += f"\n\nFocus areas: {', '.join(focus_areas)}"
    
    if comparison_period:
        user_content += f"\nCompare with: {comparison_period}"
    
    user_content += """

Please provide:
1. Overall financial health assessment
2. Revenue analysis by category/customer
3. Expense breakdown and trends
4. Cash flow statement highlights
5. Profitability analysis
6. Key performance indicators (KPIs)
7. Areas of concern or opportunity
8. Strategic recommendations

Include both absolute values and percentages, growth rates, and relevant ratios."""
    
    return [assistant_msg, Message(role="user", content=user_content)]


@mcp.prompt()
def categorize_transaction_prompt(
    transaction_description: str,
    amount: float,
    transaction_type: str,
    existing_categories: Optional[str] = None,
) -> PromptMessage:
    """Generate a prompt for categorizing transactions.
    
    Args:
        transaction_description: Description of the transaction
        amount: Transaction amount
        transaction_type: Type (income/expense)
        existing_categories: Available analytical categories
    
    Returns:
        Prompt message for transaction categorization.
    """
    content = f"""Please categorize this transaction:

Description: {transaction_description}
Amount: {amount}
Type: {transaction_type}
"""
    
    if existing_categories:
        content += f"\nAvailable categories:\n{existing_categories}"
    
    content += """

Based on the transaction details:
1. Suggest the most appropriate analytical category
2. Explain why this categorization makes sense
3. Identify if multiple categories might apply
4. Recommend any new categories if needed
5. Consider the impact on financial reporting

Categorization should enable:
- Accurate cost center allocation
- Meaningful management reporting
- Budget vs actual comparison
- Trend analysis over time"""
    
    return Message(role="user", content=content)


@mcp.prompt()
def generate_report_prompt(
    report_type: str,
    period: str,
    recipients: Optional[str] = None,
    specific_requirements: Optional[str] = None,
) -> List[PromptMessage]:
    """Generate a prompt for creating financial reports.
    
    Args:
        report_type: Type of report (P&L, balance_sheet, cash_flow, management, board)
        period: Reporting period
        recipients: Target audience for the report
        specific_requirements: Any specific requirements
    
    Returns:
        Prompt messages for report generation.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I'll help you prepare financial reports from Pennylane data.

Report types and my focus:
- P&L: Revenue, expenses, profitability
- Balance Sheet: Assets, liabilities, equity position
- Cash Flow: Operating, investing, financing activities
- Management Report: KPIs, variances, operational metrics
- Board Report: Strategic metrics, risks, opportunities

I ensure reports include:
1. Clear structure and formatting
2. Period comparisons
3. Variance analysis
4. Key insights and commentary
5. Visual representations where helpful
6. Executive summary for longer reports

Let me create your report."""
    )
    
    user_content = f"""Generate a {report_type} report for {period}."""
    
    if recipients:
        user_content += f"\nTarget audience: {recipients}"
    
    if specific_requirements:
        user_content += f"\nSpecific requirements:\n{specific_requirements}"
    
    user_content += """

The report should include:
1. Report header with period and date
2. Key highlights/executive summary
3. Detailed sections as appropriate
4. Comparison with previous period/budget
5. Notable variances explained
6. Trends and patterns identified
7. Recommendations or action items
8. Supporting schedules if needed

Format for clarity and professional presentation."""
    
    return [assistant_msg, Message(role="user", content=user_content)]


@mcp.prompt()
def budget_analysis_prompt(
    period: str,
    budget_data: str,
    variance_threshold: float = 10.0,
) -> PromptMessage:
    """Generate a prompt for budget vs actual analysis.
    
    Args:
        period: Period for analysis
        budget_data: Budget information or reference
        variance_threshold: Percentage threshold for highlighting variances
    
    Returns:
        Prompt message for budget analysis.
    """
    content = f"""Perform budget vs actual analysis for {period}:

Budget reference: {budget_data}
Variance threshold: {variance_threshold}%

Please analyze:
1. Overall budget performance
2. Revenue achievement vs target
3. Expense control by category
4. Significant variances (>{variance_threshold}%)
5. Variance explanations and drivers
6. Forecast for remainder of period
7. Corrective actions needed

For each variance:
- Calculate absolute and percentage difference
- Identify if favorable or unfavorable
- Explain likely causes
- Suggest management actions

Highlight:
- Budget items at risk
- Opportunities to improve
- Structural vs timing differences
- Need for budget revisions"""
    
    return Message(role="user", content=content)


@mcp.prompt()
def cash_flow_forecast_prompt(
    forecast_period: str,
    include_scenarios: bool = False,
    key_assumptions: Optional[str] = None,
) -> List[PromptMessage]:
    """Generate a prompt for cash flow forecasting.
    
    Args:
        forecast_period: Period to forecast (e.g., "next 3 months", "Q2 2024")
        include_scenarios: Whether to include best/worst case scenarios
        key_assumptions: Important assumptions for the forecast
    
    Returns:
        Prompt messages for cash flow forecasting.
    """
    assistant_msg = Message(
        role="assistant",
        content="""I'll create cash flow forecasts using Pennylane data.

I consider:
1. Receivables collection patterns
2. Payables payment schedules
3. Recurring revenues and expenses
4. Seasonal variations
5. One-time items
6. Credit terms and payment history

Forecast components:
- Opening cash balance
- Operating cash flows (in/out)
- Investing activities
- Financing activities
- Closing cash balance

I include timing of cash movements, not just accrual accounting.

Let me prepare your cash flow forecast."""
    )
    
    user_content = f"""Create a cash flow forecast for {forecast_period}."""
    
    if key_assumptions:
        user_content += f"\n\nKey assumptions:\n{key_assumptions}"
    
    if include_scenarios:
        user_content += "\n\nInclude best case, expected, and worst case scenarios."
    
    user_content += """

The forecast should show:
1. Weekly or monthly cash positions
2. Major inflows by source
3. Major outflows by category
4. Minimum/maximum cash positions
5. Any financing needs identified
6. Key risks to cash flow
7. Recommendations for optimization

Highlight:
- Potential cash shortfalls
- Excess cash for investment
- Working capital improvements
- Collection/payment optimizations"""
    
    return [assistant_msg, Message(role="user", content=user_content)] 