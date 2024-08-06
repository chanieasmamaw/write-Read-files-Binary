"""
The Task Manager Program

Write a multi-file program that simulates a task manager.


Two main files
def_filetaskmanager()


The 3 different files should be responsible for the following:
- The views (communication with the users through the termina)
- The repository (stores the tasks)
- The main program (the program that runs the task manager)

The program should allow the user to:
- add tasks 
- display the tasks 
- mark tasks as completed
- delete tasks

The task has
- a name
- a status (completed or not)

The execution of the program should look like this:

Task Manager
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Choose an option: 1
Enter task description: Learn to code
Task added with ID 3.

Task Manager
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Choose an option: 2
ID: 1, Description: Laundry, Status: Incomplete
ID: 2, Description: Dishes, Status: Incomplete
ID: 3, Description: Learn to code, Status: Incomplete

Task Manager
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Exit
Choose an option: ....
etc.
"""
    
#1.Body for Taskmanager
def display_menu():
  print("Taskmanager")
  print("Add Task"- "or choose")
  print("View Task")
  print("Update Task")
  print("Delete Task")
  print("Exit")
  
# Functions of the Body of Taskmanager

#A)Get Task Description or Legend


def get_task_description():
  pass

task_list = [] #{}
task_list = ['painting', 'cleaning', 'Learn to code']
#task_list = {
 # 'painting':1, 'cleaning':2, 'Learn to code':3}


#1. Add Task ()
def adding_task_to_manager(task_list):
  user_adds_task = input("What task would you like to add? ")
  task_list = task_list.append(user_adds_task)
  print(f"{user_adds_task} was added to the taskmanager")


#should we ousource the task list here for better structure?
def display_taskmanager(task_list):
  for index, task in enumerate(task_list):
    print(f"\n{index + 1}: {task}")   


#2. View Task (?) Updated or original?
def get_all_tasks():
  
  #task_list= [0] 
  pass
  
#Reset Task Manager for Debugging

# modified List of Tasks (List get's too long or replace the old ones?)
old_task = task_list 
updated_tasks = task_list + task_list
copy_updated_tasks = set(updated_tasks) #if it looks like this("task,1","task,2" etc.)


#3. Update task
def update_tasks(task_list):
  task_to_update = input("Which task would you like to update? (Provide the task description): ")

  if task_to_update in task_list:
    new_task_description = input("What do you want to name it? ")

    for i, task in enumerate(task_list):
      if task == task_to_update:
        task_list[i] = new_task_description
        print(f"Task '{task_to_update}' updated to '{new_task_description}'.")
        break
  else:
    print("This task is not in the list")


# Example usage
#task_list = ['painting', 'cleaning', 'Learn to code']
#update_tasks(task_list)
print(task_list)

      
# A) How to get task description "Help" or legend(Overview)?  


#4. Delete task
def delete_task(task_list):
  delete_task = input("Which task would you like to delete? ")
  if delete_task in task_list:
    task_list.remove(delete_task) # Keep pop- function in mind to improve functionality;)
    print(f"'{delete_task}' was removed from the task manager.")
  else:
    print("This task is not in the list")
    
    # Example usage
  #task_list = ['painting', 'cleaning', 'Learn to code']
  
#delete_task(task_list)
#print(task_list)
          
#function of the Taskmanager
#Manager should print the Description of each Task(Better should have ID's while calling?):

#description=
#task=
#print()
# Manager should get and run the function choosen from ch_f_list

# Get the User choice
while True:
  #task_list = []
  ch_f_list = int(input(
      "\n---------Task Manager---------\nMenu:\n1.Add Task\n2.View Tasks\n3.Update Task\n4.Delete Task\n5.Exit\nEnter choice (1-5): "))
  if ch_f_list == 1:  
    adding_task_to_manager(task_list)
  elif ch_f_list == 2:
    display_taskmanager(task_list)
  elif ch_f_list == 3:
    update_tasks(task_list)
  elif ch_f_list == 4:
    delete_task(task_list)
  elif ch_f_list == 5:
    print("Goodbye")
    break
  else:
    print("invalid input")
    

