student = {"name": "Noah", "course": "Python", "grade": 90}
print("Created:", student)
print("Name by key:", student["name"])
print("Missing key with default:", student.get("email", "Not provided"))
student["grade"] = 95
print("Updated grade:", student)
student["city"] = "Irvine"
print("Added city:", student)
print("Keys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))
for key, value in student.items():
    print(f"{key}: {value}")
removed_course = student.pop("course")
print(f"Removed course ({removed_course}):", student)
print("Length:", len(student))

report_card = {"name": "Noah", "subject": "Python", "grades": (92, 85, 96)}
print(f"Student: {report_card['name']}; Subject: {report_card['subject']}")
average = sum(report_card["grades"]) / len(report_card["grades"])
report_card["average"] = average
print(f"Average: {average:.2f}")
if average >= 90:
    print("Excellent!")
elif average >= 70:
    print("Good job!")
else:
    print("Needs improvement!")
del report_card["subject"]
print("Updated report card:", report_card)
