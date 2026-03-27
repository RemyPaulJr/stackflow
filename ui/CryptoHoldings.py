import streamlit as st
from ui import app
from sqlalchemy import text
from models import crypto_holding
from ui import app

st.title("Crypto Holdings Table")

crypto_holdings = app.conn.execute(text("SELECT * FROM crypto_holding;"))
st.dataframe(crypto_holdings)

# instance = crypto_holding.CryptoHolding()
# result = instance.get_portfolio_value(app.conn)
# st.metric(label="Current portfolio value is: ", value=result)