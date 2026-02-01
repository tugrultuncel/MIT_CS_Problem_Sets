from math import sqrt
for i in range (1,11):
    print (f'sqrt of {i} is {sqrt(i)}')
    if sqrt(i)%1 !=0:
        print (f'{i} is not a perfect square')
    else:
        print (f'{i} is a perfect square')