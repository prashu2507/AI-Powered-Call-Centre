from flask import Flask, request, jsonify
from flask_cors import CORS
from loan_counselor_agent import LoanCounselorAgent

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.json
        agent = LoanCounselorAgent()
        response = agent.handle_message(data['message'])
        return jsonify(response)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8000)
