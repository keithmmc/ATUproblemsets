import matplotlib.pyplot as plt
import statistics
import numpy as np 

d = [1, 1000]

plt.hist(d, bins= 11, color ='c')
m = statistics.mean(d)
sd = statistics.stdev(d)

plt.axvline(m, color='b', linestyle = 'dashed')
plt.axvline(m + sd, color='k', linestyle = 'dashed')
plt.axvline(m - sd, color='k', linestyle = 'dashed')
plt.xlabel("value")
plt.ylabel("Frequency")
plt.title("histogram")
plt.show()



    

