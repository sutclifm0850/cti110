#P4HW3
#Factorial
#Sutcliffe
#March 25, 2018

factorial = 1

integer = int(input('Enter a nonnegative integer?'))

while integer < 1:
    integer = int(input('Enter a nonnegative integer?'))

for number in range(1, integer + 1):
    factorial = factorial * number
print('The factorial of', integer, 'is', factorial)
    
