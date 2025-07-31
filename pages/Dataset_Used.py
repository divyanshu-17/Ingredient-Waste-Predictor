# Dataset_Used.py
import streamlit as st

st.set_page_config(page_title="Dataset Used", page_icon="📊")
st.title("📊 Dataset Used")

st.markdown("""
We used a dataset named `final_ingredient_waste_dataset.csv`.

### Key Features:
- Ingredient Name
- Quantity Purchased & Used
- Expected Usage
- Date (with Holidays/Weekend)
- Weather Info (optional)

Upload this dataset on the **Home** page to get predictions.
""")
