def main(): 
    print('welcome to the balance app')#print statement to introduce the problem 
    balance1 = input("first balance:  ")#take in user input for the first balance 
    balance2 = input("second balence: ")#take in user input for the second balance 
    sum = float(balance1) + float(balance2)# Adding two numbers
    print("The sum of {0} and {1} is {2}" .format(balance1, balance2, sum))
