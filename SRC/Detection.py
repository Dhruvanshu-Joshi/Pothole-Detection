import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import math

def pothole_detection(depth,zv,h1,w1,min_d,max_d):
    height = depth.shape[0]
    width = depth.shape[1]
    #Calculate the difference of the two surfaces
    diff =np.array(depth) - np.array(zv)
    
    # copy this difference in another variable
    diff_2 = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            diff_2[i][j] = diff[i][j]
    # Region whose difference is greater than 0 are not pothole region hence we assign them 0
    for i in range(height):
        for j in range(width):
            if diff_2[i][j] >0:
                diff_2[i][j] = 0

    # now copy this difference in another variable
    diff_4 = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            diff_4[i][j] = diff_2[i][j]
    # our pothole region must not correpond to a garbage value and hence assign them 0
    for i in range(height):
        for j in range(width):
            if(depth[i][j]< min_d or depth[i][j]> max_d):
                diff_4[i][j] = 0

    #Now we calculate the average of all the candidate pothole regions
    sumc =0
    noc = 0
    for i in range(height):
        for j in range(width):
            sumc= sumc + diff_4[i][j]
            if(diff_4[i][j] != 0):
                noc = noc +1
    avgc = sumc / noc

    #We now create a binary image of the difference obtained with the threshold that all points below the average of all pothole candidates represent a pothole
    diff_3 = np.zeros((height,width))
    for i in range(height):
        for j in range(width):
            diff_3[i][j] = diff_2[i][j]
    for i in range(depth.shape[0]):
        for j in range(depth.shape[1]):
            if(diff_4[i][j] <= (avgc)):
                diff_3[i][j] =0 
            else:
                diff_3[i][j] =1


    # Since the obtained binary image also has some noise we use image processing to minimize them 
    kernel2 = np.ones((21, 21), np.uint8)
    dst2 = cv2.dilate(diff_3, kernel2, iterations=1)
    dst3 = cv2.erode(dst2, kernel2, iterations=1)
    diff_5 = cv2.morphologyEx(dst3, cv2.MORPH_CLOSE, kernel2)
    plt.imshow(diff_5 , 'gray')
    plt.colorbar()
    plt.show()
    
    return diff_5