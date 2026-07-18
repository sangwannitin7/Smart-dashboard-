import streamlit as st
import requests
from datetime import datetime

st.set_page_config(
    page_title="Personal Smart Dashboard",
    page_icon="⚡",
    layout="wide"
)

def get_crypto_prices():
    """Fetches real-time crypto prices from CoinGecko (No key required)."""
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd&include_24hr_change=true"
        response = requests.get(url, timeout=5)
        return response.json()
    except Exception:
        return None

def get_daily_quote():
    """Fetches a random programming/inspirational quote."""
    try:
        url = "https://zenquotes.io/api/random"
        response = requests.get(url, timeout=5)
        data = response.json()
        return data[0]['q'], data[0]['a']
    except Exception:
        return "Code is like humor. When you have to explain it, it’s bad.", "Cory House"

st.title("⚡ Personal Smart Dashboard")
st.write(f"Welcome back! Today is **{datetime.now().strftime('%A, %B %d, %Y')}**")

st.divider()

col1, col2 = st.columns([2, 1])

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
    st.subheader("💡 Daily Motivation")
    quote, author = get_daily_quote()
    st.info(f'"{quote}" \n\n— *{author}*')

    st.subheader("⚙️ Quick Tools")
    user_name = st.text_input("Personalize your dashboard greeting:", placeholder="Enter your name")
    if user_name:
        st.success(f"Hello, {user_name}! Have a highly productive coding session!")

st.divider()
st.caption("Built with Python & Streamlit • Connect live data via free public APIs")
