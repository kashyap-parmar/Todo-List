# To Do List
import os
from services.addTodo import addTodo
from services.markAsCompleted import mark_as_completed
from services.getUserChoice import get_user_choice
from services.listTodos import list_todos
from services.editTodo import edit_todo
from services.deleteTodo import delete_todo

# ------------------------------------------------------

operation = {
    1: "listTodo",
    2: "addTodo",   +
    3: "edit_todo",
    4: "completeTodo",
    5: "delete_todo",
}


folder_name = "My_Todos"
current_dir = os.getcwd()
folder_path = os.path.join(current_dir, folder_name)
os.makedirs(folder_path, exist_ok = True)


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
        list_todos(folder_path)
    case 2:
        addTodo(folder_path)
    case 3:
        edit_todo(folder_path)
    case 4:
        mark_as_completed(folder_path)
    case 5:
        delete_todo(folder_path)


