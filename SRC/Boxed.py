import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import math

def Rectangle(depth,diff_5,single,disparity_pl): 
    height = depth.shape[0]
    width = depth.shape[1]
    # We draw a rectangle around these potholes and also display its distnce
    # disparity_rect = np.zeros((height,width))
    # for i in range(height):
    #     for j in range(width):
    #         disparity_rect[i][j] = depth[i][j]
    top=[]
    bottom=[]
    left =[]
    right =[]
    sum_calc = 0
    d_no = 0
    #Calculate left , right , top and bottom corner coordinates for rectangle around each pothole
    for x in range(len(single)):
        proxy =[]
        proxy2=[]
        for i in range(0,height):
            for j in range(0,width):
                if(disparity_pl[i][j] == single[x]):
                    proxy.append(i)
                    break
        top.append(proxy[0])
        bottom.append(proxy[len(proxy)-1])
        for j in range(0,width):
            for i in range(0,height):
                if(disparity_pl[i][j] == single[x]):
                    sum_calc = sum_calc + depth[i][j]
                    d_no = d_no+1
        avg_disp = sum_calc / d_no 
        #Assumption: I encounter the particular label only in one pothole 
        for j in range(0,width):
            for i in range(0,height):
                if(disparity_pl[i][j] == single[x]):
                    proxy2.append(j)
                    break
        left.append(proxy2[0])
        right.append(proxy2[len(proxy2)-1])
    # a =1
    for x in range(len(single)):
        start_point = (left[x]-5 , top[x]-5)
        end_point = (right[x]+5 , bottom[x]+5)
        start_point_txt = (left[x]-5 , top[x]-25)
        start_point_txt1 = (left[x]-5 , top[x]-10)
        color = (255, 0, 0)

        # Line thickness of 2 px
        # thickness = 2
        # txt = 'Pothole '+str(a)
        # txt1 = 'depth: '+str(avg_disp)
        # Using cv2.rectangle() method
        # Draw a rectangle with thickness of 2 px
        # disparity_rect = cv2.rectangle(disparity_rect, start_point, end_point, color, thickness)
        # disparity_rect = cv2.putText(disparity_rect, txt , start_point_txt,
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
        # disparity_rect = cv2.putText(disparity_rect, txt1 , start_point_txt1,
        #                 cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 1)
        # a=a+1
    # return disparity_rect ,top,bottom,right,left
    return top,bottom,right,left