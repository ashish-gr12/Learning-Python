'''Write a program that takes a list of numbers and removes all duplicates using a set'''

list1 = [1,2,4,6,7,8,3,7,2,4,7,9,10]

list1Set = set(list1)
list1 = list(list1Set)
print(list1)

'''Given a dictionary of products and their prices , find the product with the highest price'''

dict1 = {
    "keyboard": 2000,
    "mousepad": 1000,
    "cpu"     : 100000,
    "monitor" : 5000
}

expensiveOne  = max(dict1,key= dict1.get)
print(expensiveOne)

products,price = max(dict1.items(),key = lambda item :item[1])
print(products,price)

'''Write a program that merges two dictionaries'''

diction1 = {
    "keyboard": 2000,
    "mousepad": 1000,
    "cpu"     : 100000,
    "monitor" : 5000
}

diction2 = {
    "Ash":20,
    "Sayali":11,
    "Shivkumar":21
}

merged = diction1 | diction2
print(merged)

diction1.update(diction2)
print(diction1)