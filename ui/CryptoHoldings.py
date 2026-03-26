import streamlit as st
from ui import app
from sqlalchemy import text

st.title("Crypto Holdings Table")

crypto_holding = app.conn.execute(text("SELECT * FROM crypto_holding;"))
st.dataframe(crypto_holding)