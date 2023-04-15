import sys 

filename = sys.argv[1]

try:
    with open(filename,'r') as f:
       text = f.read()
       count = 0
       for i in text:
         if (i == "e"or i =="E"):
            count +=1
       print(count)

except FileNotFoundError:
   print("filename (", filename,") does not exist. Please re-run and enter a valid filename", sep = '')




# https://www.youtube.com/watch?v=decAHMKIo_A 
#https://www.youtube.com/watch?v=QJBVjBq4c7E
# https://www.delftstack.com/howto/python/occurrences-of-a-character-in-a-string-in-python/
# https://www.cs2study.com/wp-content/uploads/2021/03/Text-File-exam-based-questions.pdf
#https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
#https://www.sanfoundry.com/python-program-read-file-counts-number/
