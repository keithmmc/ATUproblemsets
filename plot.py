# importing the following modules for the program
import numpy as np
import matplotlib.pyplot as plt

# Defining the function h(x) = x^3
def h(x):
    return x ** 3

#Creating an array of x values in the range 0, 10 and get y values using h(x) = x^3
x = np.array(range(0, 10))
print(x)
y = h(x)

# Creating a plot of h(x) vs. x
plt.plot(x, y, color="red")

# Generating 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(5, 2, 1000)

# Create a histogram
plt.hist(data, bins = 10, color = "blue")


# Add labels and a title
plt.xlabel('value',fontsize="18",font = "Brush Script MT")
plt.ylabel('frequency',fontsize="18",font = "Brush Script MT")
plt.title('Week 08 Task histogram',font = "Brush Script MT",fontsize="20",color="green")
plt.legend()
# Show both of the plots
plt.show()


  

