import pytest
import add_item
import remove_item
import complete_item

tasklist={'Weed garden': {'status': 'complete', 'date_entered': '2024-07-15 00:00:00.000000'}   \
          , 'Walk dog': {'status': 'incomplete', 'date_entered': '2024-05-15 00:00:00.000000'}  \
          , 'Feed cat': {'status': 'incomplete', 'date_entered': '2024-04-15 00:00:00.000000'}  \
          , 'Read paper': {'status': 'incomplete', 'date_entered': '2024-06-15 00:00:00.000000'}}

#### HAPPY PATH ###

def test_add_item():
    test_item='Test Item'
    return_str=add_item.add_item(test_item,tasklist)
    assert test_item in tasklist
    assert return_str == "Item successfully added."

def test_remove_item():
    test_item='Test Item'
    return_str=remove_item.remove_item(test_item,tasklist)
    assert test_item not in tasklist
    assert return_str == "Item removed from the list."

def test_completed():
    test_item='Test Item'
    add_item.add_item(test_item,tasklist)
    return_str=complete_item.complete_item(test_item,tasklist)
    assert tasklist[test_item].get('status') == 'complete'
    assert return_str == "Task marked complete."

### NON-HAPPY PATH ###

def test_add_dup_item():
    test_item='Test Item'
    add_item.add_item(test_item,tasklist)
    return_str=add_item.add_item(test_item,tasklist)
    assert return_str == "Task already exists in your to do list."

def test_remove_item_not_found():
    test_item='Test Item2'
    return_str=remove_item.remove_item(test_item,tasklist)
    assert return_str == "Task doesn't exists in your to do list."

def test_completed_not_found():
    test_item='Test Item3'
    return_str=complete_item.complete_item(test_item,tasklist)
    assert return_str == "Task doesn't exists in your to do list."