# ***** PYTHON LOOPS *****

# 1. Basic For Loop
# A loop iterates over a sequence and performs the same operation on each element, such as a list.
# EX: Iterate over and print each number in a list
numbers = [1,2,3,4,5]
for num in numbers:
    print(num)


# 2. For Loop with Range
# EX: Using Range, print numbers from 10 to 15 and step by 2
for num in range(10,16,2):
    print(num)


# 3. For Loop over a String
# EX: print each letter in string
team = 'lakers'
for letter in team:
    print(letter)


# 4. While Loop
# A while loop keeps executing as long as its conditional True
# EX: print numbers from 1 to 5 using a while loop
count = 1
while count <= 5:
    print(count)
    count += 1


# 5. Break Statement
# the break statement breaks out of the loop when a certain condition is met
# EX: Stop the loop when the number 3 is found
count = 0
print('breaking with while loop')
while count <= 5:
    print(count)
    count += 1
    if (count == 3):
        break
    
print('breaking with for loop')
for num in range(5):
    if (num == 3):
        break
    print(num)

    
# 6. Continue Statement
# the continue statement skips the current iteration and contiues with the next
# EX: Skip printing number 3
for num in range(5):
    if (num == 3):
        continue
    print(num)


# 7. Nested Loops
# EX: print a multiplication table (1-3)
for x in range(1,10):
    for y in range(1, 10):
        print(f'{x}*{y} = {x * y}')

cars = ['jeep', 'mustang', 'audi']
colors = ['red', 'black', 'white']

for car in cars:
    for color in colors:
        print(f'{color} {car}')




# ***** PYTHON FUNCTIONS *****
# 1. Basic Function
# A function is defined using the def keyword, followed by the function name and parentheses. Inside the parentheses, you can include parameters that the function can accept.
# EX: Define a function to greet a user
def greet():
    print('Hello, Christian')

greet()


# 2. Function with Parameters
# NOTE: The term "parameters" & "arguments" are used interchangeably
# EX: Define a function with one parameter
def greet_with_param(name):
    print(f'Hello, {name}')

name = greet_with_param('Mason') # returns None
print(name)

# 3. Function with Return Value
# NOTE: In most cases, functions will always return a value
# EX: Define a function that adds two numbers
def add_numbers(a,b):
    return a + b

total = add_numbers(7,5) # returns the value (12)
print(total)


# 4. Function with Default Parameters
# You can specify default values for parameters. If an argument is not provided, the default value is used.
# EX: Define a function with a default parameter
def multiply(a=7, b=5):
    return a * b

print(multiply(2))


# 5. Anonymous Function(lambda)
# a small function that can have any number of parameters but only one expression
# NOTE: Its not ever needed, its mainly used to clean up code.
# EX: Define a lambda function to cube a number
cubed = lambda x: x**3
print(cubed(2))



# 8. Functions with Arbitrary Arguments (*args)
# pass any number of arguments to a function
# EX: Define a function that accepts any number of arguments
def add_nums(*args):
    return sum(args)

print(add_nums(1,2))
print(add_nums(1,2,3,4,5,6))
print(add_nums(1,2,100,22,200))


# 9. Functions with Keyword Arguments (**kwargs)
# pass any number of keyword arguments to a function
# EX: Define a function that accepts any number of keyword arguments
def nfl_teams(first_name,**kwargs):
    print(first_name)
    print(kwargs)

nfl_teams('christian', seattle='Seahawks', dallas='Cowboys', ny='Giants')