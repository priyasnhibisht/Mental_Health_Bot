from flask import Flask, request, jsonify
from chatbot import get_response
import sqlite3
import datetime

app = Flask(__name__)

# Initialize the database
def init_db():
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations 
                 (id INTEGER PRIMARY KEY, user_input TEXT, bot_response TEXT, timestamp TEXT)''')
    conn.commit()
    conn.close()

# Log conversation
def log_conversation(user_input, bot_response):
    conn = sqlite3.connect('chatbot.db')
    c = conn.cursor()
    c.execute("INSERT INTO conversations (user_input, bot_response, timestamp) VALUES (?, ?, ?)",
              (user_input, bot_response, datetime.datetime.now().isoformat()))
    conn.commit()
    conn.close()

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    log_conversation(user_input, response)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
