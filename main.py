# To Do List
import json
import os
from datetime import datetime
from services.addTodo import addTodo

# ------------------------------------------------------

operation = {
    1: "listTodo",
    2: "addTodo",
    3: "edit_todo",
    4: "completeTodo",
    5: "delete_todo",
}


folder_name = "My_Todos"
current_dir = os.getcwd()
folder_path = os.path.join(current_dir, folder_name)
os.makedirs(folder_path, exist_ok = True)


def get_user_choice(arr):
    while True:
        userchoice = input("Enter your operation number : ")
        try:
            if int(userchoice) not in arr:
                print("This operation is not listed Yet !!")
            elif int(userchoice) in arr:
                return int(userchoice)
        except Exception as e:
            print("Enter a valid number")


def list_todos():
    listOfFiles = os.listdir(folder_path)
    useOptions = {}

    if (len(listOfFiles) > 0):
        print('''
    These are the list of the todo tasks, Which one do you wannt to open ??
    ''')
        for index, file in enumerate(listOfFiles):
            useOptions.update({ index+1 : file })
            print(f"{index + 1}. {file}")

        userListChoice = get_user_choice(useOptions)

        filename = useOptions[userListChoice]

        file_path = os.path.join(folder_path, filename)
        try:
            with open(file_path, "r") as file:
                content = file.read()
                print(f'''{content}''')
        except Exception as e:
                print(f"Could not read {filename}: {e}")
    else:
        print("No such To-Do Added Yet !!")


def list_todos_for_select(ele):
    print(f"{ele['id']} : {ele['Title']}")
    pass


def mark_as_completed():
    print('''
    These are some group of the todo tasks, In which from do you wanna mark as complete ??
    ''')
    listOfFiles = os.listdir(folder_path)
    useOptions = {}

    for index, file in enumerate(listOfFiles):
        useOptions.update({ index+1 : file })
        print(f"{index + 1}. {file}")

    userMarkChoice = get_user_choice(useOptions)

    filename = useOptions[userMarkChoice]

    file_path = os.path.join(folder_path, filename)

    try:
        with open(file_path, "r") as file:
            content = file.read()
            if not content.strip():
                raise ValueError("File is empty")

            todos = json.loads(content)

            for todo in todos:
                list_todos_for_select(todo)

        userTodoChoice = get_user_choice(list(map(lambda x: x['id'],todos)))
        
        for todo in todos:
            if todo["id"] == userTodoChoice:
                todo["isCompleted"] = True
                break

        with open(file_path, "w") as file:
            json.dump(todos, file, indent=4)
        print(f"Todo with id {userTodoChoice} marked as complete.")
            
    except Exception as e:
            print(f"Could not read {filename}: {e}")


def edit_todo():
    pass


def delete_todo():
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


user_choice = get_user_choice(operation)


match int(user_choice):
    case 1:
        list_todos()
    case 2:
        addTodo(folder_path)
    case 3:
        edit_todo()
    case 4:
        mark_as_completed()
    case 5:
        delete_todo()


