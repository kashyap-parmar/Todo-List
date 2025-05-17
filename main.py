# To Do List
import json
import os
from datetime import datetime

operation = {
    1: "listTodo",
    2: "addTodo",
    3: "editTodo",
    4: "completeTodo",
    5: "deleteTodo",
}

current_dir = os.getcwd()
folder_name = "My_Todos"
folder_path = os.path.join(current_dir, folder_name)

def getUserChoice(arr):
    while True:
        userchoice = input("Enter your operation number : ")
        try:
            if int(userchoice) not in arr:
                print("This operation is not listed Yet !!")
            elif int(userchoice) in arr:
                return int(userchoice)
        except Exception as e:
            print("Enter a valid number")

def addTodo():
    title = input("Enter your to-do title here :")
    description = input("Enter your to-do description here :")

    os.makedirs(folder_path, exist_ok=True)

    today_str = datetime.today().strftime("%d-%b-%Y")

    file_path = os.path.join(folder_path, f"{today_str}_todo.json")

    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, "r") as json_file:
            try:
                data = json.load(json_file)
            except json.JSONDecodeError:
                data = []
    else:
        data = []

    # Ensure it's a list to append to
    if not isinstance(data, list):
        data = [data]

    data.append({
        "Title" : title, 
        "Description" : description, 
        "id": len(data) + 1
    })

    with open(file_path, "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print('''
    Yeeey ! You have successfully Added your task !!!
    ''')

def listTodos():
    print('''
    These are the list of the todo tasks, Which one do you wannt to open ??
    ''')
    listOfFiles = os.listdir(folder_path)
    useOptions = {}

    for index, file in enumerate(listOfFiles):
        useOptions.update({ index+1 : file })
        print(f"{index + 1}. {file}")

    userListChoice = getUserChoice(useOptions)

    filename = useOptions[userListChoice]

    file_path = os.path.join(folder_path, filename)
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(f'''{content}''')
    except Exception as e:
            print(f"Could not read {filename}: {e}")
       

print(
    """
Hello ! This is Your To-do list project

You can perform these operations:
1. List of all the task
2. Add new To-Do task
3. Edit any perticular task
4. Mark as complete any task
5. Delete a perticular task
"""
)


userChoice = getUserChoice(operation)

if int(userChoice) == 1 :
    listTodos()
elif int(userChoice) == 2 :
    addTodo()


