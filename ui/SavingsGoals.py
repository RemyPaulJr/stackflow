import streamlit as st
from ui import app
from sqlalchemy import text
from models import savings_goals

st.title("Savings Goals table")

saving_goals = app.conn.execute(text("SELECT * FROM savings_goals;"))
st.dataframe(saving_goals)

instance = savings_goals.SavingsGoals()
result = instance.calculate_Trajectory(app.conn,1)
st.metric(label="Saving goal with id 1 has is expected be paid of in amount of months:", value=result)