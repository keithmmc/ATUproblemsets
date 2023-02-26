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

print (weekdays[dayasnumber])


