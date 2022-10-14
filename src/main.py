import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits import mplot3d
from matplotlib import cm
import scipy.optimize
from scipy.stats import cauchy
import math
from DepthGenerator import load_depth_map
from DepthGenerator import Surface_chart_of_depth
from data import Prepare_Data_without_outliers
from SurfaceFit import Surface_fit_of_Road
from Detection import pothole_detection
from Labelling import pothole_labelling
from Boxed import Rectangle
from MinimizeError import Eliminate
from Result import Final_result
import os
from datetime import datetime

def main():
    
    filename = input("Enter the name of the file")
    path = os.path.abspath(filename)
    print(path)
    start = datetime.now()
    depth = load_depth_map(path)
    
    depth3d = np.copy(depth) # save a copy of the depth map in a new variable
    
    
    width = depth.shape[1] # store the width of depth image
    height = depth.shape[0]# store the height of depth image
    
    max_d = 190 # maximum disparity of Oak-D camera already known
    min_d = (882.5 * 7.5) / 190 # Minimum disparity of Oak-D camera
    
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution input is : {td:.03f}ms")
    
    start = datetime.now()
    
    w1 , h1,w,h = Surface_chart_of_depth(height,width,depth)
    
    depth1 , depth3d , d2,w2,h2,d1 = Prepare_Data_without_outliers(depth ,depth3d , min_d , max_d )
    
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution of data preparation is : {td:.03f}ms")
    
    Expected_surface = Surface_fit_of_Road(d2,w2,h2,d1,w1,h1,h,w,height,width)
    
    start = datetime.now()
    
    pothole = pothole_detection(depth,Expected_surface,h1,w1,min_d,max_d)
    
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution of pothole detection is : {td:.03f}ms")
    
    start = datetime.now()
    single_val,label = pothole_labelling(depth,pothole)
    
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution of above program is : {td:.03f}ms")
    
    start = datetime.now()
    
    top,bottom,right,left = Rectangle(depth,pothole,single_val,label)
    
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution of above program is : {td:.03f}ms")
    
    start = datetime.now()
    
    eliminated_pothole_boxed,top,bottom,right,left,single_val_1,distance = Eliminate(single_val,label,top,bottom,right,left,depth)
    
    end = datetime.now()
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution of above program is : {td:.03f}ms")
    
    start = datetime.now()
    
    detected_pothole = Final_result(top,bottom,right,left,single_val_1,distance,eliminated_pothole_boxed)
    
    end = datetime.now()
 
    # find difference loop start and end time and display
    td = (end - start).total_seconds() * 10**3
    print(f"The time of execution of above program is : {td:.03f}ms")

if __name__=="__main__":
    main()