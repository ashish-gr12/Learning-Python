"""
Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''
"""
letter ='''
Dear <|Name|>,
You are selected!
<|Date|>

'''
Name = input("Enter Your Name : ")
Date = input("Enter Your Date : ")
Replace = letter.replace("<|Name|>",Name).replace("<|Date|>",Date)
print(Replace)