Text = "Coding in python is fun"

print(Text.replace("fun","Awesome"))
print(Text.index("python"))
print(Text.upper())

# Bonus (Vowels Check)

sum = 0
vowels = ['a','e','i','o','u']

for char in Text.lower() :
    if (char in vowels) :
        sum+=1
        
print(f"There are {sum} vowels in the string ")

# Bonus (Palindrome)

String1 = "MOM"

if (String1[::1] == String1[::-1]) :
    print("This is a palindrome")
else :
    print("This is not a palindrome")
