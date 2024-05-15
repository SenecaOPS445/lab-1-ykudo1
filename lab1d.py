#!/usr/bin/env python3
'''Description: This program will output "hello world" to the screen.'''

# Any line that starts with a "#" is also known as a comment,
# these lines are ignored by the python interpreter even if
# they contain code. The very first line is called a Shebang line, 
# it is used to tell the system which interpreter to 
# use(python2, python3, bash, etc). 

#print(10 + 5)    # addition
#print(10 - 5)    # subtraction
#print(10 * 5)    # multiplication
#print(10 / 5)    # division
#print(10 ** 5)   # exponents

x = 10
y = 2
z = 5

result = x+y*z

print(str(x) + ' + ' + str(y) + ' * ' + str(z) + ' = ' +  str(result))