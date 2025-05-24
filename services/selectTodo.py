import os
import json
from services.getUserChoice import get_user_choice

# --------------------------------------------------

def select_todo(folder_path):
    
    listOfFiles = os.listdir(folder_path)
    useOptions = {}

    if len(listOfFiles) > 0:
        print('''
    These are some group of the todo tasks, In which from do you wanna perform operation ??
    ''')
        for index, file in enumerate(listOfFiles):
            useOptions.update({ index+1 : file })
            print(f"{index + 1}. {file}")
    else:
        print("There are no any To-Dos available")
        return

    userMarkChoice = get_user_choice(useOptions)

    filename = useOptions[userMarkChoice]

    file_path = os.path.join(folder_path, filename)

    try:
        with open(file_path, "r") as file:
            if os.path.getsize(file_path) == 0:
                print(f"⚠️  Could not read {os.path.basename(file_path)}: File is empty")
                return None
            content = file.read()
            if not content.strip():
                raise ValueError("File is empty")

            todos = json.loads(content)
        return {"data" : todos, "filename" : filename}
    except Exception as e:
        print(f"Could not read {filename}: {e}")