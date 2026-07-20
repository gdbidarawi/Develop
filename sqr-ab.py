import math

print("Simple Calculator")
print("1. Multiplication")
print("2. Division")
print("3. Absolute Value")
print("4. Square Root")

choice = input("Choose an operation (1-4): ")

if choice == "1":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a * b)

elif choice == "2":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")

elif choice == "3":
    num = float(input("Enter a number: "))
    print("Absolute Value:", abs(num))

elif choice == "4":
    num = float(input("Enter a number: "))
    if num >= 0:
        print("Square Root:", math.sqrt(num))
    else:
        print("Cannot find square root of a negative number")

else:
    print("Invalid choice")