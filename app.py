# curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "Hello, world!"}'
from flask import Flask, request, jsonify 
import os
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise RuntimeError("OPENAI_API_KEY not found in environment variables")

client = OpenAI(api_key=api_key)

app = Flask(__name__)

# Root route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Chat API!"})

# Chatbox route
@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({"error": "Invalid input: 'message' field is required"}), 400
        
        user_message = data['message']
        
        if not isinstance(user_message, str) or not user_message.strip():
            return jsonify({"error": "Invalid input: message must be a non-empty string"}), 400

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {'role': 'system', 'content': 'You are a helpful assistant.'},
                {'role': 'user', 'content': user_message}
            ],
            max_tokens=150
        )
        
        assistant_message = response.choices[0].message.content.strip()
        return jsonify({"response": assistant_message})
        
    except OpenAIError as e:
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)