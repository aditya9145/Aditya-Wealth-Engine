import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Smart CGAS Platform", layout="wide")

# ---------------- HEADER ----------------
st.title("🏦 Smart CGAS Platform")
st.caption("AI + Wealth + Tax Optimization Engine")

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio("Navigation", [
    "🏠 Dashboard",
    "📊 Calculator",
    "🔮 Simulator",
    "📈 Insights",
    "🤖 AI Advisor",
])

# ---------------- DASHBOARD ----------------
if menu == "🏠 Dashboard":
    col1, col2, col3 = st.columns(3)
    col1.metric("Capital Gain", "₹12L")
    col2.metric("Tax", "₹2.4L")
    col3.metric("Saved", "₹1.2L")

    st.subheader("Utilization")

    data = pd.DataFrame({
        "Type": ["Used", "Remaining"],
        "Amount": [500000, 700000]
    })

    fig, ax = plt.subplots()
    ax.pie(data["Amount"], labels=data["Type"], autopct='%1.1f%%')
    st.pyplot(fig)

# ---------------- CALCULATOR ----------------
elif menu == "📊 Calculator":
    sale = st.number_input("Sale Price", 0)
    purchase = st.number_input("Purchase Price", 0)

    if st.button("Calculate"):
        gain = sale - purchase
        tax = gain * 0.2 if gain > 0 else 0

        st.success(f"Gain: ₹{gain}")
        st.error(f"Tax: ₹{tax}")

        if gain > 1000000:
            st.info("💡 Property + Bonds recommended")
        elif gain > 500000:
            st.info("💡 CGAS + Bonds")
        else:
            st.info("💡 CGAS only")

# ---------------- SIMULATOR ----------------
elif menu == "🔮 Simulator":
    gain = st.number_input("Capital Gain", 0)
    reinvest = st.slider("Reinvest", 0, int(gain) if gain > 0 else 0)

    before = gain * 0.2
    after = (gain - reinvest) * 0.2

    st.write("Tax Before:", before)
    st.write("Tax After:", after)

# ---------------- INSIGHTS ----------------
elif menu == "📈 Insights":
    st.subheader("Smart Insights")

    gain = st.number_input("Enter Gain", 0)

    if gain > 1000000:
        st.warning("⚠ High tax exposure detected")
        st.success("✔ Recommendation: Property reinvestment")
    elif gain > 500000:
        st.info("💡 Moderate tax planning needed")
    else:
        st.success("✔ Low tax impact")

# ---------------- AI ADVISOR ----------------
elif menu == "🤖 AI Advisor":
    st.subheader("AI Advisor")

    user = st.text_input("Ask anything:")

    if user:
        # fallback logic (works without API)
        if "tax" in user.lower():
            st.write("Tax is approx 20%. Use CGAS or reinvestment.")
        elif "save" in user.lower():
            st.write("Use CGAS + 54EC bonds to save tax.")
        else:
            st.write("AI suggestion: Plan reinvestment smartly.")
