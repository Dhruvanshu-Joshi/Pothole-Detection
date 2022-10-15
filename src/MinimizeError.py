import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import math

def Eliminate(single,disparity_pl,top,bottom,right,left,depth): 
    height = depth.shape[0]
    width = depth.shape[1]
    # Now to further eliminate a region which is not pothole but has been detected even after processing , we border out the image into a smaller frame
    # all LABELLED potholes whose even a small part lies in these region are eliminated
    single1 = []
    remove = []
    remove=[]
    removel=[]
    remover=[]
    removet=[]
    removeb=[]
    [single1.append(x) for x in single]
    avg =[]
    avg_pot=[]
    for x in range(len(single)):
        sum_final =0
        dis_final_no =0
        sum_final_pot =0
        dis_final_no_pot =0
        for s in range(top[x]-50, bottom[x]+50):
            for r in range(left[x]-50 , right[x]+50):
                if(s < 0 or s >= height or r<0 or r>=width):
                    if single[x] not in remove:
                        remove.append(single[x])
                        removel.append(left[x])
                        remover.append(right[x])
                        removet.append(top[x])
                        removeb.append(bottom[x])
                else:
                    if(disparity_pl[s][r] ==0 and depth[s][r] != 0):
                        sum_final = sum_final + depth[s][r]
                        dis_final_no = dis_final_no + 1
                    else:
                        sum_final_pot = sum_final_pot + depth[s][r]
                        dis_final_no_pot = dis_final_no_pot + 1
        avg_dis_final = sum_final / dis_final_no
        avg.append(avg_dis_final)
        avg_dis_final_pot = sum_final_pot / dis_final_no_pot
        avg_pot.append(avg_dis_final_pot)
    diff_pot =[]
    for x in range(len(avg)):
        difflia = avg[x]-avg_pot[x]
        diff_pot.append(difflia)
    for i in range(len(remove)):
        single1.remove(remove[i])
        left.remove(removel[i])
        right.remove(remover[i])
        top.remove(removet[i])
        bottom.remove(removeb[i])
    disparity_rect_1 = np.copy(depth)

    return disparity_rect_1,top,bottom,right,left,single1,avg_pot