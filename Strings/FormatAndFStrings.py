# Format Strings 

Template = "Dear {}  you can have {} ruppees"

a = "Sai"
a1 = 1000

b = "Ashish"
b1 = 20000

c = "Chaitanya"
c1 = 30000

s1 = Template.format(a,a1)
print(s1)

# F Strings

Template2 = f"DeaR {b} you can have {b1} ruppees"
print(Template2)