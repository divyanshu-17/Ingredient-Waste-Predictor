# Team.py
import streamlit as st

st.set_page_config(page_title="Team Members", page_icon="👥")
st.title("👥 Team Members")

team_data = [
    ("Divyanshu Ranjan", "https://www.linkedin.com/in/divyanshu-ranjan-b23986271"),
    ("Harsh Awasthi", "https://www.linkedin.com/in/harsh-awasthi-6132b82a1"),
    ("Akash Nigam", "https://www.linkedin.com/in/akash-nigam-3436ab248"),
    ("Awanish Bhatt", "https://www.linkedin.com/in/awanish-bhatt-153585276")
]

for name, link in team_data:
    st.markdown(f"- [{name}]({link})")
