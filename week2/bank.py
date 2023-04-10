#print statement to introduce problem
print("welcome to the balance calculator")
var = input('what is your name')
print(f"'welcome to the balance calulator' {var}")
# Prompt user for two money amounts (in cent)24
amount1 = int(input("Enter the first amount (in cents):\t "))
amount2 = int(input("Enter the second amount (in cents):\t "))
# Add the two amounts and divide sum by 100 to convert cents to euros
eur = (amount1+amount2)/100
# Display result in requested format
print(f'{var}your total balance is: \t\t\t€{eur}')
#closing print statement 
print(f"'thanks for using the balance calulator'{var}")
