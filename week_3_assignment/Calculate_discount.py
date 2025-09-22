def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# user input price and discount percentage
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate and print the final price
final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"Discount applied! Final price: {final_price}")
else:
    print(f"No discount applied. Final price: {final_price}")
