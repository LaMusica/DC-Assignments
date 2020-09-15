

# multi-line syntax

tasks = []

print("""
        1: Add new Task
        2: Delete Task
        3: Display all Tasks
        q: Quit
      """)
while True:
    act = input("Choose Action:  ")

    if act == "1":
    # ask user for task name 
        task_name = input("Enter Task:  ")

    # ask user for priority level 

        pri_gauge = input("Enter Priority Level (low, mid, or high): ")

    

        task = {"name": task_name, "priority": pri_gauge}

     # save tasks to an list of tasks 

    
        tasks.append(task)

    if act == "3":
        for i in range(0,len(tasks)):
            task = tasks[i]
            # go to 29:00 on day 5 video to understand why 
            # using "Double quotes won't work in string interpolation "
           
        
            print(f'{task["name"]} - {task["priority"]}')
            #print(i)
    
#cant get this to print 

        print(tasks)
    elif act == "q":
        break 