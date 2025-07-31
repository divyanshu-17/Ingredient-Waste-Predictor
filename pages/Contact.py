# Contact.py
import streamlit as st

st.set_page_config(page_title="Contact Us", page_icon="📢")
st.title("📢 Contact Us")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    query = st.text_area("Your Query")
    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Thanks {name}, we have received your query!")
