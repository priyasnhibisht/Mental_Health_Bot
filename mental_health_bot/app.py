import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Placeholder for conversation storage
conversations = []

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    
    if not user_input:
        return jsonify({'error': 'User  input is required.'}), 400
    
    bot_response = f"Bot response to: {user_input}"  # Replace with your bot logic
    conversations.append({'user_input': user_input, 'bot_response': bot_response})

    # Here you would save conversations to a database instead of a file
    # save_conversations_to_db(conversations)  # Example function call

    return jsonify({'bot_response': bot_response})

@app.route('/conversations', methods=['GET'])
def get_conversations():
    return jsonify(conversations)
