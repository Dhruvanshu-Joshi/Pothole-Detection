import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import math

def load_depth_map(image):
    image1 = image[::-1]
    end = image1[2]+image1[1]+image1[0]
    if end == 'npy':
        depth = np.load(image) #loading the depth-map generated from the camera
    else:
        depth = cv2.imread(image,0)
    plt.imshow(depth, "gray")
    plt.colorbar()
    plt.show()
    return depth

def Surface_chart_of_depth(height,width,depth):
    w=[]
    h=[]
    for i in range(height):
            for j in range(width):
                w.append(i)
                h.append(j)
    w1 = np.reshape(w,(height,width))
    h1 = np.reshape(h,(height,width))
    
    return w1,h1,w,h

    # max_d = 190 # maximum disparity of Oak-D camera already known
    # min_d = (882.5 * 7.5) / 190 # Minimum disparity of Oak-D camera
