# Sets are unordered,unique collections (no duplicates.)

numbers = {12,21,22,19,20}
print(numbers)

# Set Methods 
numbers.add(20)
numbers.remove(21)
numbers.discard(20)
numbers.pop()
print(numbers)

# Set Operations 

a = {1,2,3}
b = {3,4,5}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
