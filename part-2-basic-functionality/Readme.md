# Part 2: Basic Functionality

This part introduces the core functionality of the Loan Counselor Agent.

## Objectives
- Implement basic loan counseling features.
- Set up helper functions and prompts.

## Setup Instructions

1. **Ensure Part 1 Setup is Complete**.

2. **Navigate to Part 2 Directory**:
   ```bash
   cd loan-counselor-agent/part-2-basic-functionality
   ```

3. **Run the Application**:
   ```bash
   python app.py
   ```

## Development Tasks

1. **Implement Helper Functions**:
   - Create functions in `helpers.py` to format lender data.

2. **Set Up Prompts**:
   - Define initial prompts in `prompts.py` for the loan counselor.

3. **Test the `/chat` Endpoint**:
   - Use a tool like Postman to send POST requests to `/chat` with a message payload.

## Troubleshooting

- Ensure `loan_counselor_agent.py` is in the same directory as `app.py`.
- Adjust import paths if necessary to resolve import errors. 