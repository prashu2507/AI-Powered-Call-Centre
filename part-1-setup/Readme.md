# Part 1: Setup

This part focuses on setting up the environment for the Loan Counselor Agent project.

## Objectives
- Set up the Python environment.
- Install necessary dependencies.
- Run a basic Flask application.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rishabh250/loan-counselor-agent.git
   cd loan-counselor-agent/part-1-setup
   ```

2. **Create a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

## Troubleshooting

- Ensure that `app.py` and `wsgi.py` are in the same directory.
- If you encounter import errors, check the file paths and adjust the import statements accordingly. 