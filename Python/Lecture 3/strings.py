''' 
In Python, strings are a sequence of Unicode Characters.

Why Unicode? ASCII supports 8-bit characters which is very small and can only support 256 characters. Unicode supports 16-bit characters which can support emojis and 4.3 billion characters.

- Creating Strings
- Accessing Strings
- Adding Chars to Strings
- Editing Strings
- Deleting Strings
- Operations on Strings
- String Functions
'''

# Creating Strings
s = 'hello'
s = "hello"
s = '''hello'''
s = """hello"""
s = str('hello')
print(s)

# Accessing Substrings from a String
# Positive Indexing
s = 'hello world'
# print(s[41]) # Error - Index out of range

# Negative Indexing
print(s[-3])

# Slicing
print(s[6:0:-2])

# Reversing
print(s[::-1])

# Reverse Iteration
print(s[-1:-6:-1])

# Editing and Deleting in Strings
# s[0] = 'H' # Error - Strings are immutable
# del s[-1:-5:2] # Error - Strings are immutable

# Operations on Strings
print('delhi' + ' ' + 'mumbai')
print('delhi'*5)
print("*"*50)
print('delhi' != 'delhi')
print('mumbai' < 'mumbb')
print('Pune' > 'pune')
print('hello' and 'world')
print('hello' or 'world')
print('' and 'world')
print('' or False)
print(not 'hello')

for i in 'hello':
  print(i)

for i in 'delhi':
  print('pune')

# Membership Operations
print('D' in 'delhi')

# Common Functions
print(len('hello world'))
print(max('hello world'))
print(min('hello world'))
print(sorted('hello world', reverse=True))

# Capitalize/Title/Upper/Lower/Swapcase
s = 'hello world'
print(s.capitalize())
print(s.title())
print(s.upper())
print('Hello Wolrd'.lower())
print('HeLlO WorLD'.swapcase())

# Count/Find/Index
print('my name is nitish'.count('i'))
print('my name is nitish'.find('x'))
# print('my name is nitish'.index('x')) # will return error if not found

# endswith/startswith
print('my name is nitish'.endswith('sho'))
print('my name is nitish'.startswith('1my'))

# format
name = 'nitish'
gender = 'male'
print('Hi my name is {1} and I am a {0}'.format(gender, name))

# isalnum/ isalpha/ isdigit/ isidentifier
print('nitish1234%'.isalnum())
print('nitish'.isalpha())
print('123abc'.isdigit())
print('first-name'.isidentifier())

# Split/Join
print('hi my name is nitish'.split())
print(" ".join(['hi', 'my', 'name', 'is', 'nitish']))

# Replace
print('hi my name is nitish'.replace('nitisrgewrhgh', 'campusx'))

# Strip
print('nitish                           '.strip())