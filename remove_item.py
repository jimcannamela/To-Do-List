# remove an item from the list

def remove_item(item,tasklist):
    if item in tasklist:
        del tasklist[item]
        return "Item removed from the list."
    else:
        return "Task doesn't exists in your to do list."

### End of Module ###