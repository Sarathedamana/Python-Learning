Balance_amount=int(input("Enter the balance amount:"))
Withdrawal_amount=int(input("Enter the withdrawal amount :"))
if Balance_amount>=Withdrawal_amount:
    if Withdrawal_amount<=20000:
        print("Transaction Successfull")
    else:
        print("daily limit exceeds")    
else:
    print("transaction declined")        
