import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Page configuration
st.set_page_config(page_title="Ingredient Waste Predictor", page_icon="🥦", layout="wide")

st.title(":green[Ingredient Waste Prediction App] 🥦")
st.markdown("Upload your restaurant ingredient & sales dataset to predict waste per ingredient.")

# Load model and encoder columns
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

@st.cache_resource
def load_encoder_columns():
    return joblib.load("encoder_columns.pkl")

model = load_model()
encoder_columns = load_encoder_columns()

# Sidebar
with st.sidebar:
    st.header("🔧 Settings")
    prediction_threshold = st.slider("Show predictions above (kg):", 0.0, 20.0, 2.0, step=0.5)
    st.markdown("---")

# File upload
uploaded_file = st.file_uploader("Upload your ingredient & sales data CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.success("✅ File uploaded successfully!")

        with st.expander("📊 View Raw Uploaded Data"):
            st.dataframe(df.head())

        # Feature Engineering
        df['Date'] = pd.to_datetime(df['Date'])
        df['Year'] = df['Date'].dt.year
        df['Month'] = df['Date'].dt.month
        df['Day'] = df['Date'].dt.day
        df['DayOfWeek'] = df['Date'].dt.dayofweek

        df['Weather'] = df['Weather'].fillna('Unknown') if 'Weather' in df else 'Unknown'
        df['Holiday'] = df['Holiday'].fillna('No') if 'Holiday' in df else 'No'
        for col in ['Expected_Ingredient_Usage_kg', 'Purchased_Qty_kg', 'Quantity_Used', 'Is_Weekend']:
            if col in df.columns:
                df[col] = df[col].fillna(0)

        categorical_cols = ['Ingredient']
        if 'Weather' in df.columns: categorical_cols.append('Weather')
        if 'Holiday' in df.columns: categorical_cols.append('Holiday')

        df_encoded = pd.get_dummies(df, columns=categorical_cols, drop_first=True)

        for col in encoder_columns:
            if col not in df_encoded.columns:
                df_encoded[col] = 0
        df_encoded = df_encoded[encoder_columns]

        # Predict
        predictions = model.predict(df_encoded)
        df['Predicted_Waste_kg'] = predictions

        tab1, tab2, tab3 = st.tabs(["Prediction Table", "Charts", "Insights"])

        with tab1:
            st.subheader("📊 Prediction Table")
            st.dataframe(df[df["Predicted_Waste_kg"] > prediction_threshold][['Date', 'Ingredient', 'Predicted_Waste_kg']])

            csv = df.to_csv(index=False).encode()
            st.download_button("Download Full Prediction CSV", csv, file_name="predicted_waste.csv", mime="text/csv")

        with tab2:
            st.subheader(":bar_chart: Waste Prediction Distribution")
            fig, ax = plt.subplots()
            sns.histplot(df['Predicted_Waste_kg'], bins=20, kde=True, ax=ax, color='skyblue')
            ax.set_xlabel("Predicted Waste (kg)")
            st.pyplot(fig)

            st.subheader(":chart_with_upwards_trend: Monthly Waste Trend")
            df['MonthYear'] = df['Date'].dt.to_period("M")
            trend = df.groupby("MonthYear")["Predicted_Waste_kg"].sum().reset_index()
            fig2 = px.line(trend, x="MonthYear", y="Predicted_Waste_kg", markers=True)
            st.plotly_chart(fig2)

        with tab3:
            st.subheader("Top 10 Ingredients by Predicted Waste")
            top_ing = df.groupby("Ingredient")["Predicted_Waste_kg"].sum().sort_values(ascending=False).head(10)
            fig3, ax3 = plt.subplots()
            sns.barplot(x=top_ing.values, y=top_ing.index, ax=ax3, palette='magma')
            st.pyplot(fig3)

            st.subheader("Feature Importance")
            importances = model.feature_importances_
            features = encoder_columns
            imp_df = pd.Series(importances, index=features).sort_values(ascending=False).head(15)

            fig4, ax4 = plt.subplots(figsize=(8, 6))
            sns.barplot(x=imp_df.values, y=imp_df.index, ax=ax4, palette='viridis')
            st.pyplot(fig4)

    except Exception as e:
        st.error(f"Error reading file: {e}")
else:
    st.info("Please upload your final_ingredient_waste_dataset.csv file to begin.")
