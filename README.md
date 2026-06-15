# 🤖 DecoBot — Rule-Based AI Chatbot

> I am a law student in Nigeria teaching myself AI Engineering.
> This is Project 1 of my DecodeLabs internship 

---

## 🎯 What is DecoBot?

DecoBot is a rule-based AI chatbot built entirely from scratch 
using Python — no frameworks, no APIs, no pre-built chatbot tools.

It responds to user inputs using a dictionary knowledge base,
input sanitization, and control flow logic — the same 
architectural pattern used by enterprise AI guardrail systems
like NVIDIA NeMo and Meta's Llama Guard.

---

## ✅ Key Features

- Handles greetings and natural conversation
- Sanitizes user input — removes capitals, spaces and punctuation
- Uses dictionary O(1) lookup — faster than IF-ELIF chains
- Runs in a continuous loop until user exits
- Returns intelligent fallback for unknown inputs
- Exits cleanly with a goodbye message

---

## 💬 Demo

Bot: Hello! I am DecoBot. Type 'quit' to exit.
You: HELLO

Bot: Hi there! How can I help you?
You: what can you do?

Bot: I can answer your questions!
You: who made you

Bot: I was built by Umoekam at DecodeLabs!
You: weather

Bot: I don't understand that.
You: quit

Bot: Goodbye! See you later!


##  The Complete Code

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



## 🧠 Architecture — The White Box

DecoBot is a **White Box AI system** — every decision is 
fully traceable:

No mystery. No hallucination. No black box.
Input → Logic → Output. Always.

---

## 💡 Why Dictionary Over IF-ELIF?

| Approach | Speed | Scalability | Maintainability |
|----------|-------|-------------|-----------------|
| IF-ELIF Ladder | O(n) — slows down | Gets worse | Hard to update |
| Dictionary | O(1) — instant | Stays fast forever | Add one line |

A dictionary is a Hash Map — it finds answers in constant 
time regardless of how many responses you add.
That's why DecodeLabs called it the professional approach.

---

## 💡 What I Learned — Including My Mistakes

Building DecoBot taught me the difference between rule-based 
AI and generative AI.

Rule-based systems like DecoBot are called **White Box AI** —
every decision is traceable and explainable.
Systems like ChatGPT are **Black Box AI** — even their 
creators can't fully trace every decision.

Banks and hospitals legally require White Box AI because 
lives and money depend on explainability.

I also learned that using IF-ELIF for every response — 
what engineers call an Anti-Pattern — creates an unstable 
tower of conditions that gets slower with every rule added.
The dictionary solution was cleaner, faster and more 
professional from day one.

---

## ⚠️ Critical Rule — Input Sanitization

```python
# Without sanitization — chatbot fails
"HELLO" → not found in dictionary → "I don't understand"

# With sanitization — chatbot works perfectly  
"HELLO" → .lower() → "hello" → found! → "Hi there!"
"hello " → .strip() → "hello" → found! → "Hi there!"
"hello?" → .replace() → "hello" → found! → "Hi there!"
```

Sanitization is Phase 1 of every professional AI pipeline —
the same concept used in enterprise NLP systems worldwide.

---

## 🏗️ Project Specifications Met

| Requirement | Status |
|-------------|--------|
| Handle greetings and exit commands | ✅ |
| Use if-else logic for responses | ✅ |
| Run in a continuous loop | ✅ |
| Dictionary with 5+ intents | ✅ 9 intents |
| Input sanitization | ✅ |
| Fallback for unknown inputs | ✅ |
| Clean exit command | ✅ |

---

## 🛠️ Technologies Used
- Python 3
- PyCharm IDE
- No external libraries — pure Python only

---

## 🚀 How to Run

1. Clone this repository
2. No installations needed — pure Python
3. Run:

4. Start chatting!

---

## 📁 Project Structure

decobot-chatbot/

│

├── decobot.py    # Complete chatbot code

├── README.md     # This file

---


## 👨‍💻 About Me
**Torobong Umoekam Edet**
AI Engineering Intern at DecodeLabs | AI Automation Specialist
Python | Machine Learning | n8n | Make.com | Zapier
📧 umoekampraise@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/torobong-umoekam-32b0b2291
