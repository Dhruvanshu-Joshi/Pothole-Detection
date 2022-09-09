# Least Square Regression Method
It is a mathematical method used to find the best fit line that represents the relationship between an independent and dependent variable.  

## Line of Best Fit 
It is a line drawn across a scattered plot of data points to represent a relationship between those data points. The line is as close as possible to all the scattered data points.  
This relationship can be defined by using least-squares method. It is based on the idea that the square of the errors obtained must be minimized to the most possible extent.  
  
If we were to plot the best fit line that shows the depicts the sales of a company over a period of time, it would look something like this:

![image](https://user-images.githubusercontent.com/103961320/189431594-32febcb5-bb2b-4a12-b3f8-cd744340c471.png)
  
### Steps to calculate the Line of Best Fit
Equation of a line:  
![image](https://user-images.githubusercontent.com/103961320/189433026-2ffd8ceb-9ad9-4019-86d3-7cb511b87008.png)  
Calculate:   
Slope  
Y-intercept  
Dependent variable corresponding to the independent variable   
  
Consider that there are ‘n’ data points:  
![image](https://user-images.githubusercontent.com/103961320/189433999-1c43b7fe-bb58-45c9-9c61-b29061026404.png)  

Example:  
Consider Tom(owner of a retail shop) found the price of different T-shirts vs the number of T-shirts sold at his shop over a period of one week.   
![image](https://user-images.githubusercontent.com/103961320/189440069-8fe1a19a-82a4-4d45-be85-48c02f158802.png)  
  
Using Least Square Regression:  
![image](https://user-images.githubusercontent.com/103961320/189440665-5dc40747-382f-4b3b-b93e-54ef6116ca85.png)  
Graph of line of best fit:  
![image](https://user-images.githubusercontent.com/103961320/189441602-e5ecd927-f462-48d9-b73c-e47c18fc3edf.png)  
Now Tom can use the above equation to estimate how many T-shirts of price $8 can he sell at the retail shop.  
y = 1.518 x 8 + 0.305 = 12.45 T-shirts => 13 T-shirts  
  
  
The least squares regression method works by minimizing the sum of the square of the errors as small as possible. The distance between the line of best fit and the error must be minimized as much as possible.  
  
### Points To Remember  
-The data must be free of outliers because they might lead to a biased and wrongful line of best fit.  
-The line of best fit can be drawn iteratively until you get a line with the minimum possible squares of errors.  
-This method works well even with non-linear data.  
-Technically, the difference between the actual value of ‘y’ and the predicted value of ‘y’ is called the Residual (denotes the error).  
  
## Implementing Least Squares Regression in Python  
https://www.edureka.co/blog/least-square-regression/#A%20short%20python%20script%20to%20implement%20Linear%20Regression
