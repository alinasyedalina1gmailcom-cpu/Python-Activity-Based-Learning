# 7. Retail Billing with Multiple Discount Rules – Python Program

### 1. Problem Statement

Develop a Retail Billing System using Python to process multiple products and their quantities. The system should calculate product-wise prices, apply category-specific taxes, provide discounts based on purchase amount, enforce maximum concession limits, and generate a detailed itemized invoice showing the final payable amount.

### 2. Algorithm

1. Start the program.
2. Enter the number of products.
3. Enter product name, category, price, and quantity.
4. Calculate the total price of each product.
5. Apply category-specific taxes:
   - Electronics: 18%
   - Clothing: 5%
   - Groceries: 3%
6. Calculate the subtotal of all products.
7. Apply threshold discounts:
   - Above ₹5,000: 10% discount.
   - Above ₹3,000: 5% discount.
   - Otherwise: No discount.
8. Limit the maximum discount to ₹1,000.
9. Calculate the final bill after discount and tax.
10. Display the itemized invoice.
11. Stop the program.

### 3. Flowchart
``` mermaid

flowchart TD
    A([Start]) --> B[/Enter number of products/]
    B --> C[/Enter product details/]
    C --> D{Validate price and quantity}
    D -- No --> E[Display Invalid Details]
    D -- Yes --> F{Check Product Category}
    F --> G[Apply Category Tax]
    G --> H[Calculate Product Amount]
    H --> I[Store Product Details]
    I --> J{More Products?}
    J -- Yes --> C
    J -- No --> K[Calculate Subtotal and Tax]
    K --> L{Subtotal above 5000?}
    L -- Yes --> M[Apply 10% Discount]
    L -- No --> N{Subtotal above 3000?}
    N -- Yes --> O[Apply 5% Discount]
    N -- No --> P[No Discount]
    M --> Q[Apply Maximum Discount Limit]
    O --> Q
    P --> Q
    Q --> R[Calculate Final Amount]
    R --> S[Generate Itemized Invoice]
    S --> T([Stop])

```
### 5. Sample Input

```
===== RETAIL BILLING SYSTEM =====

Enter number of products: 3

Product 1
Enter product name: Laptop
Enter category: electronics
Enter product price: 40000
Enter quantity: 1

Product 2
Enter product name: Shirt
Enter category: clothing
Enter product price: 1000
Enter quantity: 2

Product 3
Enter product name: Rice
Enter category: groceries
Enter product price: 500
Enter quantity: 2
```

### 6. Sample Output

```
========== ITEMIZED INVOICE ==========

Product    Category       Price   Qty   Amount   Tax

Laptop     electronics    40000   1     40000    18%
Shirt      clothing       1000    2     2000     5%
Rice       groceries      500     2     1000     3%

--------------------------------------
Subtotal: Rs. 43000.0
Total Tax: Rs. 7270.0
Discount: Rs. 1000.0
--------------------------------------
Final Amount: Rs. 49270.0

Thank You for Shopping!
```

