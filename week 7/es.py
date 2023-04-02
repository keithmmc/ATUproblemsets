import sys 
#asking the user to input the file for searching
filename = input("Enter file name: ")
#asking the user to enter the letter to be searched
l=input("Enter letter to be searched:")
k = 0
 #opens the text file
with open(filename, 'r') as f:
    for line in f:
        words = line.split()
# splits line to get list of words
        for i in words:
            for letter in i:
                if(letter==l):
                    k=k+1
#print the occurrences of the letter 
print("Occurrences of the letter:")
print(k)

#https://youtu.be/QJBVjBq4c7E
#https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
#https://www.sanfoundry.com/python-program-read-file-counts-number/
