
# create a fucntion 

def sqrt(userinput):
    # convert from str to float 
    userinput = float (userinput) 
    r = userinput
    precision = 10 ** (-10)
    
    while abs(userinput - r * r) > precision:
        r = (r + userinput / r) / 2
        
    return round(r,1)
# getting the user input for a postive number 
userinput = input("Please enter a positive number:")
print("The square root of", userinput, "is approx." , sqrt(userinput))


# References:
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
#  https://www.w3schools.com/python/python_functions.asp 



