import random
from nlp_module import process_input  # Ensure this module is correctly implemented

def get_response(user_input):
    # Process the user input through the NLP module
    tokens = process_input(user_input)
    
    # Define a list of general responses
    responses = [
        "I'm here to listen. How can I support you?",
        "Remember, taking deep breaths can sometimes help. What’s on your mind?",
        "It’s okay to feel this way. Want to talk about it more?",
    ]
    
    # Example simple response based on token analysis
    if "anxiety" in tokens:
        return "I'm here for you. Let's take it one step at a time."
    
    # Return a random response if no specific keywords are found
    return random.choice(responses)

# Optional: A main block for testing the function directly
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = get_response(user_input)
        print(f"Bot: {response}")
