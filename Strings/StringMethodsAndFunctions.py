Text = " hello world "

# Changing Case
print(Text.upper())
print(Text.lower())
print(Text.capitalize())
print(Text.title())

# Removing Whitespaces

print(Text.strip())
print(Text.lstrip())
print(Text.rstrip())

# Finding and Replacing

Text2 = "Python is Fun"
print(Text2.find("is"))
print(Text2.replace("is","is very much"))

# Splitting and Joining

Text3 = "DBMS,Math,E-Commerce,Cybersecurity,Qra,Computer-Organiztion"
print(Text3.split(","))
NewText3 = "-".join(['DBMS', 'Math', 'E-Commerce', 'Cybersecurity', 'Qra', 'Computer-Organiztion'])
print(NewText3)

# Checking String Properties

Text4 = "Python3145"
print(Text4.isalpha())
print(Text4.isdigit())
print(Text4.isalnum())
print(Text4.isspace())

# Example of isspace() Function 

Text5 = " \t\n"

if Text5.isspace() : 
    print("This String Contains Only Whitespace Characters")
else :
    print("This String Does Not Contain Only Whitespace Characters")

# Useful Built-In String Functions

print(len(Text))
print(ord("A"))
print(chr(65))

# Format and F-Strings

name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))
print(f"My name is {name} and I am {age} years old.")     