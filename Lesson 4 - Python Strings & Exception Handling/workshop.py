# ****** Python Strings
# NOTE: Strings are immutable, cannot change

# 1. Creating a String "" or ''

# 2. String Concatenation
first_name = 'christian'
last_name = 'sachs'
full_name = first_name + ' ' + last_name
print(full_name)

# 3. String Formatting
print(f'My name is: {first_name} {last_name}.')

# 4. String Slicing
my_string = 'Hello, CLASS'
print(my_string[0:5])
print(my_string[7:])


# 5. String Methods

# print string in upper case
upper_case = my_string.upper()
print(upper_case)
print(my_string)

# print string in lower case
print(my_string.lower())

# split a string
sentence = 'Python is a great language'
print(sentence.split())


# Replace Python with JavaScript
print(sentence.replace('Python', 'JavaScript'))
print(sentence)

# 6. String Length Function
sentence_count = len(sentence)
print(sentence_count)


# 7. Check if substring exists
if 'JavaScript' in sentence:
    print('Found language')
else:
    print('Langauge not found')



# ****** Python Exceptions

#1. Basic try-except Block
# NOTE: To except and handle all errors, replace specfic error with "Exception"

try:
    user_choice = int(input('What number would you like to cube?\n'))
    print(user_choice ** 3)
except Exception:
    print('Not a valid choice')