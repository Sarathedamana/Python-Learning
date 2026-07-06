Monthly_Salary = float(input("Monthly Salary is :"))
Hike_Percentage = float(input("Hike percentage:"))
Salary_hike=Hike_Percentage/100
New_Salary = (Monthly_Salary+(Monthly_Salary* Salary_hike))
print(New_Salary)
