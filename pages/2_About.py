# About.py
import streamlit as st

st.set_page_config(page_title="About", page_icon="📘")
st.title("📘 About This Project")

st.markdown("""
### 🥦 Ingredient Waste Predictor

This project aims to help restaurants reduce ingredient waste by predicting excess based on historical usage, weather, holidays, and other patterns.

**Problem Addressed:**
- Food waste leads to financial losses and environmental impact.

**Solution Provided:**
- Our machine learning model analyzes restaurant inventory and sales data.
- Predicts waste per ingredient so restaurants can optimize purchasing.

This tool empowers restaurant managers with **data-driven insights** to make better operational decisions.

---
💡 Built with love and code by passionate data engineers.
""")
