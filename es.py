#using sys.argv
filename = sys.argv[1]  

#creating a function to open and read filename
def countEs(filename):      
    with open(filename) as f:
        text = f.read()
        # Starts to count from 0.
        numLower = numUpper = numTotal = 0  
# using a loop to  count instances of 'e' in the file.
        for i in text:
            if i == 'e':        
                numLower += 1   
                numTotal += 1 
# using a loop to count instances of 'E' in the file.  
            elif i == 'E':
                numUpper += 1   
                numTotal += 1                
                # numTotal counts every instance of 'e' in the file despite of its case.
        return(numLower, numUpper, numTotal)
# Function countEs() returns multiple values stored as a tuple.
values = countEs(filename)   
lower = values [0] 
upper = values [1]
total = values [2]
#printing out the number of e's and E's with upper and lowercase 
print(f'This file contains a total of {total} instances of letter "e".')
print(f'Out of {total}, {lower} are lowercase and {upper} are uppercase.')


