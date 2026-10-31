
# Railway Fare and Reservation Calculator

print("===== RAILWAY RESERVATION SYSTEM =====")

n = int(input("Enter number of passengers: "))

total_collection = 0

for i in range(n):

    print("\nPassenger", i + 1)

    name = input("Enter passenger name: ")
    age = int(input("Enter passenger age: "))
    distance = float(input("Enter travel distance in km: "))

    print("\nTravel Classes:")
    print("1. Sleeper")
    print("2. AC 3 Tier")
    print("3. AC 2 Tier")
    print("4. AC First Class")

    choice = int(input("Select travel class (1-4): "))

    # Validate input
    if age < 0 or distance <= 0 or choice not in [1, 2, 3, 4]:
        print("Invalid passenger details!")
        continue

    # Calculate distance-based fare
    if distance <= 100:
        fare = distance * 1

    elif distance <= 300:
        fare = (100 * 1) + (distance - 100) * 1.5

    else:
        fare = (100 * 1) + (200 * 1.5) + (distance - 300) * 2

    # Class charges
    if choice == 1:
        class_name = "Sleeper"
        multiplier = 1

    elif choice == 2:
        class_name = "AC 3 Tier"
        multiplier = 2

    elif choice == 3:
        class_name = "AC 2 Tier"
        multiplier = 3

    else:
        class_name = "AC First Class"
        multiplier = 4

    fare = fare * multiplier

    # Age-based concession
    concession = 0

    if age < 5:
        concession = fare
    elif age >= 60:
        concession = fare * 0.20

    fare_after_concession = fare - concession

    # Reservation fee
    reservation_fee = 50

    final_fare = fare_after_concession + reservation_fee

    print("\n----- TICKET DETAILS -----")
    print("Passenger Name:", name)
    print("Age:", age)
    print("Travel Class:", class_name)
    print("Distance:", distance, "km")
    print("Basic Fare:", fare)
    print("Concession:", concession)
    print("Reservation Fee:", reservation_fee)
    print("Final Fare:", final_fare)

    # Cancellation
    cancel = input("Do you want to cancel ticket? (yes/no): ")

    if cancel.lower() == "yes":

        penalty = final_fare * 0.20
        refund = final_fare - penalty

        print("Cancellation Penalty:", penalty)
        print("Refund Amount:", refund)

    else:
        print("Ticket Confirmed!")
        total_collection += final_fare

print("\n===== FINAL SUMMARY =====")
print("Total Railway Collection: Rs.", round(total_collection, 2))

print("Thank You for Using Railway Reservation System!")

