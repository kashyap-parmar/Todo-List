def get_user_choice(arr):
    while True:
        userchoice = input("Select a number which you seeing above to this: ")
        try:
            if int(userchoice) not in arr:
                print("This operation is not listed Yet !!")
            elif int(userchoice) in arr:
                return int(userchoice)
        except Exception as e:
            print("Enter a valid number")