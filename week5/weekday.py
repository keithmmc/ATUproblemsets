#importing the datetime module to extract today's date.

import datetime 

# Assigning either yes unfortunately or yay weekend
Monday = "Yes, unfortunately today is a weekday."
Tuesday = "Yes, unfortunately today is a weekday."
Wednesday = "Yes, unfortunately today is a weekday."
Thursday = "Yes, unfortunately today is a weekday."
Friday = "Yes, unfortunately today is a weekday."
Saturday = "It is the weekend, yay!"
Sunday = "It is the weekend, yay!"

# Make day of week into integer
dayasnumber = datetime.datetime.today().weekday()

# Assigining intergers to days of week
weekdays = {0:Monday,1:Tuesday, 2:Wednesday, 
            3:Thursday,4:Friday,5:Saturday,6:Sunday}
# printing out the result
print (weekdays[dayasnumber])

##https://www.geeksforgeeks.org/python-datetime-module/
##https://docs.python.org/3/library/datetime.html?highlight=datetime%20module
##https://pythontic.com/datetime/date/weekday
##https://stackoverflow.com/questions/16348815/python-assigning-multiple-variables-to-same-value-list-behavior
