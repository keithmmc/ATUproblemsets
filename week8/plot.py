import numpy as np
import matplotlib.pyplot as plt

# Define the function h(x) = x^3
def h(x):
    return x ** 3

#Create an array of x values in the range 0, 10 and get y values using h(x) = x^3
x = np.array(range(0, 10))
print(x)
y = h(x)

# Create a plot of h(x) vs. x
plt.plot(x, y, label='Histogram', color="red")

# Generate 1000 random values from a normal distribution with mean 5 and standard deviation 2
data = np.random.normal(5, 2, 1000)

# Create a histogram
plt.hist(data, bins = 10, label = 'Normal Distribution', color = "blue")

# Add labels and a title
plt.xlabel('Value',fontsize="18",font = "Brush Script MT")
plt.ylabel('Frequency',fontsize="18",font = "Brush Script MT")
plt.title('Week 08 Task histogram',font = "Brush Script MT",fontsize="20",color="green")
plt.legend()
# Show both of the plots
plt.show()



##https://numpy.org/doc/stable/reference/generated/numpy.arange.html
##https://www.w3schools.com/python/matplotlib_line.asp
##https://www.w3schools.com/python/matplotlib_labels.asp
##https://youtu.be/yj31agJRBoI 

  

