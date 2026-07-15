name= input("Enter your name:")
experience=float(input("Enter the experience:"))
performance_score=float(input("Enter Performance score:"))
if experience>=7:
    if performance_score >=90:
       print("Elible for promotion")
    else:
        print("Need to improve")
else:
    print("Not elible for promotion")    