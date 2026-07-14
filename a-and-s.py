# Simple Calculator

print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")

choice = input("Choose an operation (1 or 2): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == "1":
    result = num1 + num2
    print("Result =", result)

elif choice == "2":
    result = num1 - num2
    print("Result =", result)

else:
    print("Invalid choice!")