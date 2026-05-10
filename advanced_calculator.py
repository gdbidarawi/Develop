"""
Advanced Calculator — Function-Based
-------------------------------------
Demonstrates clean code organisation with separate functions for each operation.
Includes input validation and a loop so the user can calculate multiple times.

Usage:
    python advanced_calculator.py
"""


# ── Operations ──────────────────────────────────────────────────────────────

def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float | str:
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


# ── Helpers ──────────────────────────────────────────────────────────────────

OPERATIONS = {
    "1": ("Add",      add),
    "2": ("Subtract", subtract),
    "3": ("Multiply", multiply),
    "4": ("Divide",   divide),
}


def display_menu():
    print("\n" + "=" * 35)
    print("       Advanced Calculator")
    print("=" * 35)
    for key, (name, _) in OPERATIONS.items():
        print(f"  {key}. {name}")
    print("  q. Quit")


def get_numbers() -> tuple[float, float] | None:
    try:
        a = float(input("  First number : "))
        b = float(input("  Second number: "))
        return a, b
    except ValueError:
        print("  [Error] Please enter valid numbers.")
        return None


# ── Main loop ─────────────────────────────────────────────────────────────────

def run():
    while True:
        display_menu()
        choice = input("\nChoose operation: ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("  [Error] Invalid choice. Enter 1–4 or q.")
            continue

        name, func = OPERATIONS[choice]
        numbers = get_numbers()
        if numbers is None:
            continue

        a, b = numbers
        result = func(a, b)
        print(f"\n  {name}({a}, {b}) = {result}")


if __name__ == "__main__":
    run()
