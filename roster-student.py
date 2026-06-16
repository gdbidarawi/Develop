# Student Roster Calculator

students = []

num_students = int(input("Enter number of students: "))

for i in range(num_students):
    print(f"\nStudent {i+1}")

    name = input("Enter student name: ")

    mark1 = float(input("Enter Mark 1: "))
    mark2 = float(input("Enter Mark 2: "))
    mark3 = float(input("Enter Mark 3: "))

    average = (mark1 + mark2 + mark3) / 3

    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"

    students.append({
        "name": name,
        "average": average,
        "grade": grade
    })

# Sort students by average score
students.sort(key=lambda x: x["average"], reverse=True)

print("\nSTUDENT ROSTER REPORT")
print("{:<20} {:<10} {:<10}".format("Name", "Average", "Grade"))

for student in students:
    print("{:<20} {:<10.2f} {:<10}".format(
        student["name"],
        student["average"],
        student["grade"]
    ))

print("\nClass Statistics")

class_average = sum(student["average"] for student in students) / len(students)

print(f"Class Average: {class_average:.2f}")
print(f"Top Student: {students[0]['name']}")