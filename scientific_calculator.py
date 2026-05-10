"""
Scientific Calculator
----------------------
Uses Python's built-in `math` module for advanced mathematical operations.
Supports angles in both degrees and radians.

Usage:
    python scientific_calculator.py
"""

import math


# ── Operation handlers ────────────────────────────────────────────────────────

def square_root(num: float) -> float:
    if num < 0:
        raise ValueError("Square root of a negative number is undefined in real numbers.")
    return math.sqrt(num)


def power(base: float, exponent: float) -> float:
    return math.pow(base, exponent)


def sine(angle_deg: float) -> float:
    return math.sin(math.radians(angle_deg))


def cosine(angle_deg: float) -> float:
    return math.cos(math.radians(angle_deg))


def tangent(angle_deg: float) -> float:
    return math.tan(math.radians(angle_deg))


def logarithm(num: float, base: float = 10) -> float:
    if num <= 0:
        raise ValueError("Logarithm is undefined for non-positive numbers.")
    return math.log(num, base)


def natural_log(num: float) -> float:
    if num <= 0:
        raise ValueError("Natural log is undefined for non-positive numbers.")
    return math.log(num)


# ── Menu ──────────────────────────────────────────────────────────────────────

MENU = """
╔══════════════════════════════════╗
║      Scientific Calculator       ║
╠══════════════════════════════════╣
║  1. Square Root  √x              ║
║  2. Power        x^y             ║
║  3. Sine         sin(°)          ║
║  4. Cosine       cos(°)          ║
║  5. Tangent      tan(°)          ║
║  6. Logarithm    log base 10     ║
║  7. Natural Log  ln              ║
║  q. Quit                         ║
╚══════════════════════════════════╝"""


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  [Error] Please enter a valid number.")


# ── Main loop ─────────────────────────────────────────────────────────────────

def run():
    while True:
        print(MENU)
        choice = input("Choose operation: ").strip().lower()

        try:
            if choice == "1":
                n = get_float("  Enter number: ")
                print(f"\n  √{n} = {square_root(n):.6f}")

            elif choice == "2":
                base = get_float("  Enter base: ")
                exp  = get_float("  Enter exponent: ")
                print(f"\n  {base}^{exp} = {power(base, exp):.6f}")

            elif choice == "3":
                angle = get_float("  Enter angle (degrees): ")
                print(f"\n  sin({angle}°) = {sine(angle):.6f}")

            elif choice == "4":
                angle = get_float("  Enter angle (degrees): ")
                print(f"\n  cos({angle}°) = {cosine(angle):.6f}")

            elif choice == "5":
                angle = get_float("  Enter angle (degrees): ")
                print(f"\n  tan({angle}°) = {tangent(angle):.6f}")

            elif choice == "6":
                n = get_float("  Enter number: ")
                print(f"\n  log({n}) = {logarithm(n):.6f}")

            elif choice == "7":
                n = get_float("  Enter number: ")
                print(f"\n  ln({n}) = {natural_log(n):.6f}")

            elif choice == "q":
                print("Goodbye!")
                break

            else:
                print("  [Error] Invalid choice. Enter 1–7 or q.")

        except ValueError as e:
            print(f"\n  [Math Error] {e}")


if __name__ == "__main__":
    run()
