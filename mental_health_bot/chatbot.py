import random
from nlp_module import process_input

def get_response(user_input):
    tokens = process_input(user_input)
    responses = [
        "I'm here to listen. How can I support you?",
        "Remember, taking deep breaths can sometimes help. What’s on your mind?",
        "It’s okay to feel this way. Want to talk about it more?",
    ]
    
    # Example simple response based on token analysis
    if "anxiety" in tokens:
        return "I'm here for you. Let's take it one step at a time."
    return random.choice(responses)
