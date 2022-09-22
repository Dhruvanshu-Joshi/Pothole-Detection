import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
#plotting using traditional calculation
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import copy

disparity = np.load('../depth-sav/image_1.npy')
sum_dis = 0
disp_no =0
for i in range(disparity.shape[0]):
    for j in range(disparity.shape[1]):
        sum_dis= sum_dis + disparity[i][j]
        disp_no = disp_no + 1
avg_dis = sum_dis/disp_no
for i in range(disparity.shape[0]):
    for j in range(disparity.shape[1]):
        if(disparity[i][j] == 0):
            disparity[i][j] = avg_dis

x3d=[]
y3d=[]
z3d=[]

for i in range(disparity.shape[0]):
    for j in range(disparity.shape[1]):
        x3d.append(i)
        y3d.append(j)
        z3d.append(disparity[i,j])


def fun_residual(cf, vars, z):
    x, y = vars
    return ((cf[0] + cf[1]*x + cf[2]*y + cf[3]*x*x + cf[4]*y*x + cf[5]*y*y) - z)**2


def fun_z(cf, x, y):

    return cf[0] + cf[1]*x + cf[2]*y + cf[3]*x*x + cf[4]*y*x + cf[5]*y*y


# cf0 = np.ones(6)
cf0 = np.zeros(6)
# np.array(z3d)
# np.zeros(len(z3d))
res_robust = scipy.optimize.least_squares(fun_residual, cf0, loss='cauchy', f_scale=100.0, args=(
    (np.array(x3d), np.array(y3d)), np.array(z3d)))

cfs = res_robust.x
print(res_robust)

x = np.linspace(0, 400, 50)
y = np.linspace(0, 600, 50)

xv, yv = np.meshgrid(x, y)

# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
ax.set_title('Robust Regression')
ax.plot_surface(xv, yv, fun_z(cfs, xv, yv),linewidth=0, antialiased=False, shade = True, alpha = 0.5)
#zp = fun(cfs , np.array(x3d), np.array(y3d))
ax.scatter(x3d[::20], y3d[::20], z3d[::20])
plt.show()