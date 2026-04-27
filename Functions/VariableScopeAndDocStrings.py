def sum(a,b) :
    c = a+b
    d = 10 
    # Here d is a local variables
    return c

    # here d is a global variable
d = 10
print(sum(10,11))
print(d)

'''To change value of a global variable inside scopre of a function we need to use the keyword global'''

def sub(a,b) :
    global d
    c = a-b
    d = 20
    return c

print(sub(20,10))    
print(d)


"""Docstrings are used to document our functions,program,code,etc"""

def greet() :
    '''This function greets as hello !'''
    print("hello")

print(greet.__doc__)


def multiply(a,b) : 
    '''
    This function gives multiplication of two numbers 

    (int a) = first number 
    (int b ) = second number 

    c  = (int) multiplication a and b 
    
    return c returns value in c and terminates the function
    '''
    c = a*b
    return c

print(multiply.__doc__)