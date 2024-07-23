# add an item to the to do list

import datetime

def add_item(item,tasklist):
    # handle duplicate tasks
    if item not in tasklist:
        tasklist[item]={'status':'incomplete', 'date_entered': datetime.datetime.today() }
        return "Item successfully added."
    else:
        return "Task already exists in your to do list."
    
### End of Module ###