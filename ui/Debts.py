import streamlit as st
from ui import app
from sqlalchemy import text

st.title("Debts Table")

debt = app.conn.execute(text("SELECT * FROM debts;"))
st.dataframe(debt)