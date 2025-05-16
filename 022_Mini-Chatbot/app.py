def chatbot_response(user_input):
    user_input = user_input.lower()
    responses = {
        "hi" : "Hello there!",
        "how are you": "i'm good, thank you! How about you?",
        "what's your name": "I am a simple chatbot.",
        "thank you": "You're welcome!",
        "goodbye": "See you later!"
    }
    return responses.get(user_input, "Sorry, I don't understand that.")

def main():
    print("Simple Chatbot, type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot_response(user_input)
        print("Chatbot:", response)

if __name__ == "__main__":
    main()