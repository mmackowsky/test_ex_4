import pytest
from pytest_mock import mocker
from testy_jednostkowe.ex_4.main.src import todos, check_pos, add_todo, remove_todo, edit_todo, remove_all


@pytest.fixture
def todos_fix(mocker):
    mocker.patch('testy_jednostkowe.ex_4.main.src.todos', ["Clean my room", "Make my bed"])

def test_add_todo(todos_fix):
    add_todo("Go to bed")
    assert todos == ["Clean my room", "Make my bed", "Go to bed"]


def test_remove_todo(todos_fix):
    remove_todo(0)
    assert todos == ["Make my bed"]


def test_edit_todo(todos_fix):
    edit_todo(0, "Vacuum my room")
    assert todos == ["Vacuum my room", "Make my bed"]


def test_remove_all(todos_fix):
    remove_all()
    assert todos == []





