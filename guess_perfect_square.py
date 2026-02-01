from math import sqrt
x = int(input("Enter a number: "))
guess = 0
negative_flag = False
if x <0:
    negative_flag = True
while guess**2 <x:
    guess +=1
if guess**2 == x:
    print (f'{guess} is square root of {x}')
else:
    print (f'{x} is not a perfect square')
    if negative_flag:
        print ("because you entered a negative number")