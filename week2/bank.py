#print statement to introduce problem
print("welcome to the balance calculator")

#asking the user to input there name
var = input('what is your name')
# take inputs
num1 = float(input('Enter first amount in cents: '))
num2 = float(input('Enter second amount in cents: '))

# adding numbers
sum = num1 + num2


# calculate sum of numbers
('total amount of {0} and {1} {2}' .format(num1, num2,sum))

# print sum plus user input 
print(f"{var} your balance is \u20ac", sum)
