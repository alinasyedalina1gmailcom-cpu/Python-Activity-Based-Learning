
# Employee Payroll and Deduction Analysis

print("===== EMPLOYEE PAYROLL SYSTEM =====")

name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")

basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

# Validate input
if (basic < 0 or allowances < 0 or
    overtime_hours < 0 or overtime_rate < 0 or incentives < 0):

    print("Invalid Input! Salary values cannot be negative.")

else:
    # Calculate overtime pay
    overtime_pay = overtime_hours * overtime_rate

    # Calculate gross salary
    gross = basic + allowances + overtime_pay + incentives

    # Progressive deductions
    if gross <= 10000:
        deduction = 0

    elif gross <= 20000:
        deduction = (gross - 10000) * 0.05

    else:
        deduction = (10000 * 0.05) + ((gross - 20000) * 0.10)

    # Calculate net salary
    net_salary = gross - deduction

    # Display salary statement
    print("\n===== SALARY STATEMENT =====")
    print("Employee Name:", name)
    print("Employee ID:", emp_id)
    print("--------------------------------")
    print("Basic Salary: Rs.", basic)
    print("Allowances: Rs.", allowances)
    print("Overtime Pay: Rs.", overtime_pay)
    print("Incentives: Rs.", incentives)
    print("--------------------------------")
    print("Gross Salary: Rs.", gross)
    print("Total Deductions: Rs.", deduction)
    print("--------------------------------")
    print("Net Salary: Rs.", net_salary)
    print("--------------------------------")
    print("Salary Processed Successfully!")

