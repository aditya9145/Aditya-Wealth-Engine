import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests
import datetime

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Aditya Nexus AI", layout="wide")

# ---------- CUSTOM UI ----------
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

# ---------- DASHBOARD ----------
if menu == "🏠 Dashboard":
    st.subheader("📊 Financial Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="card"><b>Total Gain</b><br>₹10,00,000</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><b>Tax Saved</b><br>₹2,00,000</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="card"><b>Net Wealth</b><br>₹8,00,000</div>', unsafe_allow_html=True)

    st.progress(70)

# ---------- TAX ENGINE ----------
elif menu == "💰 Tax Engine":
    st.subheader("💰 Smart Tax Calculator")

    gain = st.number_input("Capital Gain", value=1000000)
    reinvest = st.number_input("Reinvestment", value=0)

    if st.button("Calculate Tax"):
        taxable = max(gain - reinvest, 0)
        tax = taxable * 0.2

        st.success(f"💸 Estimated Tax: ₹{tax}")
        st.info("Tip: Use Section 54 / 54EC to save tax")

# ---------- MARKET ----------
elif menu == "📈 Market":
    st.subheader("📈 Stock Market Viewer")

    symbol = st.text_input("Enter Stock Symbol (e.g. AAPL)")

    if st.button("Fetch Data"):
        try:
            # TRY REAL API (OPTIONAL)
            API_KEY = "YOUR_ALPHA_KEY"
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

            response = requests.get(url)
            data = response.json()

            if "Time Series (Daily)" in data:
                df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient='index')
                df = df.astype(float)
                df = df.sort_index()
                st.line_chart(df["4. close"])
            else:
                st.warning("⚠️ API issue, showing demo data")
                raise Exception()

        except:
            # FALLBACK (ALWAYS WORKING)
            demo = pd.DataFrame({
                "Price": [100, 105, 110, 108, 115, 120]
            })
            st.line_chart(demo)

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
    st.subheader("⚠️ CGAS Compliance Tracker")

    date = st.date_input("Investment Date")

    if date:
        days = (datetime.date.today() - date).days

        st.write(f"Days Passed: {days}")

        if days > 1000:
            st.error("🚨 High Risk: Tax Triggered")
        elif days > 700:
            st.warning("⚠️ Deadline Near")
        else:
            st.success("✅ Safe Zone")

# ---------- AI ADVISOR ----------
elif menu == "🤖 AI Advisor":
    st.subheader("🤖 AI Assistant")

    user_input = st.text_input("Ask about tax, CGAS, investment")

    if st.button("Ask AI"):
        if user_input:
            # OFFLINE SMART RESPONSES (NO ERROR)
            if "tax" in user_input.lower():
                st.write("Capital gains tax is approx 20% in India.")
            elif "save" in user_input.lower():
                st.write("You can save tax via Section 54 or 54EC bonds.")
            elif "cg as" in user_input.lower():
                st.write("CGAS helps defer capital gains tax until reinvestment.")
            else:
                st.write("AI Demo Mode: Try asking about tax or saving.")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built by Aditya | IIT Madras | AI Innovator 🚀")
