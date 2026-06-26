import pytest
from pawpal_system import Owner, Pet, Task


@pytest.fixture
def owner():
    return Owner(
        first_name="Anthony",
        last_name="Goines",
        email="anthonyig45@gmail.com",
        available_minutes=90,
    )


@pytest.fixture
def pet(owner):
    return Pet(name="Biscuit", species="Dog", breed="Golden Retriever", age=3, owner=owner)


@pytest.fixture
def task():
    return Task(
        name="Morning Walk",
        duration_minutes=30,
        priority="high",
        category="exercise",
        recurrence="daily",
    )


def test_task_completion(task):
    assert task.is_completed is False
    task.mark_complete()
    assert task.is_completed is True


def test_task_addition(pet, task):
    assert len(pet.tasks) == 0
    pet.add_task(task)
    assert len(pet.tasks) == 1
