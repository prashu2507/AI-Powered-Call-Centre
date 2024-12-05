"""
This module contains helper functions for formatting and displaying loan-related data
to students in a clear and understandable way.
"""

from typing import Any, Dict, List

def format_lenders_data(lenders: List[Dict[str, Any]]) -> str:
    """
    Format loan provider information into a student-friendly display format.
    
    This function takes raw lender data and formats it into an easy-to-read string
    that shows important loan details like:
    - Interest rates and maximum loan amounts
    - Key features and requirements
    - Collateral and cosigner requirements
    - Geographic availability and currency
    
    Args:
        lenders: List of dictionaries containing lender information
                Each dictionary should have fields for name, interest rate,
                maximum amount, etc.
    
    Returns:
        A formatted string containing all lender information, with each lender
        separated by newlines
    """
    formatted_data = []
    for lender in lenders:
        lender_info = (
            f"{lender['name']}:\n"
            f"- Interest Rate: {lender['interest_rate']}\n"
            f"- Maximum Amount: {lender['maximum_amount']}\n"
            f"- About: {lender['about']}\n"
            f"- Key Points: {', '.join(lender['key_points'])}\n"
            f"- Currency: {lender['currency']}\n"
            f"- Collateral Required: {lender['collateral_required']}\n"
            f"- Non-Collateral Option: {lender['non_collateral_option']}\n"
            f"- US Cosigner Required: {lender['us_cosigner_required']}\n"
            f"- Country: {lender['country']}\n"
            f"- University Country: {lender['university_country']}"
        )
        formatted_data.append(lender_info)
    return "\n\n".join(formatted_data)
