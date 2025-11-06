value = float(input("How much money did you work until this time"))

def tax_calculator(value):
    if value >= 0 and value <= 2000:
        tax_owned = (value * 0)
        net_income = (value - tax_owned)
        print(f"Your tax is {tax_owned}. And your net income is {net_income}")
    elif value >= 2001 and value <= 4000:
        tax_owned = (value * 0.15)
        net_income = (value - tax_owned)
        print(f"Your tax is {tax_owned}. And your net income is {net_income}")
    elif value >= 4001 and value <= 7000:
        tax_owned = (value * 0.20)
        net_income = (value - tax_owned)
        print(f"Your tax is {tax_owned}. And your net income is {net_income}")
    elif value >= 7001 and value <= 10000:
        tax_owned = (value * 0.25)
        net_income = (value - tax_owned)
        print(f"Your tax is {tax_owned}. And your net income is {net_income}")
    elif value >= 10001 and value <= 14000:
        tax_owned = (value * 0.30)
        net_income = (value - tax_owned)
        print(f"Your tax is {tax_owned}. And your net income is {net_income}")
    elif value > 14000:
        tax_owned = (value * 0.35)
        net_income = (value - tax_owned)
        print(f"Your tax is {tax_owned}. And your net income is {net_income}")
    else: 
    		print("Invalid Input")
    
    
tax_calculator(value)
    
    
    
    
