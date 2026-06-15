# Discount Calculator

print("Discount Calculator")

original_price = float(input("Enter original price: "))
discount_percent = float(input("Enter discount percentage (%): "))

discount_amount = original_price * (discount_percent / 100)
final_price = original_price - discount_amount

print("\nResult")
print(f"Original Price: ${original_price:.2f}")
print(f"Discount Percentage: {discount_percent:.2f}%")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Final Price: ${final_price:.2f}")