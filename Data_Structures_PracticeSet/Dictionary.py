student = {"name":"John","age":20,"grade":"A"}
print(student["name"])
student["grade"] = "A+"
student["city"] = "Delhi"
print(student)

# Dictionary of friends contacts

contacts = {
    "Chaitanya":8669722298,
    "Pratik"   :9022211296,
    "Soham"    :8898762452
    }

print(contacts.keys())
print(contacts.values())
print(contacts.items())

for keys,values in contacts.items():
    print(keys,values)