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

def pothole_labelling(depth,diff_5):
    start = datetime.now()
    # We have successfully detected the potholes now and now wish to label them so that they are identified as seperate potholes
    # We create a binary image with limits(0,255) so as to fit the labels
    height = depth.shape[0]
    width = depth.shape[1]

    # We use connected component labelling algorithm here(Better explained in notes)
    disparity_pl = np.zeros((height+1,width+1))
    child=[]
    mom =[]
    a=1
    for i in range(1,height):
        for j in range(1,width):
            if(diff_5[i][j] == 0):
                if(disparity_pl[i-1][j]==0 and disparity_pl[i][j-1]==0 ):
                    a = a+1
                    disparity_pl[i][j]=a
                else:
                    if(disparity_pl[i-1][j]!=0 or disparity_pl[i][j-1]!=0):
                        if(disparity_pl[i-1][j]==0 and disparity_pl[i][j-1]!=0):
                            disparity_pl[i][j]=disparity_pl[i][j-1]
                        elif(disparity_pl[i-1][j]!=0 and disparity_pl[i][j-1]==0):
                            disparity_pl[i][j]=disparity_pl[i-1][j]
                        elif(disparity_pl[i-1][j]!=0 and disparity_pl[i][j-1]!=0):
                            c = min(disparity_pl[i-1][j] , disparity_pl[i][j-1])
                            mo =c
                            disparity_pl[i][j] = c
                            chil = max(disparity_pl[i-1][j] , disparity_pl[i][j-1])
                            if mo in child:
                                mom.append(mom[child.index(mo)])
                            else:
                                mom.append(mo)
                            child.append(chil)
                            
    for i in range(1,height):
        for j in range(1,width):
            if(disparity_pl[i][j] != 0):
                if(disparity_pl[i][j] in child):
                    disparity_pl[i][j] = mom[child.index(disparity_pl[i][j])]
    
    #Single contains parent value with duplication removed
    single = [] 
    [single.append(x) for x in mom if x not in single]
    print(single)
    
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution for labelling is : {td:.03f}ms")
    return single , disparity_pl