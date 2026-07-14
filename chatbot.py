import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer (only first time)
nltk.download('punkt')

responses = {
    ("hello", "hi", "hey"): "Hello! How can I help you?",
    ("bye", "goodbye"): "Goodbye! Have a nice day!",
    ("python", "programming"): "Python is a popular programming language.",
    ("help",): "Sure! Ask me something."
}

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())

    for words, response in responses.items():
        if any(word in tokens for word in words):
            return response

    return "Sorry, I don't understand that."
