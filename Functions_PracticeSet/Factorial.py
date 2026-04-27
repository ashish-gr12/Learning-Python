def fac(n) :
    if n<0 :
        print("Factorial Not Defined For Negative Numbers !")
    if(n == 0 or n == 1 ):
        return 1 
    return fac(n-1)*n

print(fac(0))