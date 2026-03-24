import pytest
from models import investments

investment = investments.Investments(
    account_type="brokerage",
    ticker="TSLA",
    shares="10",
    avg_cost_basis="5"
)

@pytest.fixture(scope="module")
def a_create_investment(session):
    new_investment = investment.add_investment(session)
    results = investment.get_investment(session, new_investment.id)
    print("\n\nTesting create method....")
    print(f"Successfully created investment {results.id} with {results.shares} shares")
    return results.id, results.shares
   
def test_b_read_investment(a_create_investment, session):
    get = investment.get_investment(session, a_create_investment[0])
    print("\nTesting read method....")
    print("Successfully read investment", get.id)

def test_c_update_investment(a_create_investment, session):
    update = investment.update_investment(session, a_create_investment[0], quantity="5.00")
    print("\nTesting update method....")
    print(f"Successfully updated investment {update.id} with {update.shares} shares")

def test_d_delete_investment(a_create_investment, session):
    delete = investment.delete_investment(session, a_create_investment[0])
    print("\nTesting delete method....")
    print("Successfully deleted investment:", delete.id)