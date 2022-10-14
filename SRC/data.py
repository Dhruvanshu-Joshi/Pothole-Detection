import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import math

# The input depth map being rectified itself and due to problems like occlusion,etc. contains many garbage values
# These garbage values misleads the surface fit form
# hence we assign a value such that its effect is minimised 
# Hence ,  we assign the average value

def Prepare_Data_without_outliers(depth ,depth3d , min_d , max_d ):
    sum_dis = 0 # store the sum of all the depth values in a variable
    disp_no =0 # store the total number of depth values
    for i in range(depth.shape[0]):
        for j in range(depth.shape[1]):
            if depth[i][j]>=min_d and depth[i][j]<=max_d :
                sum_dis= sum_dis + depth[i][j]
                disp_no = disp_no + 1
    avg_depth = sum_dis/disp_no
    d1= depth.flatten()
    for i in range(depth.shape[0]):
        for j in range(depth.shape[1]):
            if depth[i][j]<min_d or depth[i][j]>max_d :
                depth3d[i][j] = int(avg_depth)

    #We seperate out the garbage values and do not consider it while calculating the surfface fit

    depth1 = np.zeros((depth.shape[0],depth.shape[1]))
    w2 = []
    h2 =[]
    d2 =[]
    for i in range(depth.shape[0]):
        for j in range(depth.shape[1]):
                if(depth3d[i][j] == int(avg_depth) and depth[i][j]!= int(avg_depth)):
                    depth1[i][j]= depth3d[i][j]
                else:
                    d2.append(depth3d[i][j])
                    w2.append(i)
                    h2.append(j)
    return depth1 , depth3d, d2,w2,h2,d1