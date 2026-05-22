import streamlit as st
import pandas as pd

from core.scanner import run_scan
from core.risk_engine import calculate_risk

st.set_page_config(page_title="Cloud Security Platform", layout="wide")

st.title("Cloud Security Posture & Compliance Platform")

try:
    findings = run_scan()
except Exception as e:
    st.error(f"Scanner failed: {e}")
    st.stop()

if not findings:
    st.warning("No security findings returned.")
    st.stop()

risk = calculate_risk(findings)

df = pd.DataFrame(findings)

st.metric("Risk Score", risk["score"])
st.metric("Risk Level", risk["level"])

st.subheader("Security Findings")
st.dataframe(df, use_container_width=True)

st.subheader("Severity Breakdown")
st.bar_chart(df["severity"].value_counts())

st.success("Dashboard loaded successfully")