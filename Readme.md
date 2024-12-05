# Loan Counselor Agent

This project is a Flask-based REST API for a loan counseling chatbot that helps students understand their loan options. It leverages AI models to provide personalized loan recommendations and maintain contextual conversations with students.

## Features

- **Chat Endpoint**: Converse with the loan counselor to get loan recommendations.
- **Request Validation**: Ensures all necessary student information is provided.
- **Conversation Memory**: Maintains context across interactions.
- **Error Handling**: Robust error handling and logging.
- **CORS Support**: Allows cross-origin requests.
- **Asynchronous Processing**: Utilizes thread pools for efficient request handling.

## Setup

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rishabh250/loan-counselor-agent.git
   cd loan-counselor-agent
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add the necessary environment variables, such as `FLASK_SECRET_KEY`, `OPENAI_API_KEY`, etc.

### Running the Application

1. Start the Flask application:
   ```bash
   python wsgi.py
   ```

2. The application will be available at `http://0.0.0.0:8000`.

## Usage

- **Chat with the Loan Counselor**: Send POST requests to `/chat` with the required student details to receive loan recommendations.
- **Reset Conversation**: Send POST requests to `/reset` to clear conversation history.

## API Endpoints

- **POST /chat**: Interact with the loan counselor.
- **POST /reset**: Reset the conversation memory for a user.

## Project Structure

- **app.py**: Main application file.
- **wsgi.py**: WSGI configuration for running the app.
- **vector_store/**: Contains modules for storing and retrieving vector-based data.
- **utils/**: Utility modules and constants.
- **helpers.py**: Helper functions for formatting data.
- **prompts.py**: Contains prompt templates for AI interactions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License.