import nltk
from nltk.tokenize import word_tokenize

# Ensure that the necessary NLTK resources are downloaded
nltk.download('punkt')

def process_input(user_input):
    """
    Tokenizes the user input into words.

    Args:
        user_input (str): The input string from the user.

    Returns:
        list: A list of tokens (words) from the input string.
    """
    # Tokenize the input and convert to lowercase
    tokens = word_tokenize(user_input.lower())
    return tokens
