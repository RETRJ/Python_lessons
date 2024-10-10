# Input in python
# There are a lot of ways to get input in python. Here are some of them.
# 1. from command line
# 2. from file
# 3. from user input
# 4. from environment variables
# 5. from other programs
# 6. etc.

# We will be focusing on user input in this section.
# To get input from user, you can use the input() function.
# The input() function takes a string as an argument and displays it to the user.
# The user can then type in a value and press enter.

# Example:
name = input('Enter your name: ')
print('Hello, ' + name)

# The input() function returns a string. If you want to convert it to a different type, you can use the appropriate function.
# For example, if you want to get an integer from the user, you can use the int() function.
# Example:
age = int(input('Enter your age: '))
print('You are ' + str(age) + ' years old')

