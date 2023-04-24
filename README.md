# ATUproblemsets

# table of contents # 

 1. helloworld.py
 2. bank.py 
 3. accounts.py
 4. collatz.py
 5. weekday.py
 6. sqaure.py
 7. es.py
 8. plot.py 
#  problem 1 print hello world #


the main idea of this problem was to commit to github along with a simple print hello world statement. this is  the first piece of code people learn when starting to code, in order to make this code do a little bit more I added a variable called input that asks for the user name it then printed this with hello world. 

# references #
https://github.com/git-guides/git-commit

#  problem 2 bank statements #

the program should:

Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

# <p>

to slove this i first introduced the problem using a print statement to welcome the user to the balance calculator and asking the user to input there name as a variable this variable is used again in the progame when recalling the total balance. I then set up two variables called amount 1 and amount 2. when the user inputs both of these amounts the program adds these amounts and also divides the sum by 100. this converts the cents value into euro. and gives the output telling the user what there total balance is, this output has a decimal sign between the euro and cent ensuring it is in the right format. to test this if you input amount one as 245 and amount 2 as 130. your result should be your name followed by your total balance 3.75 with the euro sign. to close off the problem I used another print statement to thank the user for using the balance calculator and outputting the users name.

# references # 

https://www.w3schools.com/python/python_variables.asp
https://realpython.com/python-variables/
https://python.land/python-data-types/python-float

#  problem 3 account number state  variables #

this problem asked the following, 

Write a python program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs) 
to solve this I started by asking the user to enter a 10 digit number. that created a string from the the input. 
# <p>
I then created another string and then used [-4:] this would splice the first 6 numbers from the account number. to test this I used the following the sequence enter your 10 digit account number: 2345678910
I then used a test print statement to print the last 6 digits. which gave me 8910.
I then printed  6 x's with the string{final} to display the final four digits as xxxxxx8901 

# references #

https://www.geeksforgeeks.org/python-list-slicing/
https://www.tutorialspoint.com/what-is-slicing-in-python
https://www.pythontutorial.net/advanced-python/python-slicing/
 
 
 #  Problem Number 4 controlling the flow #

 this programme asked the following,
 
  Write a program, called collatz.py, that asks the user to input any positive integer and outputs the successive values of the following calculation. Have the program end if the current value is one
 # <p>
"The Collatz conjecture is a conjecture that a particular sequence always reaches 1. my program checks for a postive number to be entered. if the user does not enter a postive number the program will throw an exception. 
# <p>
I used the number 34 as the first test integer so the sequence the sequence ran as 34 17 52 26 13 40n 20 10 5 16 8 4 2 1. 
I then used the number 9 to test this sequence. the sequence ran as follows 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
I also used 0 as a input, when zero is entered it will print that the input is invalid. 

# references # 
https://en.wikipedia.org/wiki/Collatz_conjecture
https://codippa.com/even-odd-python/
https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print
https://www.pythonpool.com/collatz-sequence-python/
https://www.sanfoundry.com/python-program-test-collatz-conjecture-given-number/
https://youtu.be/tYQCfYqFa4E


#  problem 5 data structures weekday #

this programme will output whether the current day is a weekday or not. To do this I imported the date time module in python, this module gets the current date and time, it will then get the current day and print weather it is a weekday or a weekend. 

# references # 

https://www.geeksforgeeks.org/python-datetime-module/
https://docs.python.org/3/library/datetime.html?highlight=datetime%20module
https://pythontic.com/datetime/date/weekday
https://stackoverflow.com/questions/16348815/python-assigning-multiple-variables-to-same-value-list-behavior



#  problem 6 functions sqaure root #

this program asked to write a program that takes a positive floating-point number as input and outputs an approximation of its square root. 

# <p>
I first asked the user for the input and converted it to a float.

I then made a function, which takes the number and got an approximate estimation of the square root by diving it in half.

I then got a better approximation of the Square Root by using Newton's method: (0.5 * (approx + (num/approx)))

By using a while loop, the approximate and better approximations were compared until the differece became close to 0. At this point the loop stopped and gave the best approximation of the square root. 

I tested this program using 10 as a input which returned 3.16 as the sqaure root. 
I also used 12 as an input to test this which gave 3.4 as the sqaure root. 

# references # 

https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
https://stackoverflow.com/questions/55232484/newtons-method-for-approximating-square-roots
https://www.w3schools.com/python/python_functions.asp 
https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/


# 7 files reading the occurances of e in a file #

Write a program that reads in a text file and outputs the number of e's it contains. Think about what is being asked here


# <p>
I started with importing the sys module and used sys.argv, a list which contains the command-line arguments passed to the script. It allows taking in an input from an argument on the command line. The sys.argv[0] is the script itself, while the sys.argv[1] is the argument on the command line. Assumption here is that the name of the file the user wants to work with, follows the name of the script, i.e. its position in the list of arguments on the command line is [1].
This argument is stored as a variable filename that is taken in by the custom function countEs defined in the subsequent lines.
# <p>
In order to get access and manipulate or read from a file, the file needs to be opened. It is achieved by using the open() function that returns a file object. Next, the read() function is used to read from the file object.
The countEs() function is set to return the total number of es in the file despite their case, as well as a number of lower- and uppercase es. Each value is stored as a separate variable. Initially, the value of all three variables is 0.
# <p>
Using the for loop, each character in the file is checked and cross-referenced with the conditions defined under the if statement. Every time lower or upper case e is encountered, +1 is added to the respective variable, as well as the variable storing total number of es, and the values stored under these variables are updated to reflect the current state of the counter. The function returns all three variables as a list. 


The function is called and each value from the generated list is assigned a variable then used in the output message.

# references # 
https://www.youtube.com/watch?v=decAHMKIo_A 
https://www.youtube.com/watch?v=QJBVjBq4c7E
https://www.delftstack.com/howto/python/occurrences-of-a-character-in-a-string-in-python/
 https://www.cs2study.com/wp-content/uploads/2021/03/Text-File-exam-based-questions.pdf
https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
https://www.sanfoundry.com/python-program-read-file-counts-number/
# week 8 plots 

create a program that creates a histogram plot using python. 

# <p>

to begin this task I downloaded the numpy module this is a library that is used for working with arrays. and I also downloaded the matplotlib module. this is used for the visualisation of arrays. 

# <p> 

 I created a histogram from the numbers the program randomly generates. As it follows, the values in the brackets are the mean, standard deviation and number of values. Once the histogram is made, the function h(x) = x ^ 3 is plotted on the same graph. The function ranges from 1 to 10. using numpy 

 # <p>

The functions title(), xlabel() and ylabel() were taken from the matplotlip.pyplot library to label the plot. I also added two labels one for value and one for frequency and set custom color and font for the plot. 

# references # 
https://numpy.org/doc/stable/reference/generated/numpy.arange.html
https://www.w3schools.com/python/matplotlib_line.asp
https://www.w3schools.com/python/matplotlib_labels.asp
https://youtu.be/yj31agJRBoI 
https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/
https://realpython.com/python-matplotlib-guide/



