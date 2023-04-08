# Ask the user to input a positive integer. 
n = int(input("Please input a positive integer: "))
# "Def Collatz" checks if the numbers are odd or even and performs those calculations.
def collatz(n):

# The loop is repeated until the number reaches 1.
    while n > 1:
# This function prints all the values listed from the number the user enters to the end.
        print(n, end =' ') 
        if (n % 2): 
# If the result is not even, the answer is multiplied by three and one added on to it. 
            n = 3 * n + 1
#If the number is even divide by two until you reach the number one. 
        else:
            n = n//2
    print(1, end='')

# This will print the sequence of the calculation, down as far as the end number such as one.
print("Sequence: ", end='')
collatz(n) 
##https://codippa.com/even-odd-python/
##https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print
##. https://www.pythonpool.com/collatz-sequence-python/
##https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/
##https://youtu.be/tYQCfYqFa4E