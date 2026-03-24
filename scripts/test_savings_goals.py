from datetime import datetime
from models import savings_goals, enums
import pytest

saving_goal = savings_goals.SavingsGoals(
    name="House",
    target_amount="100000.00",
    current_amount="33000.00",
    deadline=datetime(2026,4,1),
    monthly_contribution="5.00",
    description="Saving for my new amazing home!",
    status=enums.SavingsGoalsStatusEnum.active   
)

@pytest.fixture(scope="module")
def a_create_SavingsGoals(session):
    new_SavingsGoals = saving_goal.add_SavingsGoals(session)
    results = saving_goal.get_SavingsGoals(session, new_SavingsGoals.id)
    print("\n\nTesting create method....")
    print(f"Successfully created SavingsGoals {results.id} with description:", results.description)
    return results.id, results.description
   
def test_b_read_SavingsGoals(a_create_SavingsGoals, session):
    get = saving_goal.get_SavingsGoals(session, a_create_SavingsGoals[0])
    print("\nTesting read method....")
    print("Successfully read SavingsGoals", get.id)

def test_c_update_SavingsGoals(a_create_SavingsGoals, session):
    update = saving_goal.update_SavingsGoals(session, a_create_SavingsGoals[0], description="Saving for my Mom's new amazing home.")
    print("\nTesting update method....")
    print(f"Successfully updated SavingsGoals {update.id} with description:", update.description)

def test_d_delete_SavingsGoals(a_create_SavingsGoals, session):
    delete = saving_goal.delete_SavingsGoals(session, a_create_SavingsGoals[0])
    print("\nTesting delete method....")
    print("Successfully deleted SavingsGoals:", delete.id)