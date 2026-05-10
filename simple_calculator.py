"""
Simple Calculator
-----------------
Performs basic arithmetic: addition, subtraction, multiplication, division.
Beginner-friendly — no functions or imports required.

Usage:
    python simple_calculator.py
"""


def run():
    print("=" * 30)
    print("       Simple Calculator")
    print("=" * 30)
    print("Operations: +  -  *  /\n")

    try:
        num1 = float(input("Enter first number : "))
        operator = input("Enter operator     : ").strip()
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("\n[Error] Please enter valid numbers.")
        return

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("\n[Error] Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print(f"\n[Error] Unknown operator '{operator}'. Use +, -, *, /")
        return

    print(f"\nResult: {num1} {operator} {num2} = {result}")


if __name__ == "__main__":
    run()
