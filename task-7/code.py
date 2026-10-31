
# Retail Billing with Multiple Discount Rules

print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

products = []
subtotal = 0
total_tax = 0

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/groceries): ").lower()
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Validate inputs
    if price < 0 or quantity <= 0:
        print("Invalid product details!")
        continue

    # Calculate product amount
    amount = price * quantity

    # Category-specific tax
    if category == "electronics":
        tax_rate = 18

    elif category == "clothing":
        tax_rate = 5

    elif category == "groceries":
        tax_rate = 3

    else:
        print("Invalid category!")
        continue

    tax = amount * tax_rate / 100

    products.append([name, category, price, quantity,
                      amount, tax_rate, tax])

    subtotal += amount
    total_tax += tax

# Calculate discount
if subtotal > 5000:
    discount = subtotal * 0.10

elif subtotal > 3000:
    discount = subtotal * 0.05

else:
    discount = 0

# Maximum discount limit
if discount > 1000:
    discount = 1000

# Calculate final bill
final_amount = subtotal + total_tax - discount

# Display invoice
print("\n========== ITEMIZED INVOICE ==========")

print("Product\tCategory\tPrice\tQty\tAmount\tTax")

for p in products:
    print(p[0], "\t", p[1], "\t",
          p[2], "\t", p[3], "\t",
          p[4], "\t", str(p[5]) + "%")

print("--------------------------------------")
print("Subtotal: Rs.", round(subtotal, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Discount: Rs.", round(discount, 2))
print("--------------------------------------")
print("Final Amount: Rs.", round(final_amount, 2))
print("Thank You for Shopping!")

