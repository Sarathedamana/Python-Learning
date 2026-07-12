customer_name=input("Enter the name:")
Purchase_amount=float(input("Enter the amount"))
 
if Purchase_amount >=10000:
    final_amount1=Purchase_amount- Purchase_amount*20/100
    print("Final amount after discount is",final_amount1)
elif Purchase_amount>=5000:
    final_amount2 =Purchase_amount-Purchase_amount*10/100
    print("Final amount after discount is",final_amount2)  
else:
    print("No discount")      
