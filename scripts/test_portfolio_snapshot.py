import pytest
from models import portfolio_snapshot

portfolio_snapshots = portfolio_snapshot.PortfolioSnapshot(
    total_value="10",
    pnl_today="5",
    pnl_percent="3",
    btc_price="50000",
    eth_price="3000",
    sol_price="100",
    doge_price="10"
)

@pytest.fixture(scope="module")
def a_create_portfolio_snapshots(session):
    new_portfolio_snapshots = portfolio_snapshots.add_portfolio_snapshot(session)
    results = portfolio_snapshots.get_portfolio_snapshot(session, new_portfolio_snapshots.id)
    print("\n\nTesting create method....")
    print(f"Successfully created portfolio_snapshots {results.id} with {results.total_value} total value")
    return results.id, results.total_value
   
def test_b_read_portfolio_snapshots(a_create_portfolio_snapshots, session):
    get = portfolio_snapshots.get_portfolio_snapshot(session, a_create_portfolio_snapshots[0])
    print("\nTesting read method....")
    print("Successfully read portfolio_snapshots", get.id)

def test_c_update_portfolio_snapshots(a_create_portfolio_snapshots, session):
    update = portfolio_snapshots.update_portfolio_snapshot(session, a_create_portfolio_snapshots[0], total_value="40.00")
    print("\nTesting update method....")
    print(f"Successfully updated portfolio_snapshots {update.id} with {update.total_value} total value")

def test_d_delete_portfolio_snapshots(a_create_portfolio_snapshots, session):
    delete = portfolio_snapshots.delete_portfolio_snapshot(session, a_create_portfolio_snapshots[0])
    print("\nTesting delete method....")
    print("Successfully deleted portfolio_snapshots:", delete.id)