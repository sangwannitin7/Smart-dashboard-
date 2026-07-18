import streamlit as st
import requests
from datetime import datetime

st.set_page_config(
    page_title="Personal Smart Dashboard Pro",
    page_icon="⚡",
    layout="wide"
)

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def get_crypto_prices():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url, timeout=5)
        return response.json()
    except Exception:
        return None

def get_daily_quote():
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data[0]['q'], data[0]['a']
    except Exception:
        return "Code is like humor. When you have to explain it, it’s bad.", "Cory House"

def get_weather():
    """Fetches weather for Delhi, India by default using Open-Meteo."""
    try:
        city = "Delhi, India"
        lat = 28.6139
        lon = 77.2090

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_response = requests.get(weather_url, timeout=3)
        weather_response.raise_for_status()
        weather_data = weather_response.json()
        value = weather_data.get("current_weather", {}).get("temperature")

        if value is None:
            return f"{city} • Weather unavailable"

        return f"{city} • {value}°C"
    except Exception:
        return f"{city} • Weather unavailable"

st.title("⚡ Personal Smart Dashboard Pro")

c_date, c_weather = st.columns(2)
with c_date:
    st.write(f"📅 Today is **{datetime.now().strftime('%A, %B %d, %Y')}**")
with c_weather:
    st.write(f"🌍 **Location/Weather:** {get_weather()}")

st.divider()

col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    st.subheader("📈 Real-Time Crypto Tracker")
    crypto_data = get_crypto_prices()

    if crypto_data:
        m1, m2, m3 = st.columns(3)

        btc_price = crypto_data['bitcoin']['usd']
        btc_change = crypto_data['bitcoin']['usd_24h_change']
        m1.metric("Bitcoin (BTC)", f"${btc_price:,.2f}", f"{btc_change:.2%}")

        eth_price = crypto_data['ethereum']['usd']
        eth_change = crypto_data['ethereum']['usd_24h_change']
        m2.metric("Ethereum (ETH)", f"${eth_price:,.2f}", f"{eth_change:.2%}")

        sol_price = crypto_data['solana']['usd']
        sol_change = crypto_data['solana']['usd_24h_change']
        m3.metric("Solana (SOL)", f"${sol_price:,.2f}", f"{sol_change:.2%}")
    else:
        st.error("Failed to load crypto data. API rate limit hit, try refreshing!")

with col2:
    st.subheader("🎯 Today's Focus List")

    new_task = st.text_input("Add a high-priority task:", key="task_input", placeholder="e.g., Push code to GitHub")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.rerun()

    if st.session_state.tasks:
        for idx, task_item in enumerate(st.session_state.tasks):

            is_done = st.checkbox(task_item["task"], value=task_item["done"], key=f"task_{idx}")
            st.session_state.tasks[idx]["done"] = is_done

        if st.button("Clear Completed Tasks"):
            st.session_state.tasks = [t for t in st.session_state.tasks if not t["done"]]
            st.rerun()
    else:
        st.write("*No tasks added for today yet. Stay productive!*")

with col3:
    st.subheader("💡 Daily Motivation")
    quote, author = get_daily_quote()
    st.info(f'"{quote}" \n\n— *{author}*')

    st.subheader("⚙️ Greetings")
    user_name = st.text_input("Change User Greeting:", value="Hi user", placeholder="Your Name")
    if user_name:
        st.success(f"Welcome, {user_name}!")

st.divider()
st.caption("Built with Python & Streamlit • Leverages session state management and dual API routing.")
