"""
This program uses bisection search to find 
the best savings rate to afford a down payment on a house within 36 months.
"""

initial_deposit = float(input("Enter the initial deposit: "))

house_cost = 800000
portion_down_payment = 0.25
down_payment = house_cost * portion_down_payment
months = 36

low = 0.0
high = 1.0
steps = 0
r = None
epsilon = 100  


if initial_deposit >= down_payment - epsilon:
    r = 0.0
    steps = 0

else:
    amount_saved = initial_deposit * (1 + high / 12) ** months
    if amount_saved < down_payment - epsilon:
        r = None
        steps = 0
    else:
        while True:
            steps += 1
            r = (low + high) / 2
            amount_saved = initial_deposit * (1 + r / 12) ** months

            if abs(amount_saved - down_payment) <= epsilon:
                break
            elif amount_saved < down_payment:
                low = r
            else:
                high = r
print("Best savings rate:", r)
print("Steps in bisection search:", steps)