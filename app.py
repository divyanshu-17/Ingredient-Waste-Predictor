import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Page configuration
st.set_page_config(page_title="Ingredient Waste Predictor", page_icon="🥦", layout="centered")

st.title("🥦 Ingredient Waste Prediction App")
st.markdown("Upload your restaurant ingredient & sales dataset to predict waste per ingredient.")

# Load model and encoder columns
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    return model

@st.cache_resource
def load_encoder_columns():
    with open("encoder_columns.pkl", "rb") as f:
        cols = pickle.load(f)
    return cols

model = load_model()
encoder_columns = load_encoder_columns()

# File upload
uploaded_file = st.file_uploader("📂 Upload your final_ingredient_waste_dataset.csv", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        st.success("✅ File uploaded successfully!")
        st.write("🔍 Data Preview:")
        st.dataframe(df.head())

        # Feature Engineering
        df['Date'] = pd.to_datetime(df['Date'])
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day
        df['DayOfWeek'] = df['Date'].dt.dayofweek

        # Fill missing values
        df['Weather'] = df['Weather'].fillna('Unknown') if 'Weather' in df else 'Unknown'
        df['Holiday'] = df['Holiday'].fillna('No') if 'Holiday' in df else 'No'
        for col in ['Expected_Ingredient_Usage_kg', 'Purchased_Qty_kg', 'Quantity_Used', 'Is_Weekend']:
            if col in df.columns:
                df[col] = df[col].fillna(0)

        # One-hot encode
        categorical_cols = ['Ingredient']
        if 'Weather' in df.columns: categorical_cols.append('Weather')
        if 'Holiday' in df.columns: categorical_cols.append('Holiday')

        df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

        # Align with model input features
        for col in encoder_columns:
            if col not in df_encoded.columns:
                df_encoded[col] = 0
        df_encoded = df_encoded[encoder_columns]

        # Predict
        predictions = model.predict(df_encoded)
        df['Predicted_Waste_kg'] = predictions

        st.subheader("📊 Prediction Results:")
        st.dataframe(df[['Date', 'Ingredient', 'Predicted_Waste_kg']].head())

        # Download predictions
        csv = df.to_csv(index=False).encode()
        st.download_button(
            label="📥 Download Full Prediction CSV",
            data=csv,
            file_name="predicted_waste_results.csv",
            mime="text/csv"
        )

        # Visualize prediction distribution
        st.subheader("📈 Waste Prediction Distribution")
        fig, ax = plt.subplots()
        sns.histplot(df['Predicted_Waste_kg'], bins=20, kde=True, ax=ax, color='skyblue')
        ax.set_xlabel("Predicted Waste (kg)")
        st.pyplot(fig)

        # Feature importance (from model)
        st.subheader("💡 Feature Importance")
        importances = model.feature_importances_
        features = encoder_columns
        imp_df = pd.Series(importances, index=features).sort_values(ascending=False).head(15)

        fig2, ax2 = plt.subplots(figsize=(8, 6))
        sns.barplot(x=imp_df.values, y=imp_df.index, palette='viridis', ax=ax2)
        st.pyplot(fig2)

        # Waste by ingredient chart
        if 'Ingredient' in df.columns:
            st.subheader("🍅 Total Predicted Waste per Ingredient")
            ing_waste = df.groupby('Ingredient')['Predicted_Waste_kg'].sum().sort_values(ascending=False).head(10)

            fig3, ax3 = plt.subplots(figsize=(10, 5))
            sns.barplot(x=ing_waste.values, y=ing_waste.index, palette='magma', ax=ax3)
            st.pyplot(fig3)

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

else:
    st.info("📌 Please upload your final_ingredient_waste_dataset.csv file to begin.")
