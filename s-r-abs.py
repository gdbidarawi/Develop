num = float(input("Enter a number: "))

# Square
square = num * num

# Absolute Value
if num < 0:
    absolute = -num
else:
    absolute = num

# Square Root (only for positive numbers)
if num >= 0:
    guess = num / 2

    if num == 0:
        root = 0
    else:
        for i in range(10):
            guess = (guess + num / guess) / 2
        root = guess

    print("Square Root =", root)
else:
    print("Square Root: Not defined for negative numbers")

print("Square =", square)
print("Absolute Value =", absolute)