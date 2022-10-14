import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import math

def Final_result(top,bottom,right,left,single1,avg_pot,disparity_rect_1):
    # Finally we draw the rectangle with its depth
    a =1
    for x in range(len(single1)):
        start_point = (left[x]-5 , top[x]-5)
        end_point = (right[x]+5 , bottom[x]-5)
        start_point_txt = (left[x]-5 , top[x]-25)
        start_point_txt1 = (left[x]-5 , top[x]-10)
        color = (0, 0, 0)

        # Line thickness of 2 px
        thickness = 2
        txt = 'Pothole '+str(a)
        txt1 = 'distance: '+str(round(avg_pot[x],3))
        # Using cv2.rectangle() method
        # Draw a rectangle with blue line borders of thickness of 2 px
        disparity_rect_1 = cv2.rectangle(disparity_rect_1, start_point, end_point, color, thickness)
        disparity_rect_1 = cv2.putText(disparity_rect_1, txt , start_point_txt,
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
        disparity_rect_1 = cv2.putText(disparity_rect_1, txt1 , start_point_txt1,
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 1)
        a=a+1
    plt.imshow(disparity_rect_1 , 'gray')            
    plt.colorbar()
    plt.show()
    
    return disparity_rect_1