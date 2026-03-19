from models import config
from sqlalchemy import text

with config.engine.connect() as conn:
    conn.execute(text("CREATE INDEX indx_trans_category ON transactions (category)"))
    conn.execute(text("CREATE INDEX indx_trans_date ON transactions (date)"))
    conn.execute(text("CREATE INDEX indx_trans_type ON transactions (type)"))
    conn.execute(text("CREATE INDEX indx_sg_status ON savings_goals (status)"))
    conn.execute(text("CREATE INDEX indx_sg_deadline ON savings_goals (deadline)"))
    conn.execute(text("CREATE INDEX indx_inv_account_type ON investments (account_type)"))
    conn.execute(text("CREATE INDEX indx_inv_ticker ON investments (ticker)"))
    conn.execute(text("CREATE INDEX indx_debt_type ON debts (debt_type)"))
    conn.execute(text("CREATE INDEX indx_debt_interest ON debts (interest_rate)"))
    conn.execute(text("CREATE INDEX indx_crypto_symbol ON crypto_holding (symbol)"))
    conn.execute(text("CREATE INDEX indx_crypto_pdate ON crypto_holding (purchase_date)"))
    conn.execute(text("CREATE INDEX indx_psnap_record ON portfolio_snapshot (recorded_at)"))
    conn.commit()