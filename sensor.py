sensory_input = float(input("Enter a number: "))
checked = False
switch = True
if 0 > sensory_input or sensory_input > 1000:
    print('Invalid Input\n Please Check the Sensor')
    checked = True
else:
    for i in range(0,1001):
        if i == sensory_input and 750 <= sensory_input <= 1000:
            print(f'Water level is at {sensory_input} ml.\n Please Check Later')
            checked = True
        elif i == sensory_input and 500 <= sensory_input < 750:
            print(f'Water level is at {sensory_input} ml.\n Please Refill Soon')
            checked = True
        elif i == sensory_input and 250 <= sensory_input <= 500:
            print(f'Water level is at {sensory_input} ml.\n Refill Needed')
            checked = True
        elif i == sensory_input and 50 < sensory_input < 250:
            print(f'Water level is at {sensory_input} ml.\n Refill Immediately')
            checked = True
        elif i == sensory_input and 0 <= sensory_input <= 50:
            print(f'Water level is at {sensory_input} ml.\n Emergency Refill Needed\n Pump Shout Down')
            checked = True
            switch = False
        elif i == sensory_input and sensory_input < 0 :
            print('Invalid Input\n Please Enter a Valid Water Level')
            checked = True
        if checked:
            break