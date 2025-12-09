import nltk
from nltk.chat.util import Chat, reflections

# Download required NLTK data (only first time)
nltk.download('punkt')

# ---- CHATBOT TRAINING DATA ----
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you today?", "Hi there! Ask me anything."]
    ],
    [
        r"what is your name?",
        ["I am an NLP Chatbot created for CODTECH Internship Task 3."]
    ],
    [
        r"how are you?",
        ["I'm functioning as expected! How about you?",
         "Doing great, thank you!"]
    ],
    [
        r"what is nlp?",
        ["NLP stands for Natural Language Processing. It helps computers understand human language."]
    ],
    [
        r"who created you?",
        ["I was built using Python and NLTK as a Task-3 project."]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye! Have a great day!", "Bye! Visit again :)"]
    ],
]

# ---- CREATE CHATBOT ----
def chatbot():
    print("CODTECH NLP Chatbot is now running...")
    print("Type 'bye' or 'quit' to exit.\n")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()