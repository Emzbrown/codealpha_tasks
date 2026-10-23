def get_bot_response(user_input: str) -> str:
    """
    Takes user input, converts it to lowercase, and returns a predefined response.
    """
    # Normalize input by removing extra spaces and converting to lowercase
    cleaned_input = user_input.strip().lower()

    # Rule-based matching logic
    if cleaned_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you today?"

    elif cleaned_input in ["how are you", "how are you?", "how's it going"]:
        return "I'm doing great, thanks for asking! How are you?"

    elif cleaned_input in ["what is your name", "what's your name", "who are you"]:
        return "I am EmzyBot, a simple Python chatbot!"

    elif cleaned_input in ["bye", "goodbye", "exit", "quit"]:
        return "Goodbye! Have a great day!"

    else:
        return "I'm sorry, I don't understand that yet. Try saying 'hello', 'how are you', or 'bye'."


def run_chatbot():
    """
    Main loop to run the interactive chatbot terminal session.
    """
    print("==========================================")
    print("      Welcome to EmzyBot Terminal!        ")
    print(" Type 'bye' or 'exit' at any time to quit. ")
    print("==========================================\n")

    while True:
        # Take input from the user
        user_message = input("You: ")

        # Get response from the bot logic function
        bot_response = get_bot_response(user_message)

        # Print the bot's response
        print(f"Bot: {bot_response}\n")

        # Exit loop if user says goodbye
        if user_message.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break


# Run the chatbot program
if __name__ == "__main__":
    run_chatbot()
