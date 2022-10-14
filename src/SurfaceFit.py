import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import math
from datetime import datetime

def fun_residual(cf, vars, z):
    x, y = vars
    return (( cf[0] + cf[1]*x + cf[2]*y + cf[3]*x*x + cf[4]*y*x + cf[5]*y*y ) - z)**2

def fun_z(cf, x, y): # calculate the coefficients

    return cf[0] + cf[1]*x + cf[2]*y + cf[3]*x*x + cf[4]*y*x + cf[5]*y*y 

def Surface_fit_of_Road(d2,w2,h2,d1,w1,h1,h,w,height,width):
    # Surface fit equation: 
    # z = a1 + a2x + a3y + a4x^2 + a5xy + a6y^2
    # we calculate the residual of actual z value available from depth-map and that we get from this equation and minimize it to get the coefficients

    cf0 = np.zeros(6)

    res_robust = scipy.optimize.least_squares(fun_residual, cf0, loss='cauchy', f_scale=100, args=((np.array(w2), np.array(h2)), np.array(d2)))

    x1 = np.linspace(0, width, 32)

    y1 = np.linspace(0, height, 32)
    
    xv, yv = np.meshgrid(x1, y1)
    cfs = res_robust.x
    zv =fun_z(cfs, w1, h1)
    z1 =zv.flatten()
    # Plot the expected surface fit and the scatter plot for a comparitive study 
    # Creating figure
    fig = plt.figure(figsize =(14, 9))
    ax = plt.axes(projection ='3d')
    ax.set_title('Robust Regression')
    ax.plot_surface(h1,w1,zv,linewidth=0, antialiased=False, shade = True, alpha = 0.5)
    ax.scatter3D(h, w, d1)
    plt.show()
    
    return zv
