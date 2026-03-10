number = int(input("Enter a Number : "))

match (number) :
    case 1 :
        print("GATE")
    case 2 :
        print("UPSC")
    case 3 :
        print("MPSC")
    case 4 :
        print("IT-Sector")
    case 5 :
        print("Something Different Than All of This")
    case _:
        print("Maybe Life Wants Something Different You Never Thought Of")
