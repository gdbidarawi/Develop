#BMI Calculator

BMI_CATEGORIES = [
    (18.5, "Underweight",    "You may be at risk for nutritional deficiencies."),
    (25.0, "Normal weight",  "Great! Maintain a balanced diet and regular exercise."),
    (30.0, "Overweight",     "Consider lifestyle changes to reduce health risks."),
    (float("inf"), "Obese",  "Please consult a healthcare professional."),
]


def classify_bmi(bmi: float) -> tuple[str, str]:
    for threshold, category, advice in BMI_CATEGORIES:
        if bmi < threshold:
            return category, advice
    return "Obese", BMI_CATEGORIES[-1][2]   # fallback (shouldn't reach)


# ── Display ───────────────────────────────────────────────────────────────────

BAR_RANGES = [(18.5, "Underweight"), (25.0, "Normal"), (30.0, "Overweight"), (40.0, "Obese")]
BAR_WIDTH  = 40


def bmi_bar(bmi: float) -> str:
    """Return a simple ASCII progress bar showing where the BMI falls."""
    max_bmi  = 40.0
    clamped  = min(bmi, max_bmi)
    position = int((clamped / max_bmi) * BAR_WIDTH)
    bar      = "─" * position + "▲" + "─" * (BAR_WIDTH - position)
    return f"  0 [{bar}] 40+"


#Input helpers

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("  [Error] Please enter a positive number.\n")


# Main

def run():
    print("=" * 45)
    print("            BMI Calculator")
    print("=" * 45)
    print("Formula: BMI = weight(kg) / height(m)²\n")

    weight = get_positive_float("  Weight (kg)   : ")
    height = get_positive_float("  Height (m)    : ")

    bmi = weight / (height ** 2)
    category, advice = classify_bmi(bmi)

    print("\n" + "─" * 45)
    print(f"  Your BMI     : {bmi:.2f}")
    print(f"  Category     : {category}")
    print(f"  Note         : {advice}")
    print()
    print(bmi_bar(bmi))
    print()
    print("  WHO BMI Scale:")
    print("    < 18.5   Underweight")
    print("    18.5–25  Normal weight")
    print("    25–30    Overweight")
    print("    ≥ 30     Obese")
    print("─" * 45)


if __name__ == "__main__":
    run()
