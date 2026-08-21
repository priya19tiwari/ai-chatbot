# 🎓 AI Tutor Chatbot

An AI-powered educational chatbot that helps users understand **AI, Machine Learning, Deep Learning, NLP, and Programming** concepts through natural-language conversations.

The project uses **Google Gemini API** with a **Python Flask backend** and an **HTML, CSS, and JavaScript frontend**.

## 🚀 Live Demo

🔗 **Live Chatbot:** Add your Render URL here

## ✨ Features

* 🤖 AI-powered chatbot using Google Gemini
* 🎓 Designed as an AI tutor
* 💬 Natural-language question and answer
* 🧠 Supports AI, ML, DL, NLP, and programming topics
* 📱 Responsive chat interface
* 🔐 Secure API key management using environment variables
* ⚡ Flask REST API
* ☁️ Deployed on Render
* 🔄 GitHub-based deployment

## 🛠️ Tech Stack

**Frontend**

* HTML5
* CSS3
* JavaScript

**Backend**

* Python
* Flask

**AI**

* Google Gemini API
* Google GenAI Python SDK

**Deployment & Tools**

* Git
* GitHub
* Render

## 🏗️ Architecture

```text
User
  ↓
HTML / CSS / JavaScript
  ↓
JavaScript fetch()
  ↓
POST /chat
  ↓
Python Flask Backend
  ↓
Google Gemini API
  ↓
AI Response
  ↓
Flask JSON Response
  ↓
Chat Interface
```

## 📂 Project Structure

```text
ai-chatbot/
│
├── app_gemini.py
├── requirements.txt
├── list_models.py
├── test_gemini.py
│
└── templates/
    └── index.html
```

## ⚙️ How It Works

1. The user enters a question in the chatbot.
2. JavaScript sends the question to the Flask `/chat` endpoint.
3. Flask receives the request.
4. Flask sends the question to the Google Gemini API.
5. Gemini generates the response.
6. Flask returns the response as JSON.
7. JavaScript displays the response in the chat interface.

## 🔐 Environment Variable

The Gemini API key is stored securely as an environment variable and is **not committed to GitHub**.

```text
GEMINI_API_KEY=your_api_key_here
```

## 💻 Run Locally

### Clone the repository

```bash
git clone https://github.com/priya19tiwari/ai-chatbot.git
cd ai-chatbot
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Set the Gemini API key

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

### Run the application

```bash
python app_gemini.py
```

Open:

```text
http://127.0.0.1:5000
```

## ☁️ Deployment

The application is deployed using **Render**.

```text
GitHub
   ↓
Render
   ↓
Build
   ↓
Deploy
   ↓
Live AI Chatbot
```

Environment variables are configured securely through Render.

## 🐛 Debugging Experience

During deployment, the chatbot initially returned a server error.

I investigated the issue using **Render logs**, identified a Gemini API model availability error, updated the model configuration, committed the change to GitHub, and redeployed the application.

This helped me gain practical experience with:

* API debugging
* HTTP error handling
* Production logs
* Environment variables
* Cloud deployment
* GitHub-based deployment workflows

## 📚 What I Learned

* Flask backend development
* REST API integration
* Frontend-backend communication
* Generative AI API integration
* Environment variable management
* API debugging
* Git and GitHub
* Cloud deployment using Render

## 🔮 Future Improvements

* User authentication
* Chat history
* Database integration
* Voice input
* PDF/document-based questions
* Personalized learning
* Multi-language support
* Dark mode

## 👩‍💻 Author

**Priya Tiwari**

MCA | Full Stack Developer

🔗 GitHub: https://github.com/priya19tiwari
