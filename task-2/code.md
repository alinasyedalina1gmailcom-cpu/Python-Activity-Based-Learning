

# 2. Progressive Electricity Billing

## 1. Problem Statement

Develop a Python program to calculate household electricity bills based on the number of units consumed using multiple consumption slabs. The program should include fixed charges, surcharges, and rebates. It should also compare electricity bills across several months and identify unusual increases in consumption or bill amount.

## 2. Algorithm

1. Start the program.
2. Read the number of months.
3. For each month, enter the month name and electricity units consumed.
4. Calculate the electricity charge using the following slabs:
   - First 100 units – ₹2 per unit.
   - Next 100 units – ₹3 per unit.
   - Above 200 units – ₹5 per unit.
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge if consumption exceeds 300 units.
7. Apply a 5% rebate if consumption is below 100 units.
8. Calculate the final electricity bill.
9. Display the monthly bill details.
10. Compare the current month's bill with the previous month's bill.
11. If the bill increases by more than 30%, display an unusual increase warning.
12. Stop the program.

## 3. Flowchart
```
```
## 5. Sample Input

```
Enter number of months: 3

Enter month name: January
Enter electricity units: 80

Enter month name: February
Enter electricity units: 150

Enter month name: March
Enter electricity units: 350
```

## 6. Sample Output

```
----- Electricity Bill -----
Month: January
Units Consumed: 80
Energy Charge: Rs. 160
Fixed Charge: Rs. 50
Surcharge: Rs. 0
Rebate: Rs. 8.0
Total Bill: Rs. 202.0

----- Electricity Bill -----
Month: February
Units Consumed: 150
Energy Charge: Rs. 350
Fixed Charge: Rs. 50
Surcharge: Rs. 0
Rebate: Rs. 0
Total Bill: Rs. 400.0
Warning: Unusual increase in bill!

----- Electricity Bill -----
Month: March
Units Consumed: 350
Energy Charge: Rs. 950
Fixed Charge: Rs. 50
Surcharge: Rs. 47.5
Rebate: Rs. 0
Total Bill: Rs. 1047.5
Warning: Unusual increase in bill!

----- Monthly Bill Comparison -----
January : 202.0
February : 400.0
March : 1047.5

Program Completed.
```

## 7. Mermaid Flowchart Code

