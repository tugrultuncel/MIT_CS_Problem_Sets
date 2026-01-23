yearly_salary = int(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the portion of salary to be saved, as a decimal: "))
cost_of_dream_home = int(input("Enter the cost of your dream home: "))
semi_annual_raise = (float(input("Enter the semi-annual raise, as a decimal: ")))
portion_down_payment = 0.25
amount_saved = 0.0
r=0.05
months = 1

while amount_saved < portion_down_payment * cost_of_dream_home:
    amount_saved += (yearly_salary / 12) * portion_saved
    amount_saved += amount_saved * r / 12
    months += 1
    if months%6==0:
        yearly_salary += yearly_salary * semi_annual_raise

print(f"Number of months: {months}... it makes {months // 12} years and {months % 12} months")