'''write a fib(n) functions that prints the first n fibonacci numbers'''

def print_fib(n):
    a,b = 0,1 
    for _ in range(n):
        print(a,end=" ")
        a,b = b,a+b

print(print_fib(11))