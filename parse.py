contacts = {
    "number":4,
    "students":
        [
            {"name":"Sean", "age":34},
            {"name":"Natalie", "age":22}
        ]
}

for student in contacts["students"]:
    print("Student:", student["name"], student["age"])