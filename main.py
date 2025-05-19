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
       
def listTodosFforSelect(ele):
    print(f"{ele['id']} : {ele['Title']}")
    pass

def markAsCompleted():
    print('''
    These are some group of the todo tasks, In which from do you wanna mark as complete ??
    ''')
    listOfFiles = os.listdir(folder_path)
    useOptions = {}

    for index, file in enumerate(listOfFiles):
        useOptions.update({ index+1 : file })
        print(f"{index + 1}. {file}")

    userMarkChoice = getUserChoice(useOptions)

    filename = useOptions[userMarkChoice]

    file_path = os.path.join(folder_path, filename)

    try:
        with open(file_path, "r") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("File is empty")

            todos = json.loads(content)

            for todo in todos:
                listTodosFforSelect(todo)

        userTodoChoice = getUserChoice(list(map(lambda x: x['id'],todos)))
        
        for todo in todos:
            if todo["id"] == userTodoChoice:
                todo["isCompleted"] = True
                break

        with open(file_path, "w") as file:
            json.dump(todos, file, indent=4)
        print(f"Todo with id {userTodoChoice} marked as complete.")
            
    except Exception as e:
            print(f"Could not read {filename}: {e}")

def editTodo():
    pass

def deleteTodo():
    pass

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

match int(userChoice):
    case 1:
        listTodos()
    case 2:
        addTodo()
    case 3:
        editTodo()
    case 4:
        markAsCompleted()
    case 5:
        deleteTodo()


