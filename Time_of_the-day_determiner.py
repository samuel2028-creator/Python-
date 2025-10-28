time = int(input('What time is it?'))

if time < 0 or time > 24:
    print("Error! You should insert a number between (0 - 24)")
else:
    if 5<= time <= 11:
        print("Its Morning")
    elif 12<= time <= 16:
        print("Its Afternoon")
    elif 17<= time <= 20:
        print("Its Evening")
    elif time >= 21 or time <= 4:
        print("Its Night")
