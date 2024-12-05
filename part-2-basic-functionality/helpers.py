def format_lenders_data(lenders):
    formatted_data = []
    for lender in lenders:
        lender_info = (
            f"{lender['name']}:\n"
            f"- Interest Rate: {lender['interest_rate']}\n"
            f"- Maximum Amount: {lender['maximum_amount']}\n"
        )
        formatted_data.append(lender_info)
    return "\n\n".join(formatted_data)
