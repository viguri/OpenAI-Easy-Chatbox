from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        user_message = request.form['message']
        # Convert form data to JSON for the API request
        response = requests.post(
            'http://127.0.0.1:5000/chat',
            headers={'Content-Type': 'application/json'},
            json={"message": user_message},
            timeout=30  # Add timeout
        )
        # Check if the response is successful
        response.raise_for_status()
        # Try to parse JSON response
        try:
            return jsonify(response.json())
        except requests.exceptions.JSONDecodeError:
            return jsonify({"error": "Invalid response from chat server"}), 500
            
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Failed to communicate with chat server: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)