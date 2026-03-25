import streamlit as st
from ui import app
from sqlalchemy import text

st.title("Transactions Table")

transaction = app.conn.execute(text("SELECT * FROM transactions;"))
st.dataframe(transaction)