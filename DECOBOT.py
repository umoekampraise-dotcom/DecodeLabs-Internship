

responses = {
    "hello": "Hi there! How can I help you?",
    "bye": "Goodbye! Have a great day",
    "name": "My name is DecoBot!",
    "help": "Sure! What do you need help with? You can ask me about my name, age, who made me, what I can do?, etc",
    "age": "I was created in 2026",
    "how are you": "I am doing great, thank you for asking!",
    "who made you": "I was built by Torobong in Decode labs!",
    "what can you do": "I can answer your questions!",
    "thanks": "You're welcome!",
    "good morning": "Good morning! How are you today?"
}

print("Bot: Hello! I am DecoBot. Type 'quit' to exit.")

while True:
    user_input = input("You: ")
    clean_input = user_input.lower().strip().replace("?" ,"").replace("!","")

    if clean_input =="quit":
        print("Bot: Goodbye! See you later!")
        break

    reply = responses.get(clean_input, "Sorry,I don't understand that yet. Try 'help' to see what I can do")
    print("Bot:", reply)