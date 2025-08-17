# chatbot.py

def chatbot():
    print("🤖 Hi! I'm ChatBot. Type 'exit' to end the chat.")
    while True:
        user_input = input("You: ").lower()  # take input in lowercase

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello! How are you doing today?")

        elif user_input in ["i am good", "i am fine", "fine", "good"]:
            print("Bot: That's great to hear! 😊")

        elif user_input in ["who are you", "what are you"]:
            print("Bot: I'm a simple rule-based chatbot built using Python if-else statements.")

        elif user_input in ["what can you do", "your purpose"]:
            print("Bot: I can chat with you and answer some simple questions!")

        elif "your name" in user_input:
            print("Bot: I'm ChatBot, your virtual assistant.")

        elif "bye" in user_input or user_input == "exit":
            print("Bot: Goodbye! Have a nice day 👋")
            break

        else:
            print("Bot: Sorry, I didn't understand that. Can you rephrase?")

if __name__ == "__main__":
    chatbot()
