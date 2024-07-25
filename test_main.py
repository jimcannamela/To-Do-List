import pytest
import main

def test_add_item():
    test_item='Test Item'
    main.todolist('A',test_item)
    assert test_item 