import os
from services.getUserChoice import get_user_choice

# -------------------------------------------------------

def list_todos(folder_path):
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