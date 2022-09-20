#importing necessary libraries
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
#plotting using traditional calculation
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize

# z = a0 + a1x + a2y + a3x^2 + a4xy + a5y^2 
def fun(cf, x, y):
    return cf[0] + cf[1]*x + cf[2]*y + cf[3]*x*x + cf[4]*y*x + cf[5]*y*y


disparity = np.load('/home/toshan/Pothole-Detection/Code/image_0.npy')

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


image_centre_h = disparity.shape[0]/2
image_centre_w = disparity.shape[1]/2

''' Projects points from 2d to 3d using disparity to calculate Z coordinates'''

points = []

f = 800.74853515625
B = 0.075

height1, width1 = disparity.shape[:2]

# assume a minimal disparity of 2 pixels is possible to get Zmax
# and then get reasonable scaling in X and Y output

#Zmax = ((f * B) / 2)
a=0
x3d=[]
y3d=[]
z3d=[]

for y in range(height1):# 0 - height is the y axis index
    for x in range(width1):# 0 - width is the x axis index

        # if we have a valid non-zero disparity
        if (disparity[y,x] > 0 or disparity[y,x] < 0):

            # calculate corresponding 3D point [X, Y, Z]

            Z = np.round(((f * B) / disparity[y,x]), 3)

            X = np.round(((x - image_centre_w) * B) / disparity[y,x], 3)
            Y = np.round(((y - image_centre_h) * Z) / disparity[y,x], 3)

            # add to points
            x3d.append(X)
            y3d.append(Y)
            z3d.append(Z)

#             if(left_img_rect.size > 0):
#                 points.append([X,Y,Z,left_img_rect[y,x]])
#             else:
            points.append([X,Y,Z])


disps = []

for i in range(400):
    for j in range(640):
        disps.append(disparity[i,j])


cf0 = np.ones(6)

res_robust = scipy.optimize.least_squares(fun, cf0, loss='arctan', f_scale=1.0, args=(np.array(x3d), np.array(y3d)))
print(res_robust)

x = np.linspace(-4, 12, 16)

y = np.linspace(-3000, 3000, 50)

xv, yv = np.meshgrid(x, y)

cfs = res_robust.x

# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
ax.set_title('Robust Regression')
ax.plot_surface(xv, yv, fun(cfs, xv, yv),linewidth=0, antialiased=False, shade = True, alpha = 0.5)
ax.scatter3D(x3d, y3d, disps)
plt.show()