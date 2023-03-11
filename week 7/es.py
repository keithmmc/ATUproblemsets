#attampt number one
#open the file mobydick.txt and read it 
f = open("mobydick.txt", "r")
#reading the data
data = f.read()
#getting all occurrences of e
occurrences = data.count("e")
#printing the result
print('Number of occurences of the letter e is:', occurrences)
#error opening file (need to research problem some more to find this solution)