from collections import Counter
import json
from datetime import date

emptyDoc = False

#task_count = 0
task_count = None
with open("todoDB.json", "r") as f:
    data = json.load(f)
if len(data) != 0:
    length_of_task = len(data["today"])
    task_count = length_of_task
else:
    task_count = 0

while True:
    with open("todoDB.json", "r") as f:
        todoData = json.load(f)
    # f=open("todoDB.json","r")
    # todoData=json.load(f)
    # print(todoData,type(todoData))

    currentDate = date.today()
    Counter
    if len(todoData) == 0:
        emptyDoc = True
        username = input(
            "\nHii there!! Welcome to TodoCLI. Please enter your username")
        todoData["name"] = username
        todoData["date"] = str(currentDate)
        print(f"Hey {username}! i hope you have a good start of the day")

        cmd = input(">>")

        print("Create a task by writing <create task> or <add task>")
        todoData["today"] = []

        if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter your task description: ")
            scheduled_time = input("\nEnter scheduled time for the task: ")

            task = {
                "task_id": task_count,
                "description": task_description,
                "scheduled_time": scheduled_time,
                "status": "TBD"
            }

            todoData["today"].append(task)

            with open("todoDB.json", "w") as f:
                json.dump(todoData, f, indent=4)
            task_count = task_count + 1

    elif "today" in list(todoData.keys()):
        # First print the existing tasks
        tasks = todoData["today"]
        username = todoData["name"]
        currDate = todoData["date"]
        print(f"Today is {date}")
        print(f"\nHey {username}, here are the tasks for your day\n")

        for task in tasks:
            #print("\nTask id", task["task_id"])
            print(f"\nTask number{tasks.index(task)+1}")
            print("\nTask Description: ", task["description"])
            print("\nScheduled time:", task["scheduled_time"])
            #print("\nStatus", task["status"])

        print("\n Create another task")
        cmd = input(">>")

        if cmd == "create task" or cmd == "add task":
            task_description = input("\nEnter your task description: ")
            scheduled_time = input("\nEnter your scheduled time: ")

            task = {
                "description": task_description,
                "scheduled_time": scheduled_time
            }

            todoData["today"].append(task)

            with open("todoDB.json", "r+") as f:
                f.seek(0)
                json.dump(todoData, f, indent=4)

            print("Task created successfully")
            print("If you want to add more task,type add task/create task")
            print("If you are done for now ,please type done")
            continue
        elif cmd == "done" or cmd == "exit":
            print("Have a good day!!")
            break
        elif cmd == "mark task as done":
            tasks = todoData["today"]
            username = todoData["name"]
            currDate = todoData["date"]
            print(f"Today is {date}")
            print(f"\nHey {username}, here are the tasks for your day\n")

        for task in tasks:
            #print("\nTask id", task["task_id"])
            print(f"\nTask number{tasks.index(task)+1}")
            print("\nTask Description: ", task["description"])
            print("\nScheduled time:", task["scheduled_time"])
            #print("\nStatus", task["status"])

        # status_cmd = input("\ntask>> ")
        task_id = int(input("\n Enter task id: "))

        for task in tasks:
            if task[task_id] == task_id:
                todoData["today"][tasks.index(task)]["status"]
            else:
                continue

        print("\n Create another task")
        cmd = input(">>")

    elif cmd == "delete task":
        with open("todo.json", "w") as f:
            json.dump({}, f, indent=4)
    print("All tasks deleted")

    # elif cmd == "delete user":
    # with open("todo.json", "w") as f:
    #     json.dump({}, f, indent=4)
    # print("User data is deleted")
