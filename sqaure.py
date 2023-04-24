#asking the user for a number.
num = float(input("PLease enter a number:"))

#creating a function
def sqrt(num):
    #going to get an approxamtion of the number by multiplying by 0.5
    approx = num * 0.5
    #introducing newtons method to get a better approxaimation of the number
    better = (0.5 * (approx + (num/approx)))
    
    #using a while loop with a condition that compares the two results and get the best approximation
    while better != approx:
        approx = better
        better = (0.5 * (approx + (num/approx)))
    return better

#using a print statement to return the results
print("The square root of " + str(num) + " is approx: " + str(sqrt(num))) 



