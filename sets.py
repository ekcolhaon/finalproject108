skills = {"Python", "React", "Python", "HTML"}
print("Created (duplicate Python removed):", sorted(skills))
skills.add("CSS")
print("Added CSS:", sorted(skills))
skills.update(["Git", "SQL"])
print("Added multiple skills:", sorted(skills))
skills.remove("HTML")
print("Removed HTML:", sorted(skills))
skills.discard("Java")  # Does not raise an error if Java is absent.
print("Discarded Java if present:", sorted(skills))
print("Contains Python:", "Python" in skills)
print("Length:", len(skills))

frontend = {"HTML", "CSS", "JavaScript"}
backend = {"Python", "SQL", "JavaScript"}
print("Union:", sorted(frontend | backend))
print("Intersection:", sorted(frontend & backend))
print("Frontend only:", sorted(frontend - backend))
print("Symmetric difference:", sorted(frontend ^ backend))
print("CSS is a subset:", {"CSS"}.issubset(frontend))
empty_set = set()  # {} creates a dictionary instead.
print("Empty set:", empty_set)