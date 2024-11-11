import os
import psycopg2
from psycopg2 import sql

# Get the database URL from environment variables
DATABASE_URL = os.environ.get('DATABASE_URL')

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS conversations
                 (user_input TEXT, bot_response TEXT)''')
    conn.commit()
    c.close()
    conn.close()

def save_conversation(user_input, bot_response):
    conn = psycopg2.connect(DATABASE_URL)
    c = conn.cursor()
    c.execute("INSERT INTO conversations (user_input, bot_response) VALUES (%s, %s)", 
              (user_input, bot_response))
    conn.commit()
    c.close()
    conn.close()

# Initialize the database
init_db()
