import streamlit as st

st.title("👨‍💻 Team Members")

team = [
    {
        "name": "Divyanshu Ranjan",
        "image": "assets/member1.jpg",
        "linkedin": "https://linkedin.com/in/divyanshu-ranjan-b23986271"
    },
    {
        "name": "Awanish Bhatt",
        "image": "assets/bhatt.jpeg",
        "linkedin": "https://linkedin.com/in/awanish-bhatt-153585276"
    },
    {   
        "name": "Harsh Awasthi",
        "image": "assets/aw.jpeg",
        "linkedin": "https://linkedin.com/in/harsh-awasthi-6132b82a1"
    },
    {
        "name": "Akash Nigam",
        "image": "assets/nigam.jpeg",
        "linkedin": "https://linkedin.com/in/akash-nigam-3436ab248"
    }
]

cols = st.columns(len(team))

for i, member in enumerate(team):
    with cols[i]:
        st.image(member["image"], caption=member["name"], width=150)
        st.markdown(f"[LinkedIn ↗️]({member['linkedin']})", unsafe_allow_html=True)
