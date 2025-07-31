# Technologies_Used.py
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Technologies Used", page_icon="🛠️")
st.title("🛠️ Technologies Used")

cols = st.columns(4)

with cols[0]:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1b/Python_logo_65x50.png", width=60)
    st.caption("Python")

with cols[1]:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg", width=60)
    st.caption("scikit-learn")

with cols[2]:
    st.image("https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png", width=60)
    st.caption("Streamlit")

with cols[3]:
    st.image("https://pandas.pydata.org/static/img/pandas_white.svg", width=60)
    st.caption("Pandas")
