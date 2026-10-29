# PART 1: LIST

hobbies = ["painting", "coding", "hiking", "DJing", "traveling"]
print("Original list:", hobbies)
print("Length:", len(hobbies))

print("Second hobby:", hobbies[1])
print("List:", hobbies)
print("Length:", len(hobbies))

hobbies[2] = "swimming"
print("After replacing hiking:", hobbies)
print("Length:", len(hobbies))

hobbies.remove("painting")
print("After removing painting:", hobbies)
print("Length:", len(hobbies))

hobbies.pop(0)
print("After removing the first item:", hobbies)
print("Length:", len(hobbies))


# PART 2: DICTIONARY

student = {
    "name": "Noah",
    "course": "Python",
    "favorite_hobby": "DJing",
    "assignments_completed": 1
}
print("\nOriginal dictionary:", student)
print("Length:", len(student))

print("Student name:", student["name"])
print("Dictionary:", student)
print("Length:", len(student))

student["city"] = "Irvine"
print("After adding city:", student)
print("Length:", len(student))

student["assignments_completed"] = 2
print("After updating assignments completed:", student)
print("Length:", len(student))

student.pop("favorite_hobby")
print("After removing favorite hobby:", student)
print("Length:", len(student))