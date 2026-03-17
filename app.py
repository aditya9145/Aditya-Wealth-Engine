import streamlit as st
import pandas as pd
import datetime
import requests

# ===== OPTIONAL REAL AI =====
USE_REAL_AI = False  # True karo agar OpenAI API use karna hai

if USE_REAL_AI:
    from openai import OpenAI
    client = OpenAI(api_key="PASTE_YOUR_OPENAI_KEY")

# ---------- CONFIG ----------
st.set_page_config(page_title="Aditya Nexus AI", layout="wide")

# ---------- LOGIN ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Login - Aditya Nexus AI")

    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.session_state.logged_in = True
        else:
            st.error("Invalid credentials")

    st.stop()

# ---------- HEADER ----------
st.title("🚀 Aditya Nexus AI")
st.caption("Unlimited Capital Gain Tax Intelligence System")

menu = st.sidebar.selectbox("Menu", [
    "🏠 Dashboard",
    "💰 Tax Engine",
    "📜 Tax Laws",
    "📈 Market",
    "🔮 Simulator",
    "⚠️ Compliance",
    "🤖 AI Advisor"
])

# ---------- TAX ENGINE ----------
def calculate_tax(gain, reinvest, asset):
    taxable = max(gain - reinvest, 0)

    if asset == "Property":
        return taxable * 0.20
    elif asset == "Equity":
        return taxable * 0.10
    else:
        return taxable * 0.20

# ---------- TAX RULES ----------
def get_tax_rules(gain):
    rules = []

    if gain > 0:
        rules.append("Section 54 → Reinvest in residential property")
        rules.append("Section 54EC → Invest in bonds within 6 months")
        rules.append("Section 54F → Full exemption possible")

    if gain > 10000000:
        rules.append("High-value gain → Advanced tax planning recommended")

    return rules

# ---------- DASHBOARD ----------
if menu == "🏠 Dashboard":
    col1, col2, col3 = st.columns(3)

    col1.metric("Total Gain", "₹10,00,000")
    col2.metric("Tax Saved", "₹2,00,000")
    col3.metric("Net Wealth", "₹8,00,000")

    st.progress(80)

# ---------- TAX ENGINE ----------
elif menu == "💰 Tax Engine":
    st.subheader("Unlimited Capital Gain Calculator")

    gain = st.number_input("Capital Gain (₹)", min_value=0.0, step=100000.0)
    reinvest = st.number_input("Reinvestment (₹)", min_value=0.0, step=100000.0)
    asset = st.selectbox("Asset Type", ["Property", "Equity", "Other"])

    if st.button("Calculate Tax"):
        tax = calculate_tax(gain, reinvest, asset)

        st.success(f"💸 Tax Payable: ₹{tax:,.2f}")
        st.info(f"💰 Taxable Gain: ₹{max(gain - reinvest,0):,.2f}")

# ---------- TAX LAWS ----------
elif menu == "📜 Tax Laws":
    st.subheader("Tax Intelligence Engine")

    gain = st.number_input("Enter Capital Gain (₹)", min_value=0.0, step=100000.0)

    rules = get_tax_rules(gain)

    for r in rules:
        st.info(r)

# ---------- MARKET ----------
elif menu == "📈 Market":
    st.subheader("Stock Viewer (Stable Version)")

    symbol = st.text_input("Enter Stock Symbol (e.g. AAPL)")

    if st.button("Fetch Data"):
        try:
            API_KEY = "YOUR_ALPHA_KEY"
            url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"

            data = requests.get(url).json()

            if "Time Series (Daily)" in data:
                df = pd.DataFrame.from_dict(data["Time Series (Daily)"], orient='index')
                df = df.astype(float)
                df = df.sort_index()
                st.line_chart(df["4. close"])
            else:
                raise Exception()

        except:
            st.warning("⚠️ API error, showing demo data")
            df = pd.DataFrame({"Price":[100,120,115,130,140,150]})
            st.line_chart(df)

# ---------- SIMULATOR ----------
elif menu == "🔮 Simulator":
    st.subheader("Unlimited What-If Simulator")

    gain = st.number_input("Capital Gain (₹)", min_value=0.0, step=100000.0)
    reinvest = st.number_input("Reinvestment (₹)", min_value=0.0, step=100000.0)

    before = gain * 0.2
    after = max(gain - reinvest, 0) * 0.2

    st.metric("Tax Before", f"₹{before:,.2f}")
    st.metric("Tax After", f"₹{after:,.2f}")

# ---------- COMPLIANCE ----------
elif menu == "⚠️ Compliance":
    st.subheader("CGAS Compliance Tracker")

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

# ---------- AI ----------
elif menu == "🤖 AI Advisor":
    st.subheader("AI Financial Advisor")

    query = st.text_input("Ask anything about tax")

    if st.button("Ask AI"):

        if USE_REAL_AI:
            try:
                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[
                        {"role": "system", "content": "You are an expert in Indian capital gain tax and finance."},
                        {"role": "user", "content": query}
                    ]
                )
                st.write(response.choices[0].message.content)

            except:
                st.error("API Error")

        else:
            # SAFE AI MODE
            if "tax" in query.lower():
                st.write("Capital gain tax: 20% (property), 10% (equity).")
            elif "54" in query:
                st.write("Section 54 allows exemption on property reinvestment.")
            elif "save" in query.lower():
                st.write("Use CGAS, bonds (54EC), and reinvestment.")
            else:
                st.write("AI Demo Mode: Ask about tax saving strategies.")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built by Aditya | IIT Madras | AI Innovator 🚀")
