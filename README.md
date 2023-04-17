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


this is a the first piece of code people learn when starting to code, in order to make this code do a little bit more I added a variable called input that asks for the user name
what is your name 
what is your name keith 
this will then been displayed with hello world 
helloworld  keith

#  problem 2 bank  #

the program should:

# <P>

Prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 

# <p>

to slove this i first introduced the problem using a print statement to welcome the user to the balance calculator and asking the user to input there name as a varable this varable is used again in the progamme when recalling the total balance. I then set up two varables called amount 1 and amount 2. when the user inputs both of these amounts the program adds them togather and also divides the sum by 100. this converts the cents value into euro. and gives the output telling the user what there total balance is, this output has a decimal sign between the euro and cent ensuring it is in the right format. to test this if you input amount one as 245 and amount 2 as 130. your result should be your name followed by your total balance 3.75 with the euro sign. to close off the problem I used another print statement to thank the user for using the balance calaualtor and outputting the users name.

#  problem 3 account number #

this problem asked the following, .
# <p>
Write a python program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs) 
to solve this I started by asking the user to enter a 10 degit number. that created a string from the the input. 
# <p>
I then created another string and then used [-4:] this would splice the first 6 numbers from the account number. to test this I used the following the sequence enter your 10 degit account number: 2345678910
I then used a test print statement to print the last 6 digits. which gave me 8910.
I then printed  6 x's with the string{final} to display the final four digits as xxxxxx8901 


 
 
 #  Problem Number 4 controlling the flow #
 # <p>
"The Collatz conjecture is a conjecture that a particular sequence always reaches 1. my program checks for a postive number to be entered. if the user does not enter a postive number the program will throw an exception. 
# <p>
I used the number 34 as the first test integer so the sequence the sequence ran as 34 17 52 26 13 40n 20 10 5 16 8 4 2 1. 
I then used the number 9 to test this sequence. the sequence ran as follows 9 28 14 7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
I also used 0 as a input, when zero is entered it will print that the input is invalid. 


#  problem 5 weekday #

this programme will output whether the current day is a weekday or not. To do this I imported the date time module in python, this module gets the current date and time, it will then get the current day and print weather it is a weekday or a weekend. 

#  problem 6 sqaure root #
I first asked the user for the input and converted it to a float.

I then made a function, which takes the number and got an approximate estimation of the square root by diving it in half.

I then got a better approximation of the Square Root by using Newton's method: (0.5 * (approx + (num/approx)))

By using a while loop, the approximate and better approximations were compared until the differece became close to 0. At this point the loop stopped and gave the best approximation of the square root. 

I tested this program using 10 as a input which returned 3.16 as the sqaure root. 
I also used 12 as an input to test this which gave 3.4 as the sqaure root. 

# #
