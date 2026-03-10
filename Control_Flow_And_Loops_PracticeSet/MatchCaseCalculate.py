No1 = int(input("Enter the first number : "))
No2 = int(input("Enter the second number : "))
Operation = input("Enter an operation as +,-,*,/ \n")

match Operation:
    case "+" :
        print(No1+No2)
    case "-" :
        print(No1-No2)
    case "*": 
        print(No1*No2)
    case "/" :
        print(No1/No2)
