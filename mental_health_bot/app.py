import os
import logging
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up logging
logging.basicConfig(level=logging.INFO)

# Get the port from the environment variable (set by Glitch)
PORT = int(os.environ.get("PORT", 3000))

@app.route('/')
def home():
    return render_template('index.html')  # Ensure you have an index.html in the templates folder

@app.route('/chat', methods=['POST'])
def chat():
    try:
        user_input = request.json.get('user_input')
        if not user_input:
            return jsonify({'error': 'User  input is required.'}), 400
        
        app.logger.info(f"User  input: {user_input}")
        
        # Here you would typically call your NLP model or chatbot logic
        bot_response = generate_bot_response(user_input)  # Call to a function that processes the input
        return jsonify({'bot_response': bot_response})

    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request.'}), 500

def generate_bot_response(user_input):
    # Placeholder for chatbot logic
    # You can integrate your NLP model or any logic here
    return f"Bot response to: {user_input}"

# This block ensures the app runs when executed directly
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)  # Ensure it listens on the correct port
    
if __name__ == '__main__':
    app.run(debug=True)
