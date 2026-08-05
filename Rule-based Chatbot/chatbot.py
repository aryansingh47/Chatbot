# Import the required modules
import random
from datetime import datetime


def get_bot_response(user_message, user_name):

    # Convert the message to lowercase and remove extra spaces, for ease of matching the user messages
    message = user_message.lower().strip()

    # Respond to greetings
    if message in ["hello", "hi", "hey", "good morning", "good evening"]:
        greetings = [
            "Hello! How can I help you?",
            "Hi there! How are you?",
            "Hiya! What would you like to talk about?"
        ]

        # Choose a random greeting from the list
        return random.choice(greetings), user_name

    # Ask the user for their name
    elif message in ["what is my name?", "do you know my name?"]:
        if user_name:
            return f"Your name is {user_name}.", user_name
        else:
            return "I don't know your name yet. You can say: My name is Aryan.", user_name

    # Detect messages such as "My name is Aryan"
    elif message.startswith("my name is "):
        # Extract the name from the original message
        name = user_message[11:].strip().title()

        if name:
            return f"Nice to meet you, {name}!", name
        else:
            return "Please tell me your name.", user_name

    # Respond when the user asks for the chatbot's name
    elif message in [
        "what is your name?",
        "what's your name?",
        "who are you?"
    ]:
        return "My name is BotBot. I am your personal chatbot.", user_name

    # Respond to questions about how the chatbot is feeling
    elif message in [
        "how are you?",
        "how are you",
        "how are you doing?"
    ]:
        responses = [
            "I'm doing well, thank you for asking mate!",
            "I'm great! Cheers for asking.",
            "I'm functioning perfectly. How are you?"
        ]

        return random.choice(responses), user_name

    # Respond when the user says they are doing well
    elif message in ["i am good", "i'm good", "i am fine", "i'm fine"]:
        return "That's very good to hear!", user_name

    # Respond when the user says they are unhappy
    elif message in ["i am sad", "i'm sad", "i feel bad", "not good"]:
        return "I'm sorry to hear that. I hope things get better soon mate.", user_name

    # Tell the current time
    elif "time" in message:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}.", user_name

    # Tell the current date
    elif "date" in message or "day is it" in message:
        current_date = datetime.now().strftime("%A, %d %B %Y")
        return f"Today is {current_date}.", user_name

    # Respond to questions about the chatbot's abilities
    elif message in [
        "what can you do?",
        "what do you do?",
        "help"
    ]:
        response = (
            "I can greet you, remember your name, tell you the date and time, "
            "and respond to some basic conversational messages."
        )
        return response, user_name

    # Respond to expressions of gratitude
    elif message in ["thank you", "thanks", "thank you so much"]:
        return "You're welcome!", user_name

    # Handle goodbye messages
    elif message in ["bye", "goodbye", "exit", "quit"]:
        if user_name:
            return f"Goodbye, {user_name}! I hope you have a great day.", user_name
        else:
            return "Goodbye! Have a great day.", user_name

    # Default response for messages the chatbot does not understand
    else:
        unknown_responses = [
            "I'm sorry, I don't understand that.",
            "Could you please say that differently?",
            "I'm still learning. Could you ask me something else?",
            "I don't have a response for that yet."
        ]

        return random.choice(unknown_responses), user_name


def run_chatbot():

    # Store the user's name.
    # Initially, the chatbot does not know the user's name.
    user_name = None

    print("-" * 50)
    print("BotBot: Hello! I am Botbot.")
    print("BotBot: Type 'bye', 'exit', or 'quit' to end the chat.")
    print("-" * 50)

    # Keep the chatbot running until the user chooses to exit
    while True:
        # Get a message from the user
        user_message = input("You: ")

        # Prevent the user from submitting an empty message
        if not user_message.strip():
            print("BotBot: Please enter a message.")
            continue

        # Generate the chatbot's response
        bot_response, user_name = get_bot_response(
            user_message,
            user_name
        )

        # Display the response
        print(f"BotBot: {bot_response}")

        # End the loop when the user enters an exit message
        if user_message.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            break

if __name__ == "__main__":
    run_chatbot()
