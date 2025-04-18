def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        # Return the original price if no discount is applied
        return price

# Prompt the user for the original price and discount percentage
price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the final price
print(f"The final price after applying the discount is: ${final_price:.2f}")
