# MindMirror 🪞

**MindMirror** is a minimal, AI-powered journaling app designed to help users reflect on their emotions through daily writing. It offers quick sentiment feedback based on your journal entry to encourage self-awareness and mindfulness.

---

## 🧠 Overview

MindMirror provides a simple interface: write about your day, submit, and get an immediate emotional analysis. It's meant to be lightweight, private, and user-friendly — no signups, no data tracking, no clutter.

---

## 🛠️ Tech Stack

- **Python 3.13**
- **Flask** – for the backend web server
- **TextBlob** – for basic natural language sentiment analysis
- **HTML/CSS** – simple frontend interface

No database required. All analysis runs locally.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.13 installed on your system

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/mindmirror.git
cd mindmirror

--
## Set up Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
--
##Install Dependencies
pip install -r requirements.txt

--

## Run the app
python app.py

--
## ✨ Features
Clean journaling interface

Instant emotional analysis of journal entries

Fully local and private (no data stored)

Lightweight and easy to run

mindmirror/
│
├── app.py               # Flask web server
├── analysis.py          # Sentiment analysis logic
├── requirements.txt     # Project dependencies
├── templates/
│   └── index.html       # Frontend interface
└── .gitignore           # Ignored files and folders

## Privacy
MindMirror does not store, transmit, or log user entries. All analysis is done in-memory and locally in your browser session
--

## Contributions
Feel free to fork, adapt, or build on top of this project. If you'd like to suggest a feature or fix a bug, open an issue or pull request.
--

## Possible Improvements
Mood history tracking

Tagging or categorizing journal entries

More advanced emotion detection

