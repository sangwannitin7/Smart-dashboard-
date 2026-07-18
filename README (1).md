# ⚡ Smart Dashboard

A clean, responsive personal dashboard built with Python and Streamlit that pulls real-time data from public APIs. This project demonstrates asynchronous data fetching, state management, and rapid frontend prototyping using pure Python.

## 🚀 Live Demo
*Coming soon! (Once deployed, replace this text with your Streamlit Community Cloud link)*

## ✨ Features
- **📈 Real-Time Crypto Tracker:** Fetches live prices and 24-hour percentage changes for Bitcoin, Ethereum, and Solana dynamically using the CoinGecko API.
- **💡 Daily Motivation:** Dynamically requests inspirational or tech quotes using the ZenQuotes API upon every page load.
- **⚙️ State Personalization:** Demonstrates interactive Python UI state management with a personalized greeting component.

## 🛠️ Tech Stack
- **Language:** Python
- **Frontend Framework:** Streamlit
- **API Handling:** Requests library
- **Data Source:** CoinGecko API & ZenQuotes API (No auth keys required)

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/smart-dashboard.git
   cd smart-dashboard
   ```

2. **Install the dependencies:**
   ```bash
   pip install streamlit requests
   ```

3. **Run the application:**
   If your Python path is fully configured:
   ```bash
   streamlit run app.py
   ```
   If you are running on Windows and encounter a path environment error, execute it directly via the Python module:
   ```bash
   python -m streamlit run app.py
   ```

## 📝 Future Roadmaps
- Add a local-storage backed persistent Daily To-Do list tracker.
- Integrate a local weather widget using geo-location mapping.
