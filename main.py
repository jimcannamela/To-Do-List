# My To Do List
import add_item
import complete_item
import remove_item
import print_menu
import print_todo_list

def todolist(operation:str, taskname:str) -> dict: 
    try:
        # add a new task
        if operation == 'A':
            print(add_item.add_item(taskname,tasklist))
        # update a task to completed
        elif operation == 'C':
            print(complete_item.complete_item(taskname,tasklist))
        # remove a task
        elif operation == 'R':
            print(remove_item.remove_item(taskname, tasklist))
        # view all tasks  
        #elif operation == 'V':
        return tasklist
    except:
       raise ValueError

# Initialize Variables
operation = ' '
# tasklist = {}
tasklist={'Weed garden': {'status': 'complete', 'date_entered': '2024-07-15 00:00:00.000000'}   \
          , 'Walk dog': {'status': 'incomplete', 'date_entered': '2024-05-15 00:00:00.000000'}  \
          , 'Feed cat': {'status': 'incomplete', 'date_entered': '2024-04-15 00:00:00.000000'}  \
          , 'Read paper': {'status': 'incomplete', 'date_entered': '2024-06-15 00:00:00.000000'}}

print_menu.print_menu()

while True:
    
    while True:        
        operation = input("Please select your action: 'A'dd 'C'omplete 'R'emove 'V'iew e'X'it => " ).upper()
        if operation in ('A', 'C', 'R', 'V', 'X'):
            break
        else:            
            print("Please enter a valid action")
            continue

    if operation =='X':
        break
    
    if operation == 'V':
        task_name=' '
    else:
        while True:
            task_name = input("Enter task name: (1-40 characters): ").capitalize()
            if 1 <= len(task_name) <= 40:
                break
            else:            
                print("Please enter a valid task name")

    #print(todolist(operation,task_name))

    todolist(operation,task_name)

    print_todo_list.print_todo_list(tasklist)

### End of Program ###