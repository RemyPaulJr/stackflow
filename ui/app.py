import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from models import config

conn = config.session

pg = st.navigation(["About.py", "Transactions.py", "SavingsGoals.py"])
pg.run()