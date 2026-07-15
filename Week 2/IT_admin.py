Employee_name=input("Enter the name:")
Department=input("Enter the department:")
Approval=input("Do you have admin approval:")
if Department=="IT":
    if Approval=="Yes":

       print("Access Granted")
    else:
        print("Approval needed")
else:
    print("Access denied")        
