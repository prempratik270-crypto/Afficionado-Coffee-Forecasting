import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Page Title
# -----------------------------
st.set_page_config(
    page_title="Coffee Sales Dashboard",
    layout="wide"
)

st.title("Coffee Sales Dashboard")
st.write("Data-Driven Forecasting & Peak Demand Prediction")

# -----------------------------
# Load Dataset
# -----------------------------
@st.cache_data
def load_data():
    return pd.read_csv("Data/processed_data.csv")

df = load_data()

# -----------------------------
# Dataset Preview
# -----------------------------
st.subheader("Dataset Preview")
st.dataframe(df.head())

# -----------------------------
# KPI Metrics
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Revenue", f"${df['Revenue'].sum():,.2f}")

with col2:
    st.metric("Total Transactions", len(df))

with col3:
    st.metric("Average Revenue", f"${df['Revenue'].mean():.2f}")

# -----------------------------
# Revenue by Hour
# -----------------------------
st.subheader("Revenue by Hour")

hourly = df.groupby("Hour")["Revenue"].sum()

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(hourly.index, hourly.values)
ax.set_xlabel("Hour")
ax.set_ylabel("Revenue")
ax.set_title("Revenue by Hour")

st.pyplot(fig)

# -----------------------------
# Revenue by Product Category
# -----------------------------
st.subheader("Revenue by Product Category")

category = (
    df.groupby("product_category")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(category.index, category.values)

plt.xticks(rotation=45)

ax.set_xlabel("Product Category")
ax.set_ylabel("Revenue")
ax.set_title("Revenue by Product Category")

st.pyplot(fig)

# -----------------------------
# Revenue by Store
# -----------------------------
st.subheader("Revenue by Store")

store = (
    df.groupby("store_location")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

fig, ax = plt.subplots(figsize=(8,4))
ax.bar(store.index, store.values)

plt.xticks(rotation=45)

ax.set_xlabel("Store")
ax.set_ylabel("Revenue")
ax.set_title("Revenue by Store")

st.pyplot(fig)

# -----------------------------
# Top 10 Products
# -----------------------------
st.subheader("Top 10 Products")

top_products = (
    df.groupby("product_detail")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

st.dataframe(top_products)

# -----------------------------
# Business Insights
# -----------------------------
st.subheader("Business Insights")

st.write("- Peak revenue hours can help optimize staff scheduling.")
st.write("- High-performing stores require better inventory planning.")
st.write("- Popular product categories contribute significantly to total revenue.")
