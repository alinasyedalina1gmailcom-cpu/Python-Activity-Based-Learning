
# Manufacturing Cost and Profitability Analysis

print("===== MANUFACTURING COST ANALYSIS =====")

product = input("Enter product name: ")

quantity = int(input("Enter production quantity: "))

material = float(input("Enter material cost per unit: "))
labour = float(input("Enter labour cost per unit: "))
wastage = float(input("Enter wastage percentage: "))
machine = float(input("Enter machine cost per unit: "))
selling_price = float(input("Enter selling price per unit: "))
target = float(input("Enter profit target percentage: "))

# Validate inputs
if (quantity <= 0 or material < 0 or labour < 0 or
    machine < 0 or selling_price < 0 or
    wastage < 0 or wastage > 100 or target < 0):

    print("Invalid input! Please enter valid values.")

else:
    # Calculate material cost
    material_cost = material * quantity

    # Calculate wastage cost
    wastage_cost = material_cost * wastage / 100

    # Calculate labour cost
    labour_cost = labour * quantity

    # Calculate machine cost
    machine_cost = machine * quantity

    # Calculate total manufacturing cost
    total_cost = (
        material_cost + wastage_cost +
        labour_cost + machine_cost
    )

    # Calculate sales revenue
    revenue = selling_price * quantity

    # Calculate profit or loss
    profit = revenue - total_cost

    # Calculate profit percentage
    if total_cost > 0:
        profit_percentage = (profit / total_cost) * 100
    else:
        profit_percentage = 0

    # Display report
    print("\n===== MANUFACTURING REPORT =====")

    print("Product Name:", product)
    print("Production Quantity:", quantity)

    print("\nMaterial Cost: Rs.", material_cost)
    print("Wastage Cost: Rs.", wastage_cost)
    print("Labour Cost: Rs.", labour_cost)
    print("Machine Cost: Rs.", machine_cost)

    print("--------------------------------")
    print("Total Manufacturing Cost: Rs.", total_cost)
    print("Total Sales Revenue: Rs.", revenue)

    if profit > 0:
        print("Total Profit: Rs.", profit)
    elif profit < 0:
        print("Total Loss: Rs.", abs(profit))
    else:
        print("No Profit No Loss")

    print("Profit Percentage:", round(profit_percentage, 2), "%")

    # Check profit target
    print("\n===== PROFIT TARGET ANALYSIS =====")

    if profit_percentage >= target:
        print("Production meets the profit target.")
    else:
        print("Production does not meet the profit target.")

print("\nThank You!")

