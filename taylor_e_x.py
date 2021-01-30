#Plotting first four orders of Taylor series for e^x 
#I am currently taking a calculus course through Coursera, so I can't guarantee that the math below is correct! Please let me know of any errors :)
#Kenneth Burchfiel--first version published on 2021-1-30
import matplotlib.pyplot as plt
import numpy as np
xset = np.arange(-1,3,0.01) #x coordinates. Graph is centered at x = 1
e_x = np.exp(xset) #e^x, the function we are trying to approximate through the Taylor series
plt.axhline(y=np.exp(1)) #Graphs a horizontal line at e = 1. 0th order derivative
first_order = np.exp(1) + np.exp(1)*(xset-1) #Each order in the series is built up of the previous order plus a new function 
second_order = np.exp(1) + np.exp(1)*(xset-1) + (np.exp(1))*((xset-1)**2)/2
third_order = np.exp(1) + np.exp(1)*(xset-1) + (np.exp(1))*((xset-1)**2)/2 + (np.exp(1))*((xset-1)**3)/6
fourth_order = np.exp(1) + np.exp(1)*(xset-1) + (np.exp(1))*((xset-1)**2)/2 + (np.exp(1))*((xset-1)**3)/6 + (np.exp(1))*((xset-1)**4)/24
plt.plot(xset,e_x)
plt.plot(xset,first_order)
plt.plot(xset,second_order)
plt.plot(xset,third_order)
plt.plot(xset,fourth_order)
plt.show()

