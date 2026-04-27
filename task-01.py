# . Write a program that takes salary as input. Using conditional statements, calculate the final tax
# based on the following rules: (Marks 3)
# • If the salary is less than 30,000 → Tax rate is 5%
# • If the salary is between 30,000 and 70,000 → Tax rate is 15%
# • If the salary is greater than 70,000 → Tax rate is 25%

salary = float(input("Please Enter you Salary :: "))

if salary < 30000 :
    tax_rate = 0.05
elif salary >= 30000 and salary <= 70000:
    tax_rate = 0.15
else:
    tax_rate = 0.25

tax = salary * tax_rate
salary_after_tax = salary - tax

print(f"tax rate on salary {tax_rate}")
print(f"Tax on salary {tax}")
print(f"Salary after tax deducton {salary_after_tax}")