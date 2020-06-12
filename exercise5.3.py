username = []
if username:
    for user in username:
        if user == 'Admin':
            print("\nHello Admin, would you like to see a status report?")
        else:
            print("\n Hello " + user + " thank you for logging in again.")
else:
    print("We need to find some users!")
