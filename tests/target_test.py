import pytest
from your_module import (
    insert_target,
    find_target_by_id,
    delete_target_by_id,
    update_target,
    get_all_targets,
    Targets,
    Success,
    Failure,
    Maybe,
    Nothing
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_database_setup import Base  # Import your Base class for SQLAlchemy

# Database setup for testing
TEST_DATABASE_URL = "postgresql://username:password@localhost/test_db"


@pytest.fixture(scope="module")
def test_db():
    engine = create_engine(TEST_DATABASE_URL)
    Base.metadata.create_all(engine)  # Create all tables
    connection = engine.connect()
    transaction = connection.begin()

    yield connection  # This will be used in the tests

    transaction.rollback()
    connection.close()
    Base.metadata.drop_all(engine)  # Cleanup


@pytest.fixture()
def target_data(test_db):
    # Insert initial data if needed (e.g., cities, target types)
    pass  # You can implement this if you need initial data


@pytest.fixture()
def new_target():
    return Targets(
        target_industry="Test Industry",
        city_id=1,  # Make sure this exists in your test setup
        target_type_id=1,  # Make sure this exists in your test setup
        target_priority=1
    )


def test_insert_target(new_target):
    result = insert_target(new_target)
    assert isinstance(result, Success), "Insert failed"
    assert result.value.target_industry == "Test Industry"


def test_find_target(new_target):
    insert_target(new_target)  # Insert to find later
    result = find_target_by_id(new_target.target_id)
    assert result.is_not_nothing(), "Target not found"


def test_update_target(new_target):
    insert_result = insert_target(new_target)
    target_id = insert_result.value.target_id

    updated_data = Targets(
        target_industry="Updated Industry",
        city_id=2,  # Use an existing city ID
        target_type_id=1,  # Use an existing target type ID
        target_priority=2
    )
    update_result = update_target(target_id, updated_data)
    assert isinstance(update_result, Success), "Update failed"
    assert update_result.value.target_industry == "Updated Industry"


def test_delete_target(new_target):
    insert_result = insert_target(new_target)
    target_id = insert_result.value.target_id

    delete_result = delete_target_by_id(target_id)
    assert isinstance(delete_result, Success), "Delete failed"

    # Ensure the target no longer exists
    assert find_target_by_id(target_id) == Nothing


def test_get_all_targets(target_data):
    insert_target(new_target())  # Add a target to retrieve
    all_targets = get_all_targets()
    assert isinstance(all_targets, list), "Should return a list"
    assert len(all_targets) > 0, "List should not be empty"