#import system 
import sys   
#take command line argument                                
filename = sys.argv[1]
#reading the filename
with open(filename, 'r') as f:
#reading the contents of the file
    e = f.read()     
#counting the upper and lower case letters                      
    count = e.count('e') + e.count('E')     
#printing the amount of times e shows up 
    print(f"The letter 'e' shows up {count} times")


# https://www.youtube.com/watch?v=decAHMKIo_A 
#https://www.youtube.com/watch?v=QJBVjBq4c7E
# https://www.delftstack.com/howto/python/occurrences-of-a-character-in-a-string-in-python/
# https://www.cs2study.com/wp-content/uploads/2021/03/Text-File-exam-based-questions.pdf
#https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
#https://www.sanfoundry.com/python-program-read-file-counts-number/
