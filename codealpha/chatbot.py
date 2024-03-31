
import nltk
from nltk.chat.util import Chat, reflections#reflections is a dictionary containing reflection pairs for transforming input phrases.
#The Chat class is used to create the chatbot.
# Define patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hey there!", "Hi, how can I help you?"]),
    (r"good morning" ,["GOOD MORNING !!!! May you have a,bright morning "]),
    (r"how to became rich",["TO become rich and successul ,hard work is the key to the success!"]),
    (r"I love you|I like you",["Thank you for your kind words! As a chatbot, I'm here to assist you "]),
    (r"(.*)what is your name? (.*)", ["I'm just a chatbot.", "You can call me Chatooooo."]),
    (r"how are you?", ["I'm just a program, so I don't have feelings, but thanks for asking!"]),
    (r"will marry me|would you become my bf | hello jaan",["As an AI chatbot, I don't have personal feelings or the capability to marry. However, I'm here to assist you with any questions or tasks you have. Is there anything else I can help you with? "]),
    (r"(.*) (age|old) are you?", ["I'm just a computer program, so I don't have an age."]),
    (r"(.*) (your name|who are you)", ["I'm a chatbot created to assist you.", "I'm Chatbot, your virtual assistant."]),
    (r"(.*) help (.*)", ["Sure, I'd be happy to help. What do you need assistance with?"]),
    (r"(.*) (weather|forecast) (.*)", ["I'm sorry, I don't have access to weather information."]),
    (r"(.*) (goodbye|bye)", ["Goodbye!", "Bye! Have a great day!"]),
    (r"quit", ["Goodbye!", "Bye! Take care!"])
]

# Create a chatbot instance
chatbot = Chat(patterns, reflections)

# Define a function to start the chat
def start_chat():
    print("Hello! I'm a text-based chatbot. You can ask me anything or just say hi!")

    # Start the conversation
    while True:
        user_input = input("You: ").lower()
        response = chatbot.respond(user_input)
        print("Chatbot:", response)

        # Check if the user wants to quit
        if user_input.lower() == 'quit':
            break

# Call the function to start the chat
if __name__ == "__main__":
    start_chat()
