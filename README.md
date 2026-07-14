# 🤖 AI Chatbot

A simple AI chatbot built using **Python**, **NLTK**, and **Streamlit**. The chatbot uses basic Natural Language Processing (NLP) techniques to tokenize user input and generate keyword-based responses through an interactive web interface.

---

## 📌 Features

* Interactive chatbot interface built with Streamlit
* Basic NLP using NLTK for text tokenization
* Keyword-based response generation
* Beginner-friendly and easy to customize
* Lightweight and easy to run locally

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **NLTK (Natural Language Toolkit)**

---

## 📂 Project Structure

```
AI-Chatbot/
│── app.py
│── chatbot.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/AI-Chatbot.git
cd AI-Chatbot
```

### 2. Create a virtual environment (Optional)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

The application will open in your default web browser.

---

## 💬 Sample Conversation

```
You: Hello
Bot: Hi! How can I help you?

You: Tell me about Python
Bot: Python is a popular programming language.

You: Help
Bot: Sure! Ask me anything related to Python or greetings.

You: Bye
Bot: Goodbye! Have a nice day!
```

---

## 📸 Screenshot

Add a screenshot of the chatbot interface here after running the project.

```
assets/chatbot.png
```

---

## 📖 How It Works

1. The user enters a message in the Streamlit interface.
2. NLTK tokenizes the input into individual words.
3. The chatbot searches for matching keywords.
4. If a keyword is found, it returns the corresponding predefined response.
5. Otherwise, it displays a default fallback message.

---

## 🔮 Future Improvements

* Add conversation history
* Support more intents and responses
* Integrate machine learning models
* Add voice input and speech output
* Connect to an LLM API (OpenAI, Gemini, etc.)
* Deploy the chatbot online using Streamlit Community Cloud

---

## 👩‍💻 Author

**Rajgaurav Mishra**

If you found this project helpful, consider giving it a ⭐ on GitHub.
