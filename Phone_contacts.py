response = int(input("Press 1 to add, Press 2 to view your contactss, Press 3 to remove contacts"))

contacts = [
	['Abebe', '0920234315'], 
	['Kebede', '0920246715'], 
	['Haile', '0920246756']
]

if response == 1:
    name = input("insert the contacts name")
    number = input("Enter the persons phone number")
    new = [[name, number]]
    contacts.extend(new)
    print(contacts) 
elif response == 2:
    print(contacts)
elif response == 3:
    last = int(input("What index of your contact that you want to remove"))
    contacts.pop(last)
    print(contacts)
else:
    print("undefined")
    
