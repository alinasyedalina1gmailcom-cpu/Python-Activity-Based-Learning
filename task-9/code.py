
# Multi-Currency Travel Budget Analysis

print("===== TRAVEL BUDGET ANALYSIS SYSTEM =====")

budget = float(input("Enter travel budget in INR: "))

n = int(input("Enter number of expense categories: "))

expenses = []
total_expense = 0

for i in range(n):

    print("\nExpense Category", i + 1)

    category = input("Enter expense category: ")
    amount = float(input("Enter expense amount in foreign currency: "))
    rate = float(input("Enter exchange rate to INR: "))

    # Validate inputs
    if amount < 0 or rate <= 0:
        print("Invalid expense details!")
        continue

    # Convert currency into INR
    converted_amount = amount * rate

    # Calculate conversion fee
    fee = converted_amount * 0.02

    # Calculate total expense
    final_amount = converted_amount + fee

    expenses.append([category, converted_amount, fee, final_amount])

    total_expense += final_amount

    print("Converted Amount: Rs.", round(converted_amount, 2))
    print("Conversion Fee: Rs.", round(fee, 2))
    print("Total Expense: Rs.", round(final_amount, 2))


# Identify largest expense category
print("\n===== TRAVEL EXPENSE REPORT =====")

if len(expenses) > 0:

    largest = max(expenses, key=lambda x: x[3])

    print("\nCategory-wise Expenses:")

    for item in expenses:
        print(item[0], ": Rs.", round(item[3], 2))

    print("\nTotal Travel Expense: Rs.", round(total_expense, 2))

    print("Largest Expense Category:", largest[0])
    print("Largest Expense Amount: Rs.", round(largest[3], 2))

    # Compare budget
    print("\n===== BUDGET ANALYSIS =====")

    if total_expense > budget:
        print("Budget Exceeded!")
        print("Extra Amount: Rs.", round(total_expense - budget, 2))

    else:
        print("Travel is Within Budget.")
        print("Remaining Budget: Rs.", round(budget - total_expense, 2))

else:
    print("No valid expenses entered.")

print("\nThank You!")

