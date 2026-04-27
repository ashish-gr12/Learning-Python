def sumofall(n):
    if n == 0 :
        return 0
    return n%10+sumofall(n//10)

print(sumofall(123))
