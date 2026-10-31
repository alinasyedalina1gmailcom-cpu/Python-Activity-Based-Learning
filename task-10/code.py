# Campus Event Financial Planning

# Input details
participants = int(input("Enter number of participants: "))

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))

catering = float(input("Enter catering cost per person: "))
transport = float(input("Enter transport cost per person: "))
certificate = float(input("Enter certificate cost per person: "))

sponsorship = float(input("Enter available sponsorship amount: "))
registration_fee = float(input("Enter registration fee per person: "))

# Validate input
if participants <= 0 or venue < 0 or equipment < 0:
    print("Invalid input")

elif catering < 0 or transport < 0 or certificate < 0:
    print("Invalid cost details")

elif sponsorship < 0 or registration_fee < 0:
    print("Invalid sponsorship or registration fee")

else:
    # Calculate costs
    fixed_cost = venue + equipment

    variable_cost = catering + transport + certificate

    total_cost = fixed_cost + (variable_cost * participants)

    # Calculate participant contribution
    contribution = total_cost / participants

    # Calculate sponsorship shortfall
    shortfall = max(0, total_cost - sponsorship)

    # Calculate break-even registrations
    amount_needed = total_cost - sponsorship

    if registration_fee >= variable_cost:
        if amount_needed <= 0:
            break_even = 0
        else:
            break_even = int(amount_needed / registration_fee)

            if break_even * registration_fee < amount_needed:
                break_even += 1
    else:
        break_even = -1

    # Display results
    print("\n----- CAMPUS EVENT FINANCIAL REPORT -----")

    print("Fixed Cost:", fixed_cost)
    print("Variable Cost per Person:", variable_cost)
    print("Total Event Cost:", total_cost)

    print("Contribution per Participant:", contribution)
    print("Sponsorship Shortfall:", shortfall)

    if break_even == -1:
        print("Break-even is not possible with this registration fee")
    else:
        print("Minimum Registrations Required:", break_even)

    print("-----------------------------------------")
