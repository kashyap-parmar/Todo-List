import os
import json
from services.getUserChoice import get_user_choice

# -------------------------------------------------------

def list_todos(folder_path):
    listOfFiles = os.listdir(folder_path)
    useOptions = {}

    if (len(listOfFiles) > 0):
        print('''
    These are the list of the todos, Which one do you wanna open ??
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
                if len(content.strip()) > 0:
                    try:
                        todos = json.loads(content)  # Convert string to Python object
                        if isinstance(todos, list):  # ✅ check if it's a list
                            showtodos = list(filter(lambda x: not x.get('is_deleted', False), todos))
                            print(f'''{json.dumps(showtodos, indent=4)}''')
                        else:
                            print(f'''{content}''')
                    except json.JSONDecodeError:
                        print("Invalid JSON format.")
                else:
                    print("There are no any todos available")
        except Exception as e:
                print(f"Could not read {filename}: {e}")
    else:
        print("No such To-Do Added Yet !!")