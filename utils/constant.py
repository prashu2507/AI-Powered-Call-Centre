"""
This module contains constants used in the application.
"""

LENDER_DATA = [{
                "name": "HDFC Credila",
                "interest_rate": "10.0% - 12.0%",
                "maximum_amount": "INR 10,000,000",
                "about": "HDFC Credila is a trusted non-banking financial institution, offering a range of customizable loan options to meet the diverse needs of its customers.",
                "key_points": [
                    "Processing fee up to 1% + GST",
                    "Tenure up to 10 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "Any"
            },
            {
                "name": "IDFC",
                "interest_rate": "10.15% - 12.0%",
                "maximum_amount": "INR 10,000,000",
                "about": "IDFC Bank is here to provide you with flexible loans that suit your requirements.",
                "key_points": [
                    "Processing fee up to 1% + GST",
                    "Tenure up to 12 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "Any"
            },
            {
                "name": "ICICI",
                "interest_rate": "10.5% - 12.0%",
                "maximum_amount": "INR 20,000,000",
                "about": "ICICI is committed to offering loan solutions customized just for you.",
                "key_points": [
                    "Processing fee up to 1% + GST",
                    "Tenure up to 10 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "Any"
            },
            {
                "name": "SBI",
                "interest_rate": "9.15% - 12.0%",
                "maximum_amount": "INR 15,000,000",
                "about": "SBI is here to serve you, with a focus on personalized loan solutions for your educational and career objectives.",
                "key_points": [
                    "Processing fee Rs 10,000 + GST",
                    "Tenure up to 15 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": False,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "Any"
            },
            {
                "name": "Union Bank of India",
                "interest_rate": "9.8% - 12.0%",
                "maximum_amount": "INR 15,000,000",
                "about": "UBI is committed to being your guide, creating customized loan solutions for your education and career journey.",
                "key_points": [
                    "Processing fee up to Rs 5,000 + GST",
                    "Tenure up to 15 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "Any"
            },
            {
                "name": "Avanse",
                "interest_rate": "11.5% - 12.0%",
                "maximum_amount": "INR 7,500,000",
                "about": "Avanse is known for its commitment to crafting adjustable loan options.",
                "key_points": [
                    "Processing fee up to 1%",
                    "Tenure up to 15 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "USA, Canada"
            },
            {
                "name": "Auxilo",
                "interest_rate": "11.25% - 12.0%",
                "maximum_amount": "INR 7,000,000",
                "about": "Auxilo Finserve Pvt. Ltd. is a trusted and reliable non-banking financial institution, dedicated to providing education loans to students in need.",
                "key_points": [
                    "Processing fee up to 1.5%",
                    "Tenure up to 10 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "USA, Canada, UK"
            },
            {
                "name": "Sallie Mae",
                "interest_rate": "4.15% - 15.6%",
                "maximum_amount": "100% of school-certified expenses (USD)",
                "about": "Sallie Mae is a 'US-based' powerhouse education solution company offering education financing products and resources to help students in their higher education dream big.",
                "key_points": [
                    "No origination fee",
                    "Tenure varies"
                ],
                "currency": "USD",
                "collateral_required": False,
                "non_collateral_option": True,
                "us_cosigner_required": True,
                "country": "USA",
                "university_country": "USA"
            },
            {
                "name": "Prodigy",
                "interest_rate": "13.99% - 12.0%",
                "maximum_amount": "USD 100,000",
                "about": "Prodigy is a trusted financial institution, personalized loan solutions.",
                "key_points": [
                    "Processing fee up to 5% + GST",
                    "Tenure up to 10 years"
                ],
                "currency": "USD",
                "collateral_required": False,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "USA, Canada, UK, Australia, Germany",
                "university_country": "USA, Canada, UK, Australia, Germany"
            },
            {
                "name": "Tata Capital",
                "interest_rate": "11.75% - 12.0%",
                "maximum_amount": "INR 6,500,000",
                "about": "Tata Capital is a leading financial services provider, offering competitive interest rates and maximum flexibility.",
                "key_points": [
                    "Processing fee up to 1.5% + GST",
                    "Tenure up to 10 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "Any"
            },
            {
                "name": "Axis Bank",
                "interest_rate": "10.5%",
                "maximum_amount": "INR 20,000,000",
                "about": "Finance your studies abroad with Axis Bank's flexible loan amounts, quick disbursals and tax exemptions.",
                "key_points": [
                    "Processing fee up to 1% + GST",
                    "Tenure up to 10 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "Any"
            },
            {
                "name": "Incred",
                "interest_rate": "11.25%",
                "maximum_amount": "INR 10,000,000",
                "about": "Invest in your education without worries, with Incred's wide range of loans covering 100% of your tuition fees*.",
                "key_points": [
                    "Processing fee up to 1.5% + GST",
                    "Tenure up to 12 years"
                ],
                "currency": "INR",
                "collateral_required": True,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "India",
                "university_country": "Any"
            },
            {
                "name": "Ascent",
                "interest_rate": "3.79% - 9.9%",
                "maximum_amount": "USD 400,000",
                "about": "Ascent is a trusted financial institution, committed to providing customizable loan solutions.",
                "key_points": [
                    "0% processing fee",
                    "Tenure up to 10 years"
                ],
                "currency": "USD",
                "collateral_required": False,
                "non_collateral_option": True,
                "us_cosigner_required": True,
                "country": "USA",
                "university_country": "USA"
            },
            {
                "name": "Earnest",
                "interest_rate": "4.25% - 9.0%",
                "maximum_amount": "USD 250,000",
                "about": "Earnest is a renowned US non-banking financial institution that provides flexible and personalized loans.",
                "key_points": [
                    "0% processing fee",
                    "Tenure up to 10 years"
                ],
                "currency": "USD",
                "collateral_required": False,
                "non_collateral_option": True,
                "us_cosigner_required": False,
                "country": "USA",
                "university_country": "USA"
            }
        ]