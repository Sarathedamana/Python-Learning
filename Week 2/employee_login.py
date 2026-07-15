username=input("Enter the username")
password=input("Enter the password:")
if username=="admin":
    if password=="Admin123":
        print("login Successfull")
    else:
        print("invalid password")
else:
    print("Incorrect Username")           