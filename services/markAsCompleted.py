import json
import os
from services.getUserChoice import get_user_choice

# ------------------------------------------------------------------------

def mark_as_completed(folder_path):
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
                print(f"{todo['id']} : {todo['Title']}")

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
