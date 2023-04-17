while True:
    try:
        #if statement to ensure number is positive and numeric
        num = int(input("Please enter a positive integer:"))
        if num <= 0:
            print("Invalid input. Please enter a positive integer.")
        else:
            break
    except ValueError as e:
        print("Invalid input. Please enter a positive integer.",e)

while num !=1:
    #use end =' ' to print number on same line in terminal 
    print(num, end=' ')
    # even number if no remainder
    if num % 2 == 0:
        num //= 2
    else:
        #if not even number then must be Odd number 
        num = num * 3 + 1
print(num) 
 
##https://codippa.com/even-odd-python/
##https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print
##. https://www.pythonpool.com/collatz-sequence-python/
##https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/
##https://youtu.be/tYQCfYqFa4E