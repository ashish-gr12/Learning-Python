# Lambda functions are used for convenience and reducing code length as they are anonymous and inline functions 

"""
Instead of writing as 
def sum(x,y) :
    return x+y

we can do it like this using lambda functions :
"""

sum = lambda x,y:x+y
print(sum(10,20))

square = lambda x:x*x
print(square(10))