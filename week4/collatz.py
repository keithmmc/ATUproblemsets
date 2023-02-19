def collatz(number):
    if(number%2==0):
        n=number//2
        print(n)
        return n
    else:
        ev=3*number+1
        print(ev)
        return ev
num1=input("Enter an integer greater than 1: \n")

#prevents user from entering 1 and negative numbers
try:
    num= int(num1)
    if(num==1):
        print("Enter an integer greater than 1")
    elif(num>1):
        a=collatz(num) 
        while(True):
            if(a==1):
                break
            else:
                a=collatz(a)
    else:
        print("Please, Enter a positive integer to begin the Collatz sequence")

#asks user to only input integers and ends programme if not
except:
    print("Please, enter an integer")
