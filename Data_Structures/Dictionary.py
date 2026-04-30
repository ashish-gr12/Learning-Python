dict = {"Ash":20,"Sayali":11,"Shivkumar":21}
print(dict)
print(dict["Ash"])
dict["Ash"] = 30
print(dict)

# Common Dictionary Methods
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.pop("Sayali"))
print(dict)
dict.clear()
print(dict)

# Dictionary Comprehensions

table_of_5  = {i: 5*i for i in range(1,11)}
print(table_of_5)

square_till_5 = {i : i**2 for i in range(6)}
print(square_till_5)