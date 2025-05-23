import os
import json
from services.getUserChoice import get_user_choice
from services.selectTodo import select_todo

# --------------------------------------------------

def edit_todo(folder_path):
    
    data = select_todo(folder_path)

    print(data)
    # for todo in data.todos:
    #     print(f"{todo['id']} : {todo['Title']}")

    # userTodoChoice = get_user_choice([1,2])

    # for todo in data.todos:
    #     if (todo['id'] == userTodoChoice):
    #         selectedTodo = todo

    # print('''
    # What do you want to edit? Title or Descriptions? 
    # 1. Title
    # 2. Descriptions
    # ''')

    # userEditChoice = get_user_choice([1,2])


    # if (userEditChoice == 1) :
    #     selectedTodo["Title"] = input("Enter your Title here :")
    # else:
    #     selectedTodo["Description"] = input("Enter your Description here :")

    # with open(file_path, "w") as file:
    #     for todo in todos:
    #         if todo['id'] == selectedTodo["id"]:
    #             todo = selectedTodo

    #     json.dump(todos, file, indent=4)
    
    # print("todos", todos)

    # except Exception as e:
    #     print(f"Could not read {filename}: {e}")