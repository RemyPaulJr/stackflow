import pytest
from models import crypto_holding

crypto_holdings = crypto_holding.CryptoHolding(
    name="ethereum",
    symbol="eth",
    quantity="2",
    avg_purchase_price="200.00"
)

@pytest.fixture(scope="module")
def a_create_crypto_holding(session):
    new_crypto_holding = crypto_holdings.add_crypto_holding(session)
    results = crypto_holdings.get_crypto_holding(session, new_crypto_holding.id)
    print("\n\nTesting create method....")
    print(f"Successfully created crypto_holding {results.id} with a quantity:", results.quantity)
    return results.id, results.quantity
   
def test_b_read_crypto_holding(a_create_crypto_holding, session):
    get = crypto_holdings.get_crypto_holding(session, a_create_crypto_holding[0])
    print("\nTesting read method....")
    print("Successfully read crypto_holding", get.id)

def test_c_update_crypto_holding(a_create_crypto_holding, session):
    update = crypto_holdings.update_crypto_holding(session, a_create_crypto_holding[0], quantity="5.00")
    print("\nTesting update method....")
    print(f"Successfully updated crypto_holding {update.id} with a quantity:", update.quantity)

def test_d_delete_crypto_holding(a_create_crypto_holding, session):
    delete = crypto_holdings.delete_crypto_holding(session, a_create_crypto_holding[0])
    print("\nTesting delete method....")
    print("Successfully deleted crypto_holding:", delete.id)