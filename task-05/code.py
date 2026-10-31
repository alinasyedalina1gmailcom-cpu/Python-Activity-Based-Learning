
# Multi-Plan Telecommunications Cost Optimization

print("===== MOBILE PLAN OPTIMIZATION SYSTEM =====")

budget = float(input("Enter your budget: "))
validity_required = int(input("Enter required validity days: "))

data_usage = float(input("Enter required data in GB: "))
call_usage = int(input("Enter required call minutes: "))
sms_usage = int(input("Enter required SMS count: "))

# Mobile plans
plans = [
    ["Basic", 199, 28, 2, 300, 100, 20, 0.50, 0.20, 0.10],
    ["Standard", 299, 28, 5, 500, 200, 30, 0.40, 0.15, 0.10],
    ["Premium", 399, 56, 10, 1000, 500, 50, 0.30, 0.10, 0.05],
    ["Unlimited", 599, 84, 20, 2000, 1000, 100, 0.20, 0.10, 0.05]
]

eligible = []

print("\n----- PLAN COMPARISON -----")

for plan in plans:

    name = plan[0]
    price = plan[1]
    validity = plan[2]
    data = plan[3]
    calls = plan[4]
    sms = plan[5]

    data_rate = plan[6]
    call_rate = plan[7]
    sms_rate = plan[8]

    if price <= budget and validity >= validity_required:

        # Calculate excess usage
        extra_data = max(0, data_usage - data)
        extra_calls = max(0, call_usage - calls)
        extra_sms = max(0, sms_usage - sms)

        # Calculate additional charges
        extra_charge = (
            extra_data * data_rate +
            extra_calls * call_rate +
            extra_sms * sms_rate
        )

        total_cost = price + extra_charge

        eligible.append([name, price, extra_charge, total_cost])

        print("\nPlan:", name)
        print("Base Price: Rs.", price)
        print("Extra Charges: Rs.", round(extra_charge, 2))
        print("Total Cost: Rs.", round(total_cost, 2))

    else:
        print("\nPlan:", name, "- Not Eligible")

# Find economical plan
print("\n===== FINAL RECOMMENDATION =====")

if len(eligible) == 0:
    print("No suitable plan found within your budget.")

else:
    best_plan = min(eligible, key=lambda x: x[3])

    print("Most Economical Plan:", best_plan[0])
    print("Plan Price: Rs.", best_plan[1])
    print("Extra Charges: Rs.", round(best_plan[2], 2))
    print("Total Cost: Rs.", round(best_plan[3], 2))

print("\nThank You!")

