'''
Project B

Objective:

Build a simple command-line To-Do list application where users can add, remove, view, and mark tasks completed.

Features:

View tasks: Users should be able to see a list of their tasks, each with a status indicating whether it is pending or completed.

Add Tasks: Users should be able to add new tasks to their list.

Remove tasks: Users should have the option to remove tasks from the list

Mark Tasks as Completed

Hints:

Think about what data structure will be most useful in this application to hold your tasks.
Implement functions for each feature: viewing tasks, adding new tasks, removing tasks, and marking tasks as completed.
Create a loop that keeps the program running and displays a menu of options for the user to choose from (view, add, remove, complete a task, and exit)

Improvements:

Implement error handling to manage user inputs
Allow for task editing
Sort tasks by status or creation date
Implement categories or tags for tasks
Focus on getting the basic functionality working before moving to more advanced features. The takeaway from this project is to practice manipulating 
lists and dictionaries, working with loops, and handling user input in Python

'''

# Task
#    Date Entered
#    Date Completed
#    Due Date
#    Categories
#    Tags

#    completed ind
#    task name

# Methods
#    view all tasks
#    Add Tasks
#    Remove tasks

#  maintain state of the task list - write to csv or text???
import datetime

def todolist(operation:str, taskname:str) -> dict: 
    try:
        # add a new task
        if operation == 'A':
            # handle duplicate tasks
            if taskname not in tasklist:
                tasklist[taskname]={'status':'incomplete', 'date_entered': datetime.datetime.today() }
            else:
                print("Task already exists in your to do list.")
        # update a task to completed
        elif operation == 'C':
            if taskname in tasklist:
#                tasklist[taskname]={'status':'complete'} #  ERROR HERE, the date is lost at this point
                tasklist[taskname]['status']='complete'  # <--- try this
            else:
                print("Task doesn't exists in your to do list.")
        # remove a task
        elif operation == 'R':
            if taskname in tasklist:
                del tasklist[taskname]
            else:
                print("Task doesn't exists in your to do list.")
      
        # view all tasks  
        #elif operation == 'V':
        return tasklist

    except:
       raise ValueError

    
print("Welcome to the Edgar/Jim To Do List")

print("What would you like to do?")
print("    V to view tasks")
print("    A to add a new task")
print("    R to remove a task")
print("    C to mark a task complete")
print("    X to end the program")

operation = ' '
# tasklist = {}
tasklist={'Weed garden': {'status': 'complete', 'date_entered': '2024-07-15 00:00:00.000000'}   \
          , 'Walk dog': {'status': 'incomplete', 'date_entered': '2024-05-15 00:00:00.000000'}  \
          , 'Feed cat': {'status': 'incomplete', 'date_entered': '2024-04-15 00:00:00.000000'}  \
          , 'Read paper': {'status': 'incomplete', 'date_entered': '2024-06-15 00:00:00.000000'}}

while True:
    
    while True:        
        operation = input("Please select your action: ").upper()
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

    #print(tasklist)
     # loop through tasks and display in a list
    print (f"\tItem List\n")

    for key in tasklist.keys():
    
        if tasklist[key].get('status') == 'incomplete':
            box="\U000025FB"
        else:
            box="\U00002705"
        
        mydate=str(tasklist[key].get('date_entered'))

        print(f"{box} \t {key} \t {mydate[5:7]}-{mydate[8:10]}-{mydate[0:4]}")
