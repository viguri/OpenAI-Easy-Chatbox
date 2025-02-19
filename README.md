# OpenAI Easy Chatbox

A simple web application that implements a chatbox using the OpenAI API. The project is built with Flask and allows users to interact with OpenAI's GPT-3.5-turbo model through a simple web interface.

## Project Structure

```
├── .env                  # Environment variables file (API key)
├── app.py               # Backend API server
├── web.py              # Frontend server
├── templates/
│   └── index.html      # User interface
└── README.md           # This documentation
```

## Features

- Simple and responsive web interface
- OpenAI GPT-3.5-turbo integration
- Separated backend/frontend architecture
- Error handling and input validation
- Environment variables support

## Requirements

- Python 3.x
- Flask
- OpenAI Python SDK
- Requests
- Configured environment variables (.env)

## Setup

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install flask openai requests python-dotenv
```

2. Create a `.env` file in the project root:

```
OPENAI_API_KEY=your-openai-api-key
```

## Usage

1. Activate the virtual environment:

```bash
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Start the backend server (API):

```bash
python app.py
```

3. In another terminal (with virtual environment activated), start the frontend server:

```bash
python web.py
```

4. Open your browser and visit `http://localhost:5001`

## API Endpoints

### Backend (app.py - port 5000)

- `GET /`: Welcome message
- `POST /chat`: Endpoint to process messages
  - Body: `{"message": "your message here"}`
  - Response: `{"response": "assistant's response"}`

### Frontend (web.py - port 5001)

- `GET /`: Chatbox web interface
- `POST /send_message`: Endpoint to send messages to backend

## Common Troubleshooting

### JSONDecodeError

If you receive a `JSONDecodeError: Expecting value: line 1 column 1 (char 0)`, verify:

1. That both servers (backend and frontend) are running:

   - Backend on port 5000 (app.py)
   - Frontend on port 5001 (web.py)

2. That the OPENAI_API_KEY variable is correctly configured in the .env file

3. That you're using the virtual environment with all dependencies installed

4. Test the backend directly with curl:

```bash
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message":"Hello"}'
```

## Development Notes

- Backend uses Flask to serve the REST API
- Frontend uses Flask to serve the web interface
- Communication between frontend and backend is done via HTTP requests
- Web interface uses vanilla JavaScript for interactions
- Messages and responses are shown in a scrollable container

## Installation Verification

To verify that everything is correctly configured:

1. Verify that the backend responds:

```bash
curl http://localhost:5000/
# Should return: "Welcome to the Chat API!"
```

2. Verify that the API key is configured:

```bash
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENAI_API_KEY'))"
# Should show your API key
```
