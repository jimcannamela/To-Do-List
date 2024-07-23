# mark an item complete

def complete_item(item,tasklist):
    if item in tasklist:
        tasklist[item]['status']='complete'
        return "Task marked complete."
    else:
        return "Task doesn't exists in your to do list."

### End of Module ###