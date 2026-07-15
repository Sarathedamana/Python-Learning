servername=input("Enter the servername:")
Environment=input("Enter the environment")
Manager_Approval=input("Do you have manager approval:")
if Environment=="Production":
    if Manager_Approval=="Yes":
        print("Allowed for restart")
    else:
        print("Get the manager approval")
else:
    print("proceed with Server start")            