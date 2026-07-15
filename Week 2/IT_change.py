Change_Request_Number=input("Enter the CR Number:")
environment1=input("Enter the environment")
Emergency_change=input("Enter if this is an emergency change")
cab_approval=input("Enter if you have cab approval:")

if environment1=="Production":
    if Emergency_change=="yes" or cab_approval=="no":
        print("exception and change approved")
    else:
        print("Need cab approval")    
    if cab_approval=="yes":
        print("Change approved")
    else:
        print("change denied ")
else:
    print("Proceed with the change")        
