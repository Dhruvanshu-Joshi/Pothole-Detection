# Least-Squares Fitting  
## Introduction  
Curve Fitting Toolbox™ software uses the method of least squares when fitting data. Fitting requires a parametric model that relates the response data to the predictor data with one or more coefficients. The result of the fitting process is an estimate of the model coefficients.  
  
To obtain the coefficient estimates, the least-squares method minimizes the summed square of residuals.  
ri = yi - ŷi   
residual = data − fit  
  
Summed square of residuals:  
![image](https://user-images.githubusercontent.com/103961320/189499261-822e5377-0074-47a6-a6dd-931b498bae81.png)  
  
## Error Distributions  
Assumptions abut error:  
- The error exists only in the response data, and not in the predictor data.  
- The errors are random and follow a normal (Gaussian) distribution with zero mean and constant variance, $σ^2$.  
  The second assumption is often expressed as  
  ![image](https://user-images.githubusercontent.com/103961320/189499470-49e3e3c2-0484-4867-ab27-f62c82c2f82b.png)  
  
Errors are assumed to be normally distributed as it often provides an adequate approximation to the distribution of many measured quantities.  
But LSF method does not assume normally distributed errors. Still it works best for the data that does not contain a large number of random errors with extreme values.  
However, statistical results such as confidence and prediction bounds do require normally distributed errors for their validity.  
  
Mean of errors = 0 ==> errors are purely random  
Mean of errors ≠ 0 ==> model not right for data OR errors are not purely random and contain systematic errors  
  
Constant variance in data => speed of errors is constant   
Data having the same variance is sometimes said to be of equal quality.  
  
It is assumed that the weights provided in the fitting procedure correctly indicate the differing levels of quality present in the data. The weights are then used to adjust the amount of influence each data point has on the estimates of the fitted coefficients to an appropriate level.  
  
## Linear Least Squares  
Curve Fitting Toolbox software uses the linear least-squares method to fit a linear model to data. A linear model is defined as an equation that is linear in the coefficients. For example, polynomials are linear but Gaussians are not.   
![image](https://user-images.githubusercontent.com/103961320/189500363-03234244-7a2d-476c-a8be-0bb9b4232f11.png)  
  
To solve this equation, we use  
![image](https://user-images.githubusercontent.com/103961320/189500431-f4908617-65d2-4eea-a495-78fb7aa23668.png)  
If n is greater than the number of unknowns, then the system of equations is overdetermined.  
   
  ![image](https://user-images.githubusercontent.com/103961320/189500500-c7132c1c-2c2f-481b-b80a-f252e9a214b0.png)  
To extend this to a higher degree polynomial, it requires an additional normal equation for each linear term added to the model.  
  
In matrix form,  
$$y = Xβ + ε$$
where  
- y is an n-by-1 vector of responses.  
- β is a m-by-1 vector of coefficients.  
- X is the n-by-m design matrix for the model.  
- ε is an n-by-1 vector of errors.  
  
For 1st  degree polynomial,  
![image](https://user-images.githubusercontent.com/103961320/189500707-b7c82b29-ea33-4089-b4d1-96b2adca7846.png)  
The least-squares solution to the problem is a vector b, which estimates the unknown vector of coefficients β. The normal equations are given by  
$$(X^TX)b = X^Ty$$
where $X^T$ is the transpose of the design matrix X. Solving for b,  
$$b = (X^TX)–1 X^Ty$$
  
To solve a system of simultaneous linear equations for unknown coefficients  use backslask operator [(mldivide)](https://in.mathworks.com/help/matlab/ref/mldivide.html)   
The backslash operator uses QR decomposition with pivoting, which is a very stable algorithm numerically.  
For more info, reffer: [Arithmetic Operators](https://in.mathworks.com/help/matlab/arithmetic.html) (from MATLAB)  
  
You can plug b back into the model formula to get the predicted response values, ŷ.  
$$ŷ = Xb = Hy$$
$$H = X(X^TX)^–1 X^T$$
A hat (circumflex) over a letter denotes an estimate of a parameter or a prediction from a model. The projection matrix H is called the hat matrix, because it puts the hat on y.  
The residuals are given by  
$$r = y – ŷ = (1–H)y$$
