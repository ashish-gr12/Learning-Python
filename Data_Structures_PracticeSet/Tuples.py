coordinates = (10,20)
print(coordinates)

# This will give an erro as tuples can't be modified
# tup[0] = 50

coorlist = list(coordinates)
coorlist[0] = 50
coordinates = tuple(coorlist)
print(coordinates)
