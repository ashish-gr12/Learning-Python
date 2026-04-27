import my_utils
''''Write a function safe_divide(a,b) that returns the reuslt of a/b, but returns "Cannot divide by zero" if b is zero '''

def safe_divide(a,b):
    if b == 0 :
        return "Cannot divide by zero"
    return a/b

print(safe_divide(10,0))
from my_utils import is_even
print(is_even(13))