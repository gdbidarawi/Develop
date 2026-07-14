# Simple Calculator

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Multiplication")
print("2. Division")

choice = input("Choose an operation (1 or 2): ")

if choice == "1":
    result = num1 * num2
    print("Result =", result)

elif choice == "2":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid choice!")