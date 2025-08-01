import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Ingredient Waste Predictor",
    page_icon="🥦",
    layout="wide",
)

# Title
st.markdown("<h1 style='text-align: center; color: green;'>Ingredient Waste Prediction App 🥦</h1>", unsafe_allow_html=True)
st.markdown("### 📢 Welcome! Use the sidebar to navigate through the app sections.")

# Optional Banner
st.image("https://images.unsplash.com/photo-1569058242342-8402b041c8b1", use_column_width=True)

# App Description
st.markdown("""
This application helps restaurant managers predict ingredient waste using machine learning.
Upload your CSV, view predictions, feature insights, and connect with our team.

---

### 🔍 Navigation Overview:

- **Home**: You're here! Central place to understand the app.
- **About**: Project motivation and goals.
- **Technologies Used**: Libraries and tools powering this app.
- **Team Members**: Meet the developers.
- **Dataset Used**: Know your data source.
- **Contact**: Reach out to us with questions or suggestions.

---
""")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("Made with ❤️ by Divyanshu Ranjan and team.")
