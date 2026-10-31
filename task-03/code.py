
# Hospital Billing and Patient Classification

print("===== HOSPITAL BILLING SYSTEM =====")

name = input("Enter patient name: ")

consultation = float(input("Enter consultation charges: "))
diagnostic = float(input("Enter diagnostic charges: "))
treatment = float(input("Enter treatment charges: "))

# Validate charges
if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid charges! Charges cannot be negative.")

else:
    # Calculate total bill
    total = consultation + diagnostic + treatment

    print("\nTotal Bill: Rs.", total)

    # Apply concession
    concession = 0

    if total > 10000:
        concession = total * 0.10

    final_bill = total - concession

    print("Concession: Rs.", concession)
    print("Final Bill: Rs.", final_bill)

    # Payment details
    paid = float(input("Enter amount paid: "))

    if paid < 0 or paid > final_bill:
        print("Invalid payment amount!")

    else:
        pending = final_bill - paid

        # Patient classification
        if paid == final_bill:
            status = "Fully Paid"

        elif paid > 0:
            status = "Partially Paid"

        else:
            status = "Unpaid"

        # Display bill
        print("\n===== PATIENT BILL DETAILS =====")
        print("Patient Name:", name)
        print("Consultation Charges: Rs.", consultation)
        print("Diagnostic Charges: Rs.", diagnostic)
        print("Treatment Charges: Rs.", treatment)
        print("Total Bill: Rs.", total)
        print("Concession: Rs.", concession)
        print("Final Bill: Rs.", final_bill)
        print("Amount Paid: Rs.", paid)
        print("Pending Amount: Rs.", pending)
        print("Patient Classification:", status)

print("\nThank You!")

