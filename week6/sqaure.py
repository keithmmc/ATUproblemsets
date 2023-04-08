# Obtaining the number from the user.
num = float(input("PLease enter a number:"))

# create a function called sqrt that takes an example 'num'
def sqrt(num):
    # getting a loose approximation of the sqaure root by dividing the number in half
    approx = num * 0.5
    # Use Newtons method to get a better estimation of the square root
    better = (0.5 * (approx + (num/approx)))
    
    # Use a while loop with a condition that compares the two results
    # and continues to iterate through results.  
    # The difference between the two should tend towards 0
    # Once the difference is insignificant the while loop will stop and return
    # the best approximation as the square root.
    while better != approx:
        approx = better
        better = (0.5 * (approx + (num/approx)))
    return better

    
print("The square root of " + str(num) + " is approx: " + str(sqrt(num))) 
    


    
    



# References:
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
#  https://www.w3schools.com/python/python_functions.asp 
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/



