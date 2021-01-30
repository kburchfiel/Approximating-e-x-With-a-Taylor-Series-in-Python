#Plotting the first five Taylor approximations for e^x at x = 1 
#I am currently taking a calculus course through Coursera, so I can't guarantee that the math below is correct! However, my answer lines up with that found at https://www.symbolab.com/solver/taylor-maclaurin-series-calculator/taylor%20e%5E%7Bx%7D%2C%201
#Kenneth Burchfiel--first version published on 2021-1-30
import matplotlib.pyplot as plt
import numpy as np
xset = np.arange(-1,3,0.01) #x coordinates. Graph is centered at x = 1
e_x = np.exp(xset) #e^x, the function we are trying to approximate through the Taylor series. xset is synonymous with x
plt.axhline(y=np.exp(1)) #Graphs a horizontal line at e = 1. 0th approximation
first_approximation = np.exp(1) + np.exp(1)*(xset-1) #Each approximation in the series is built up of the previous approximation plus a new expression
second_approximation = np.exp(1) + np.exp(1)*(xset-1) + (np.exp(1))*((xset-1)**2)/2
third_approximation = np.exp(1) + np.exp(1)*(xset-1) + (np.exp(1))*((xset-1)**2)/2 + (np.exp(1))*((xset-1)**3)/6
fourth_approximation = np.exp(1) + np.exp(1)*(xset-1) + (np.exp(1))*((xset-1)**2)/2 + (np.exp(1))*((xset-1)**3)/6 + (np.exp(1))*((xset-1)**4)/24
plt.plot(xset,e_x)
plt.plot(xset,first_approximation)
plt.plot(xset,second_approximation)
plt.plot(xset,third_approximation)
plt.plot(xset,fourth_approximation)
plt.show() #The plot shows that each approximation equals e^x at x=1, but then diverges from e^x to the left and right of x=1.

