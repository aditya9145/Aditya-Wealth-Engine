import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime
from openai import OpenAI

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Aditya Nexus AI", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #0f172a, #1e293b);
        color: white;
    }
    .card {
        padding: 20px;
        border-radius: 15px;
        background: rgba(255,255,255,0.05);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        margin-bottom: 15px;
    }
    .metric {
        font-size: 22px;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.title("🚀 Aditya Nexus AI")
st.caption("Next-Gen Intelligent CGAS Platform")

# ---------- SIDEBAR ----------
menu = st.sidebar.radio("Navigation", [
    "🏠 Dashboard",
    "💰 Tax Engine",
    "📈 Market",
    "🔮 Simulator",
    "⚠️ Compliance",
    "🤖 AI Advisor"
])

# ---------- API ----------
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

# ---------- DASHBOARD ----------
if menu == "🏠 Dashboard":
    st.subheader("📊 Financial Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><div class="metric">₹10,00,000</div>Total Gain</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><div class="metric">₹2,00,000</div>Tax Saved</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><div class="metric">₹8,00,000</div>Net Wealth</div>', unsafe_allow_html=True)

    st.progress(70)

# ---------- TAX ----------
elif menu == "💰 Tax Engine":
    st.subheader("💰 Smart Tax Calculator")

    col1, col2 = st.columns(2)

    with col1:
        gain = st.number_input("Capital Gain", value=1000000)

    with col2:
        reinvest = st.number_input("Reinvestment", value=0)

    if st.button("Calculate Tax"):
        tax = (gain - reinvest) * 0.2
        st.success(f"💸 Estimated Tax: ₹{tax}")

# ---------- MARKET ----------
elif menu == "📈 Market":
    st.subheader("📈 Live Market Tracker")

    symbol = st.text_input("Enter Stock Symbol")

    if st.button("Fetch Data"):
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=YOUR_API_KEY"
        data = requests.get(url).json()

        try:
            df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient='index')
            df = df.astype(float)
            df = df.sort_index()

            st.line_chart(df["4. close"])
        except:
            st.error("Error fetching data")

# ---------- SIMULATOR ----------
elif menu == "🔮 Simulator":
    st.subheader("🔮 What-If Analysis")

    gain = st.slider("Capital Gain", 0, 2000000, 1000000)
    reinvest = st.slider("Reinvest", 0, gain, 200000)

    before = gain * 0.2
    after = (gain - reinvest) * 0.2

    st.metric("Tax Before", f"₹{before}")
    st.metric("Tax After", f"₹{after}")

# ---------- COMPLIANCE ----------
elif menu == "⚠️ Compliance":
    st.subheader("⚠️ Risk Monitor")

    date = st.date_input("Investment Date")
    days = (datetime.date.today() - date).days

    if days > 1000:
        st.error("🚨 High Risk")
    elif days > 700:
        st.warning("⚠️ Deadline Near")
    else:
        st.success("✅ Safe")

# ---------- AI ----------
elif menu == "🤖 AI Advisor":
    st.subheader("🤖 AI Assistant")

    query = st.text_input("Ask anything")

    if st.button("Ask"):
        if query:
            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[{"role":"user","content":query}]
            )
            st.write(response.choices[0].message.content)

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built by Aditya | IIT Madras | AI Innovator")
