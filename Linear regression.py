import matplotlib.pyplot as plt
from scipy import stats
from numpy import arange

Xdata = [1,59,87,6,12,33,9,85,1,69,8,54,56]  #Input data as array
Ydata = [9,51,46,5,15,36,75,64,76,53,3,1,2]

Xdata.sort() #Sort data in ascending order
Ydata.sort()
print("X data = ",Xdata)
print("Y data = ",Ydata)

slope, intercept, r_value, p_value, std_err = stats.linregress(Xdata,Ydata)
print("Slope = ", slope)
print("Intercept = ", intercept)
print("R value = ", r_value)
print("P value = ", p_value)
print("Standard error = ", std_err)

xi=arange(0,max(Xdata)) #determine line range of y=mx+b using max Xdata
Line = slope*xi+intercept

plt.plot(Xdata,Ydata, 'o', Line)
plt.title('Regression sample')
plt.xlabel('X data')
plt.ylabel('Y data')
plt.show()