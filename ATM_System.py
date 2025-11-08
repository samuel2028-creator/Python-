withdrawal = float(input("Enter the money that you want to withdraw for today?"))

def Atm_withdrawal():
    balance = 1000.00

    if withdrawal > balance:
        print("Insufficient funds")
    elif withdrawal == balance:
        print("Balance will be 0")
        balance = 0
    elif withdrawal < balance:
        print("Withdrawal successful")
        balance -= withdrawal
        print(f"The left balance is {balance}")
        

Atm_withdrawal()
    
    
