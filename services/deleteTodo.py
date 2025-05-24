import os
import json
from services.getUserChoice import get_user_choice
from services.selectTodo import select_todo

# ------------------------------------------------

def delete_todo(folder_path):
    try:
        selectedTodo = select_todo(folder_path)
        
        if selectedTodo is not None :
            filename = selectedTodo.get('filename')
            todos = selectedTodo.get("data")

            for todo in todos:
                print(f"{todo['id']} : {todo['Title']}")

            userTodoChoice = get_user_choice(list(map(lambda x : x['id'], todos)))

            with open(f"{folder_path}/{filename}", "w") as file:
                for todo in todos:
                    if (todo['id'] == userTodoChoice):
                        todo['is_deleted'] = True
                json.dump(todos, file, indent=4)
            print(f'''{json.dumps(todo, indent=4)}''')

    except Exception as e :
        print(f"Could not perform operation:", e)
    pass