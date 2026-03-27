import streamlit as st
from ui import app
from sqlalchemy import text

st.title("Portfolio Snapshots Table")

portfolio_snapshot = app.conn.execute(text("SELECT * FROM portfolio_snapshot;"))
st.dataframe(portfolio_snapshot)