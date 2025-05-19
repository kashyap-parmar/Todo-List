import json
import os
from datetime import datetime

def addTodo(folder_path):
    title = input("Enter your to-do title here :")
    description = input("Enter your to-do description here :")

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
