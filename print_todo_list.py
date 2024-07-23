# Display tasklist

def print_todo_list(tasklist):
    # loop through tasks and display in a list
    print (f"\tItem List\n")

    for key in tasklist.keys():
    
        if tasklist[key].get('status') == 'incomplete':
            box="\U000025FB"
        else:
            box="\U00002705"
        
        mydate=str(tasklist[key].get('date_entered'))

        print(f"{box} \t {key} \t {mydate[5:7]}-{mydate[8:10]}-{mydate[0:4]}")

### End of Module ###