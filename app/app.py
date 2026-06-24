import sqlite3
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(
    page_title="Finance Dashboard",
    layout="wide"
)

conn = sqlite3.connect("data/data.db")
df = pd.read_sql("SELECT * FROM transactions", conn)

st.title("Finance Dashboard")

if df.empty:
    st.warning("No transactions found. Import a CSV file to begin.")
    st.stop()

df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
df = df.dropna(subset=["amount"])
df["category"] = df["category"].fillna("Other")

df["type"] = df["amount"].apply(lambda x: "Income" if x > 0 else "Expense")

st.sidebar.header("Filters")

categories = ["All"] + sorted(df["category"].unique().tolist())
selected_category = st.sidebar.selectbox("Category", categories)

type_filter = st.sidebar.selectbox("Type", ["All", "Income", "Expense"])

filtered = df.copy()

if selected_category != "All":
    filtered = filtered[filtered["category"] == selected_category]

if type_filter != "All":
    filtered = filtered[filtered["type"] == type_filter]

total_spent = filtered[filtered["amount"] < 0]["amount"].sum()
total_income = filtered[filtered["amount"] > 0]["amount"].sum()
net = filtered["amount"].sum()

col1, col2, col3 = st.columns(3)

col1.metric("Spending", f"${abs(total_spent):,.2f}")
col2.metric("Income", f"${total_income:,.2f}")
col3.metric("Net", f"${net:,.2f}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("Spending by Category")

    expenses = filtered[filtered["amount"] < 0]
    cat_data = expenses.groupby("category")["amount"].sum().abs().reset_index()

    fig = px.bar(
        cat_data,
        x="category",
        y="amount",
        title="Expenses by Category"
    )
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Income vs Expenses")

    type_data = filtered.groupby("type")["amount"].sum().reset_index()

    fig2 = px.pie(
        type_data,
        names="type",
        values="amount",
        title="Income vs Expenses"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.divider()

st.subheader("Transactions")

st.dataframe(
    filtered.sort_values("amount"),
    use_container_width=True,
    height=500
)