# Store input numbers
num1 = input('Enter first number: ')
num2 = input('Enter second number: ')

# Add two numbers
sum = float(num1) + float(num2)
avg = (float(num1) + float(num2))/2
mul = (float(num1) * float(num2))

# Display the sum
print('The sum of {0} and {1} is {2} avg of {0} and {1} is {3} and mul of {0} and {1} is {4}'.format(num1, num2, sum, avg, mul))
