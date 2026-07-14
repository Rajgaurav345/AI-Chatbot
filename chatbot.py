import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer (only first time)
nltk.download('punkt')

responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello there!",
    "bye": "Goodbye! Have a nice day!",
    "name": "I'm a simple AI Chatbot.",
    "python": "Python is a popular programming language.",
    "help": "Sure! Ask me anything related to Python or greetings."
}

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())

    for token in tokens:
        if token in responses:
            return responses[token]

    return "Sorry, I don't understand that."
