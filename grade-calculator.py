# Grade Calculator

def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

print("Grade Calculator")

num_subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(num_subjects):
    mark = float(input(f"Enter mark for subject {i+1}: "))
    total += mark

average = total / num_subjects
grade = calculate_grade(average)

print("\nResult")
print(f"Total Marks: {total:.2f}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
