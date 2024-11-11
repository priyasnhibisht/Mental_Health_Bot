import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load conversations from JSON file
def load_conversations():
    try:
        with open('conversations.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save conversations to JSON file
def save_conversations(conversations):
    with open('conversations.json', 'w') as f:
        json.dump(conversations, f, indent=4)  # Use indent for pretty printing

# Load existing conversations
conversations = load_conversations()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('user_input')
    bot_response = f"Bot response to: {user_input}"  # Replace with your bot logic
    conversations.append({'user_input': user_input, 'bot_response': bot_response})
    save_conversations(conversations)
    return jsonify({'bot_response': bot_response})

@app.route('/conversations', methods=['GET'])
def get_conversations():
    return jsonify(conversations)

if __name__ == '__main__':
    app.run(debug=True)  # Set debug=True for development
