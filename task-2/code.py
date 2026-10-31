
# Progressive Electricity Billing System

n = int(input("Enter number of months: "))

bills = []
units_list = []

for i in range(n):
    print("\nMonth", i + 1)

    units = int(input("Enter electricity units consumed: "))

    # Calculate slab charges
    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    # Fixed charges
    fixed_charge = 50

    subtotal = charge + fixed_charge

    # Surcharge
    surcharge = subtotal * 0.05

    total = subtotal + surcharge

    # Rebate
    rebate = 0

    if units < 100:
        rebate = total * 0.05

    final_bill = total - rebate

    units_list.append(units)
    bills.append(final_bill)

    print("Electricity Charge: Rs.", charge)
    print("Fixed Charge: Rs.", fixed_charge)
    print("Surcharge: Rs.", surcharge)
    print("Rebate: Rs.", rebate)
    print("Final Bill: Rs.", round(final_bill, 2))

# Compare monthly bills
print("\n----- Monthly Bill Comparison -----")

for i in range(n):
    print("Month", i + 1, "Bill: Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]
        percentage = (increase / bills[i - 1]) * 100

        if percentage > 30:
            print("Warning: Unusual increase in bill!")

        else:
            print("Bill increase is normal.")

# Total bill
print("\nTotal Electricity Bill: Rs.", round(sum(bills), 2))

