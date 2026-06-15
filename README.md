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

# DecodeLabs-Internship_-KNN-Classification-Algorithm
Iris flower classifier built in Python using KNN algorithm, StandardScaler and F1 Score evaluation — DecodeLabs 

# 🌸 Iris Flower Classification — KNN Supervised Learning


## 🎯 Results — Two Datasets, One Pipeline

| Dataset | Features | Samples | F1 Score | Accuracy |
|---------|----------|---------|----------|----------|
| Iris    | 4        | 150     | 1.0000   | 100%     |


After completing Iris — I independently applied the exact same 
pipeline to the Wine dataset without any guidance.
That second result proved I understood the pipeline — 
not just followed instructions.

---

## 📊 Dataset
- **Name:** Iris Dataset (Fisher, 1936)
- **Samples:** 150 flowers
- **Classes:** 3 — Setosa, Versicolor, Virginica
- **Features:** 4 — Sepal Length, Sepal Width, Petal Length, Petal Width
- **Source:** Built into Scikit-Learn

---

## 📈 Confusion Matrix

PREDICTED
          Setosa  Versicolor  Virginica



          Zero misclassifications across all 3 species.

---

## 🔧 Complete Pipeline

### Step 1 — Import Libraries
```python
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score
```

### Step 2 — Load Dataset
```python
iris = load_iris()
X = iris.data
y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names)
```

### Step 3 — Handle Missing Data
```python
df.replace(0, np.nan, inplace=True)
df.fillna(df.mean(), inplace=True)
```

### Step 4 — Train-Test Split 80/20
```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    shuffle=True
)
```

### Step 5 — Feature Scaling
```python
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)  # transform only — never fit_transform
```

### Step 6 — Define and Train Model
```python
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
```

### Step 7 — Evaluate
```python
predictions = model.predict(X_test)
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:")
print(cm)
print("F1 Score:", f1_score(y_test, predictions, average='weighted'))
print("Accuracy:", accuracy_score(y_test, predictions))
```

---

## 💡 What I Learned — Including My Mistakes

The most surprising discovery was that 99% accuracy can be 
completely meaningless — what the industry calls the 
**Accuracy Mirage.**

On imbalanced datasets — an AI that always predicts the 
majority class scores 99% while never catching a single 
real case. F1 Score exposes this lie.

I also discovered that using fit_transform on test data — 
a mistake I made initially — silently causes data leakage 
and produces unreliable results.

Fixing that one line improved my Wine classifier from 
94.65% to 97.28% accuracy.

Small code mistakes — huge real world consequences.


---

## 🛠️ Technologies Used
- Python 3
- NumPy
- Pandas
- Scikit-Learn
- PyCharm IDE

---

## 🚀 How to Run
1. Clone this repository
2. Install dependencies:


---


# AI-Recommendation-System
An AI Recommendation System that calculates using mathematics to accurately recommend your role based on the skills you input. 

markdown

 # 🧑‍💻 Recommendation System
 

## 🤷‍♂️ What This Recommendation System Does?
This system offers you Top 5 roles that will suit you best after you input your skills.

## How It Works
1. Gets User to type in their skills
2. System converts skills into numbers using TF-IDF
3. Cosine Similarity measures how closely skills match each role
4. Top 3 matches are returned

## 👩‍💻Technologies Used
- Python
- Pandas
- Scikit-learn (TF-IDF, Cosine Similarity)


## Complete Pipeline

### Step 1 (Install Libraries)
```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
```

### Step 2 (Reads the Raw_Skils.csv file I created)
```python
df = pd.read_csv("raw-skills.csv")
```

### Step 3 (Gets user's skills)
```python
user_input = input("Enter your skills (separated by spaces): ")
```


###Step 4 (Learning the data in the CSV file)
```python
tdif_matrix = vectorizer.fit_transform(df["skills"])
```

### Step 4 (Apply the data learnt on the user's skills)
```python
user_vector= vectorizer.transform([user_input])
```

### 📏StepMeasures the role mathStepm Top 1 - Top 3)
```python
scores = cosine_similarity(user_vector, tdif_matrix)
top_indices = scores[0].argsort()[::-1][:3]
```

### 👌Step 6 (Recommends the Top 3 roles to the user)
```python
print("\n Top 3 Recommended Roles for you:")
for i , idx in enumerate(top_indices):
    role=df["role"].iloc[idx]
    score=scores[0][idx]
    print(f"{i + 1}. {role} - Match score: {round(score * 100, 2)}%")
```

## How To Run It
1. Clone the repository
2. Make sure you have Python installed
3. Install requirements: pip install pandas scikit-learn
4. Run: python recommender.py
5. Type in your skills when prompted

## RESULT Example
Enter your skills (separated by spaces): pandas n8n Workflow_automation make.com zapier sklearn promptengineering basicpython APIs machine_learning

 Top 3 Recommended Roles for you:
1. AI Automation Specialist - Match score: 69.74%
2. AI Engineer - Match score: 26.71%
3. Data Scientist - Match score: 22.58%

Process finished with exit code 0


## 📁 Dataset Structure (raw-skills.csv)

| role | skills |
|------|--------|
|AI Engineer | Python TensorFlow PyTorch Machine_Learning Deep_Learning APIs Model_Deployment Docker|
|Prompt Engineer | LLMs Prompt_Design ChatGPT Claude API_Integration NLP AI_Tools Evaluation Fine_Tuning|
|AI Automation | Specialistn8n Make Zapier APIs Workflow_Automation LLMs Prompt_Design No_Code AI_Tools|
|AI Trainer | Python Data_Labeling Annotation Prompt_Design LLMs Evaluation Quality_Control RLHF|
|Machine Learning Engineer | Python Scikit_learn TensorFlow PyTorch Model_Training Feature_Engineering Data_Preprocessing Statistics|
|Data Scientist | Python SQL Statistics Data_Analysis Machine_Learning Data_Visualization Pandas Numpy Jupyter|
|NLP Engineer | Python NLP Transformers BERT LLMs Text_Processing Hugging_Face Deep_Learning Linguistics|
|Computer Vision Engineer | Python OpenCV TensorFlow PyTorch Image_Processing CNNs Object_Detection Deep_Learning|
|MLOps Engineer | Python Docker Kubernetes CI_CD Model_Deployment AWS Cloud MLflow Monitoring|
|Data Analyst | Python SQL Excel Data_Visualization Pandas Statistics Power_BI Reporting Business_Intelligence|



## 👨‍💻 About Me
**Torobong Umoekam Edet**
AI Engineering Intern at DecodeLabs | AI Automation Specialist
Python | Machine Learning | n8n | Make.com | Zapier
📧 umoekampraise@gmail.com
🔗 LinkedIn: https://www.linkedin.com/in/torobong-umoekam-32b0b2291
