# Python Syntax
# camelCase, snake_case, PascalCase, UPPER_CASE
firstName = 'christian'
first_name = ''
FirstName = 'christian' # used only for classes
FIRST_NAME = 'christian' # used only for constants (value never changes) 

# Python Conditionals (if, elif, else)
# falsy values
# empty sequences and collections (lists, tuples, strings, dictionaries, sets), zero in every numeric type, None, and False

temp = 65

if (temp):
    print('temp defined')
else:
    print('temp undefined')



# comparison operators
# <, <=, >, >=, ==, !=
if (temp >= 90):
    print('Its pretty steamy outside, do not wear black!')
elif (temp >= 75):
    print('Its a nice day!')
elif (temp == 65):
    print('Its exactly 65 degrees')
else:
    print('Its coooooold outside, consider laying up!')


# logical AND & OR
# nested if & input function

username = ''
password = 'gohawks'

if (first_name == 'christian' or username == 'csachs'):
    user = input('Are you the Lead Instructor, Christian Sachs?(yes or no)\n').lower()
    if (user == 'yes'):
        password = input('What is your password?\n')
        if (password == 'gohawks'):
            print('Access Granted: Hello ' + username)
        else:
            print('Incorrect password, try again')
    else:
        print('Hello, Student!')
else:
    print('Hello, Student!')


# Python Lists: Stores multiple values in a single variable
students = ['Bdada', 'Dennis', 'Brittany', 'Sakura']

# indexing
print(students[0])
print(students[1])
print(students[2])


# slicing (start(includes): stop(excludes): step)
print(students[:2])
print(students[1::2])

passing_students = students[0:2]
print(passing_students)


# add to list
students.append('Mason')
print(students)

# remove from list using .pop(0), .remove('student 1'), del, .clear()
students.pop(2) # .pop(2) removes index value
print(students)

students.remove('Bdada') # removes the value itself
print(students)

del students[0] # deletes the index defined
print(students)

students.clear() # clears all values in a list
print(students)


# membership checks with "in" & "not in"

languages = ['python', 'html/css', 'javascript']

if ('c++' not in languages):
    print('Language is NOT in the program')
else:
    print('Language is apart of the curriculum')