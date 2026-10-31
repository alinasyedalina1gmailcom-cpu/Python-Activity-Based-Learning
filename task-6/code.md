
# 6. Railway Fare and Reservation Calculator – Python Program

### 1. Problem Statement

Develop a Railway Fare and Reservation Calculator using Python. The program should calculate railway fares for multiple passengers based on travel distance, travel class, age-based concessions, and reservation fees. It should also calculate cancellation penalties and display the final payable amount for each passenger.

### 2. Algorithm

1. Start the program.
2. Enter the number of passengers.
3. Enter passenger name, age, travel distance, and travel class.
4. Calculate basic fare according to distance slabs:
   - First 100 km: ₹1 per km.
   - 101–300 km: ₹1.5 per km.
   - Above 300 km: ₹2 per km.
5. Apply travel class charges:
   - Sleeper: 1x
   - AC 3 Tier: 2x
   - AC 2 Tier: 3x
   - AC First Class: 4x
6. Apply age-based concessions:
   - Children below 5 years: Free.
   - Passengers aged 60 and above: 20% concession.
   - Other passengers: No concession.
7. Add reservation fee of ₹50 per passenger.
8. Calculate the final fare.
9. Ask whether the passenger wants to cancel the ticket.
10. If cancelled, apply a 20% cancellation penalty.
11. Display passenger-wise fare details and total collection.
12. Stop the program.

### 3. Flowchart
```mermaid

```
### 5. Sample Input

```
===== RAILWAY RESERVATION SYSTEM =====

Enter number of passengers: 2

Passenger 1
Enter passenger name: Rahul
Enter passenger age: 30
Enter travel distance in km: 250

Travel Classes:
1. Sleeper
2. AC 3 Tier
3. AC 2 Tier
4. AC First Class

Select travel class (1-4): 1

Do you want to cancel ticket? (yes/no): no

Passenger 2
Enter passenger name: Ramesh
Enter passenger age: 65
Enter travel distance in km: 400

Select travel class (1-4): 2

Do you want to cancel ticket? (yes/no): yes
```

### 6. Sample Output

```
----- TICKET DETAILS -----

Passenger Name: Rahul
Age: 30
Travel Class: Sleeper
Distance: 250 km
Basic Fare: 325.0
Concession: 0
Reservation Fee: 50
Final Fare: 375.0

Ticket Confirmed!

----- TICKET DETAILS -----

Passenger Name: Ramesh
Age: 65
Travel Class: AC 3 Tier
Distance: 400 km
Basic Fare: 1300.0
Concession: 260.0
Reservation Fee: 50
Final Fare: 1090.0

Cancellation Penalty: 218.0
Refund Amount: 872.0

===== FINAL SUMMARY =====

Total Railway Collection: Rs. 375
