Name=input("Enter the name:")
Employee_id=input("Enter the employeeid:")
Department= input("Enter the Department:")
Experience=float(input("Enter the experience:"))
Salary=float(input("Enter the Salary:"))
Performance_score=float(input("Enter the performance score :"))
if Salary >= 100000:
    print("High Salary")
else:
    print("Normal Salary")
if Performance_score >=90:
    print("Outstanding and Eligible for Bonus")
elif Performance_score >=75:
    print("Very Good, Eligible for Bonus")      
elif Performance_score >=60:
    print("good, Eligible for Bonus") 
else:
    print("Need improvement, Not eligble")
              