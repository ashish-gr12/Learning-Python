a = 5
table = []

for i in range(1,11):
    table.append(a*i)

print(table)

#  Efficient Comprehensions

table = [5*i for  i in range(1,11)]
print(table)

square = [x**2 for x in range(5)]
print(square)