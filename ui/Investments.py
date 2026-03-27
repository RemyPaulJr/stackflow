import streamlit as st
from ui import app
from sqlalchemy import text

st.title("Investments Table")

investment = app.conn.execute(text("SELECT * FROM investments;"))
st.dataframe(investment)