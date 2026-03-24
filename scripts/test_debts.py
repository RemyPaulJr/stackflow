import pytest
from models import debts

debt = debts.Debts(
    name="AMEX",
    balance="1000.00",
    interest_rate="10.50",
    minimum_payment="5.00",
    debt_type="credit_card"
)

@pytest.fixture(scope="module")
def a_create_debt(session):
    new_debt = debt.add_debt(session)
    results = debt.get_debt(session, new_debt.id)
    print("\n\nTesting create method....")
    print(f"Successfully created debt {results.id} with balance:", results.balance)
    return results.id, results.balance
   
def test_b_read_debt(a_create_debt, session):
    get = debt.get_debt(session, a_create_debt[0])
    print("\nTesting read method....")
    print("Successfully read debt", get.id)

def test_c_update_debt(a_create_debt, session):
    update = debt.update_debt(session, a_create_debt[0], balance="500.00")
    print("\nTesting update method....")
    print(f"Successfully updated debt {update.id} with balance:", update.balance)

def test_d_delete_debt(a_create_debt, session):
    delete = debt.delete_debt(session, a_create_debt[0])
    print("\nTesting delete method....")
    print("Successfully deleted debt:", delete.id)