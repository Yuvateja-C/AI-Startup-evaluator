# 🧠 InvestorLens AI

### AI-Powered Startup Idea Evaluator (Local LLM)

---

## 🚀 Overview

**InvestorLens AI** is an AI-powered web application that evaluates startup or project ideas like a real investor.

It analyzes ideas based on multiple factors and provides:

* 📊 Score (0–100)
* ✅ Verdict (Invest / Reject)
* 💡 Reasoning & insights

Unlike typical AI projects, this system uses a **local Large Language Model (LLM)** via Ollama, making it:

* 💸 Free to use
* 🔒 Privacy-friendly
* ⚡ Offline-capable

---

## 🎯 Features

* 🧠 AI-based idea evaluation
* 📊 Smart scoring system
* ⚖️ Investor-style verdict
* 💬 Reasoning explanation
* 👤 User authentication (Login/Register)
* 🏆 Leaderboard of top ideas
* 🔄 Multiple investor modes:

  * Friendly
  * Strict
  * Shark (Harsh evaluation 😈)
* ⚡ Works with local AI (Ollama – LLaMA 3)
* 🛡️ Error-safe JSON parsing (handles messy AI outputs)

---

## 🛠️ Tech Stack

| Technology | Usage             |
| ---------- | ----------------- |
| Python     | Core programming  |
| Streamlit  | Frontend UI       |
| Ollama     | Local AI model    |
| LLaMA 3    | Language model    |
| SQLite     | Database          |
| Requests   | API communication |

---

## 🧩 Project Structure

```
InvestorLens-AI/
│
├── app.py              # Main Streamlit app
├── evaluator.py        # AI evaluation logic
├── prompts.py          # Prompt engineering
├── database.py         # Database handling
├── auth.py             # Authentication system
├── requirements.txt    # Dependencies
├── README.md           # Project documentation
└── assets/             # Screenshots/images
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/YOUR_USERNAME/InvestorLens-AI.git
cd InvestorLens-AI
```

---

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Install Ollama

Download from:
👉 https://ollama.com

---

### 4️⃣ Pull the AI model

```
ollama pull llama3
```

---

### 5️⃣ Run Ollama

```
ollama run llama3
```

---

### 6️⃣ Run the application

```
python -m streamlit run app.py
```

---

### 7️⃣ Open in browser

```
http://localhost:8501
```

---

## 📸 Screenshots

![App Screenshot](assets/screenshot.png)

---

## 🧠 How It Works

1. User enters a startup idea
2. Idea is sent to the local AI model
3. AI evaluates based on:

   * Market potential
   * Innovation
   * Feasibility
   * Risk
4. AI returns structured or semi-structured output
5. App extracts JSON safely
6. Results are displayed and stored

---

## ⚠️ Challenges Solved

* ❌ Handling inconsistent AI outputs
* ❌ JSON parsing errors
* ❌ API dependency removal
* ✅ Built robust fallback parsing system
* ✅ Implemented local AI integration

---

## 🔮 Future Improvements

* 📊 Analytics dashboard (graphs & insights)
* 🎤 Voice input support
* 🔍 Idea comparison system
* 🌐 Online deployment with API fallback
* 📱 Mobile-friendly UI

---

## 💡 Use Cases

* Students evaluating project ideas
* Startup founders testing concepts
* Hackathon idea validation
* Learning AI product development

---

## 📌 Key Learning Outcomes

* Working with Local LLMs (Ollama)
* Prompt Engineering
* Full-stack AI application development
* Error handling in AI systems
* Building production-ready projects

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Yuva Teja**
B.Tech Student | AI Enthusiast

---

## ⭐ Support

If you like this project:
👉 Star this repository
👉 Share it with others

---

## 💬 Final Note

This project demonstrates how AI can simulate **human-like decision making in venture capital**, making it a powerful tool for idea validation and learning AI product development.

---
