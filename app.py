import streamlit as st
import pandas as pd
import datetime
import requests

st.set_page_config(page_title="Aditya Nexus AI", layout="wide")

# ---------- HEADER ----------
st.title("🚀 Aditya Nexus AI")
st.caption("AI Powered Capital Gain | Tax Intelligence | Wealth Platform")

menu = st.sidebar.selectbox("Navigation", [
    "🏠 Dashboard",
    "💰 Tax Engine",
    "📊 Wealth Manager",
    "📜 Tax Intelligence",
    "🔮 What-If Simulator",
    "📈 Live Market",
    "🤖 AI Advisor"
])

# ---------- TAX ENGINE ----------
def calculate_tax(gain, reinvest, asset):
    taxable = max(gain - reinvest, 0)

    if asset == "Property":
        return taxable * 0.20
    elif asset == "Equity":
        return max(taxable - 100000, 0) * 0.10
    else:
        return taxable * 0.20

# ---------- DASHBOARD ----------
if menu == "🏠 Dashboard":
    st.subheader("📊 Smart Wealth Overview")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Gain", "₹25,00,000")
    col2.metric("Tax Saved", "₹5,00,000")
    col3.metric("Net Wealth", "₹20,00,000")
    col4.metric("Risk Score", "Medium")

    st.progress(75)

    st.markdown("### 🔥 Insights")
    st.success("You are saving 20% tax using smart reinvestment.")
    st.info("Consider 54EC bonds for additional exemption.")

# ---------- TAX ENGINE ----------
elif menu == "💰 Tax Engine":
    st.subheader("💰 Unlimited Capital Gain Calculator")

    gain = st.number_input("Capital Gain (₹)", min_value=0.0, step=100000.0)
    reinvest = st.number_input("Reinvestment (₹)", min_value=0.0, step=100000.0)
    asset = st.selectbox("Asset Type", ["Property", "Equity", "Other"])

    if st.button("Calculate"):
        tax = calculate_tax(gain, reinvest, asset)

        st.success(f"Tax Payable: ₹{tax:,.2f}")
        st.info(f"Taxable Gain: ₹{max(gain - reinvest,0):,.2f}")

# ---------- WEALTH MANAGER ----------
elif menu == "📊 Wealth Manager":
    st.subheader("📊 Wealth Allocation Engine")

    equity = st.slider("Equity %", 0, 100, 50)
    debt = st.slider("Debt %", 0, 100, 30)
    gold = st.slider("Gold %", 0, 100, 20)

    data = pd.DataFrame({
        "Asset": ["Equity", "Debt", "Gold"],
        "Allocation": [equity, debt, gold]
    })

    st.bar_chart(data.set_index("Asset"))

    st.markdown("### 💡 Strategy Suggestion")

    if equity > 70:
        st.warning("High Risk Portfolio")
    elif debt > 50:
        st.info("Stable Income Strategy")
    else:
        st.success("Balanced Portfolio")

# ---------- TAX INTELLIGENCE ----------
elif menu == "📜 Tax Intelligence":
    st.subheader("📜 Indian Capital Gain Tax Strategies")

    st.markdown("""
### 🔥 Advanced Tax Saving Strategies

- Section 54 → Buy residential property
- Section 54F → Full exemption (conditions apply)
- Section 54EC → Invest in bonds (NHAI, REC)
- Indexation benefit (for long-term assets)
- Tax harvesting for equity gains

### ⚠️ Smart Tips

- Always reinvest within timeline
- Use CGAS if property not purchased
- Track holding period carefully

### 🚀 Pro Moves

- Split gains across financial years
- Combine exemptions smartly
- Use family member structuring (legal)
    """)

# ---------- SIMULATOR ----------
elif menu == "🔮 What-If Simulator":
    st.subheader("🔮 Advanced Tax Simulator")

    gain = st.number_input("Capital Gain (₹)", min_value=0.0, step=100000.0)
    reinvest = st.slider("Reinvestment %", 0, 100, 50)

    reinvest_amt = gain * (reinvest / 100)

    before = gain * 0.2
    after = max(gain - reinvest_amt, 0) * 0.2

    st.metric("Tax Before", f"₹{before:,.2f}")
    st.metric("Tax After", f"₹{after:,.2f}")

# ---------- LIVE MARKET ----------
elif menu == "📈 Live Market":
    st.subheader("📈 Live Stock Market")

    symbol = st.text_input("Enter Stock (e.g. AAPL, RELIANCE.BSE)")

    if symbol:
        st.info(f"Showing chart for {symbol}")

        # Widget trigger (IMPORTANT)
        import web
        web.run(f"genui_run|stock_chart|{{\"ticker\":\"{symbol}\"}}")

# ---------- AI ----------
elif menu == "🤖 AI Advisor":
    st.subheader("🤖 AI Tax Advisor")

    query = st.text_input("Ask anything about tax / wealth")

    if query:
        if "tax" in query.lower():
            st.write("Capital gain tax depends on asset type (10%–20%).")
        elif "save" in query.lower():
            st.write("Use 54, 54F, 54EC, CGAS strategies.")
        elif "invest" in query.lower():
            st.write("Diversify across equity, debt, gold.")
        else:
            st.write("Advanced AI coming soon 🚀")

# ---------- FOOTER ----------
st.markdown("---")
st.caption("Built by Aditya | IIT Madras | AI Fintech Innovator 🚀")
