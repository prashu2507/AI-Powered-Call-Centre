# AI-Powered Call Centre for Students

## Overview
The **AI-Powered Call Centre for Students** is a chatbot designed to assist students with various academic tasks. It provides reminders for assignments, tests, and other academic activities, helping students stay organized and on top of their schedules. The chatbot leverages AI to deliver personalized responses and automate student support.

## Features
- **Assignment & Test Reminders**: Sends notifications about upcoming assignments and tests.
- **Class Schedule Management**: Provides details on class timings and schedules.
- **Query Resolution**: Answers students' questions related to coursework, exams, and other academic concerns.
- **Real-time Assistance**: Supports students by offering instant responses to their inquiries.
- **Multi-Channel Support**: Can be integrated with platforms like WhatsApp, Telegram, or a web-based chatbot interface.
- **Personalized Notifications**: Reminds students based on their course schedules.

## Technologies Used
- **Backend**: Flask (Python) with LangChain and LangSmith for AI-driven responses.
- **Frontend**: HTML, CSS, JavaScript (if using a web-based UI).
- **Database**: MySQL or Firebase (for storing schedules and reminders).
- **AI Model**: Google Generative AI model for contextual responses.

## Installation
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-repo/AI-Powered-Call-Centre.git
   cd AI-Powered-Call-Centre
   ```
2. **Set Up Virtual Environment** (Optional but recommended)
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Database**
   - Configure MySQL or Firebase.
   - Import the schema provided in `database.sql`.
5. **Run the Application**
   ```sh
   python app.py
   ```

## Usage
- Students can interact with the chatbot via text or voice commands.
- The chatbot fetches schedules and due dates from the database.
- Notifications are sent based on pre-set schedules.
- AI-powered responses help answer queries efficiently.

## Future Enhancements
- Integration with Google Calendar for better scheduling.
- Voice-based assistance for a more interactive experience.
- Mobile app integration for push notifications.
- Improved AI model for better contextual understanding.

## Contributors
- Vegi Prasanthi
- Deepali Sanchan
## License
This project is licensed under the MIT License.

---
For any issues or contributions, feel free to open an issue on the GitHub repository!

