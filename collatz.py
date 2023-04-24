while True:
    try:
        #using an if statement to get a positive number if this is not entered it will ask the user to input a positive one
        num = int(input("Please enter a positive integer:"))
        if num <= 0:
            print("Invalid input. Please enter a positive integer.")
        else:
            break
    except ValueError as e:
        print("Invalid input. Please enter a positive integer.",e)

while num !=1:
    #using end =' ' to print number on same line in terminal 
    print(num, end=' ')
    # if it's an even number
    if num % 2 == 0:
        num //= 2
    else:
        #if not even number then must be Odd number 
        num = num * 3 + 1
print(num) 
 
