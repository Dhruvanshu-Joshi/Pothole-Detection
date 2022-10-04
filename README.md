## Pothole-Detection  
Detecting road potholes using OAK-D camera  

<!-- TABLE OF CONTENTS -->  
## Table of Contents  
- [About the Project](#about-the-project)  
    - [Aim](#aim)  
    - [Description](#description)  
    - [Tech Stack](#tech-stack)  
    - [File Structure](#file-structure)  
- [Getting Started](#getting-started)  
    - [Prerequisites](#prerequisites)  
    - [Installation](#installation)  
    - [Execution](#execution)  
- [Theory and Approach](#theory-and-approach)  
- [Algorithm Flowchart](#algorithm-flowchart)  
- [Results and Demo](#results-and-demo)  
- [Future Work](#to-dos)  
- [Contributors](#contributors)  
- [Acknowledgements and Resources](#acknowledgements-and-resources)  

<!--ABOUT THE PROJECT -->  
## About The Project   

### Aim   
Potholes are bowl-shaped openings on the road that are caused by the combined effect of wear-and-tear and weathering of the road. Potholes are not only main cause of car accidents, but also can be fatal to motorcycles. Drivers might see the pothole before they pass it, it is usually too late for them to react. Keeping this in mind , our project aims to locate the potholes present on a road through the input image and provide its distance in cm from the camera. 

###  Description   
We have used OAK-D camera to get the monochromatic stereo images of the surface which are then rectified using the inbuilt functioning of the camera. We have implemented stereo image processing algorithms to generate disparity maps and then labelled the appropriate areas in the image as pothole using the connected component labelling algorithm.  

### Tech Stack  
- [OpenCV](https://opencv.org/)  
- [Matplotlib](https://matplotlib.org/)  
- [Scikit Learn](https://scikit-learn.org/stable/)  
- [DepthAI](https://docs.luxonis.com/en/latest/)  


### File Structure  
```
📦Pothole-Detection
 ┣ 📂Assets                           #contains images taken from the left-right stereo camera
 ┃ ┗ 📂Images
 ┃ ┃ ┣ 📜LeftImage_1.png
 ┃ ┃ ┣ 📜LeftImage_2.png
 ┃ ┃ ┣ 📜RightImage_1.png
 ┃ ┃ ┣ 📜RightImage_2.png
 ┃ ┃ ┣ 📜left_image1.png
 ┃ ┃ ┣ 📜left_image2.png
 ┃ ┃ ┣ 📜left_image3.png
 ┃ ┃ ┣ 📜left_image4.png
 ┃ ┃ ┣ 📜left_image5.png
 ┃ ┃ ┣ 📜left_image6.png
 ┃ ┃ ┣ 📜left_image7.png
 ┃ ┃ ┣ 📜rightt_image1.png
 ┃ ┃ ┣ 📜rightt_image2.png
 ┃ ┃ ┣ 📜rightt_image3.png
 ┃ ┃ ┣ 📜rightt_image4.png
 ┃ ┃ ┣ 📜rightt_image5.png
 ┃ ┃ ┣ 📜rightt_image6.png
 ┃ ┃ ┗ 📜rightt_image7.png
 ┣ 📂Results
 ┃ ┗ 📂Disparity		      #contains depth map in form of .npy file generated from the Oak-D camera
 ┃ ┃ ┣ 📜dispimage_7.npy
 ┃ ┃ ┣ 📜dispimage_8.npy
 ┃ ┃ ┣ 📜pothole_depth1.npy
 ┃ ┃ ┣ 📜pothole_depth2.npy
 ┃ ┃ ┣ 📜image7.png
 ┃ ┃ ┗ 📜image8.png
 ┃ ┗ 📂Pothole Detection	      #contains final result with detected potholes
 ┃ ┃ ┣ 📜Pothole_depthimage_1.png
 ┃ ┃ ┣ 📜Pothole_depthimage_2.png
 ┃ ┃ ┣ 📜Resultwith21Matrix7.png
 ┃ ┃ ┗ 📜Resultwith21Matrix8.png
 ┣ 📂notes                            
 ┃ ┣ 📂Dhruvanshu_notes		      #contains notes created by Dhruvanshu
 ┃ ┃ ┣ 📜# What is STEREO.md
 ┃ ┃ ┣ 📂Jhon Lambert's Paper
 ┃ ┃ ┃ ┣ 📜Paper by jhon lambert.md
 ┃ ┃ ┃ ┣ 📜ref.md
 ┃ ┃ ┃ ┣ 📜s1.png
 ┃ ┃ ┃ ┣ 📜s2.png
 ┃ ┃ ┃ ┣ 📜s3.png
 ┃ ┃ ┃ ┣ 📜s4.png
 ┃ ┃ ┃ ┣ 📜s5.png
 ┃ ┃ ┃ ┣ 📜s6.png
 ┃ ┃ ┃ ┣ 📜s7.png
 ┃ ┃ ┃ ┣ 📜s8.png
 ┃ ┃ ┃ ┣ 📜s9.png
 ┃ ┃ ┃ ┣ 📜s10.png
 ┃ ┃ ┃ ┗ 📜s11.png
 ┃ ┃ ┣ 📂Linear Algebra notes
 ┃ ┃ ┃ ┣ 📜10_CrossProducts.md
 ┃ ┃ ┃ ┣ 📜13_Change of basis.md
 ┃ ┃ ┃ ┣ 📜14)Eigenvectors and Eigenvalues.md
 ┃ ┃ ┃ ┣ 📜3_Linear transformation and Matrices note.md
 ┃ ┃ ┃ ┣ 📜4_Multiplication.md
 ┃ ┃ ┃ ┣ 📜5_Three dimensional linear transformati.md
 ┃ ┃ ┃ ┣ 📜6_Determinant.md
 ┃ ┃ ┃ ┣ 📜7_Inverse matrix.md
 ┃ ┃ ┃ ┣ 📜8)Non-Squre matrices as transformations.md
 ┃ ┃ ┃ ┣ 📜9_Dot products and duality.md
 ┃ ┃ ┃ ┣ 📜Cramer's rule.md
 ┃ ┃ ┃ ┣ 📜LA1.jpg
 ┃ ┃ ┃ ┣ 📜LAchp2.jpg
 ┃ ┃ ┃ ┣ 📜La2.jpg
 ┃ ┃ ┃ ┣ 📜La3.jpg
 ┃ ┃ ┃ ┣ 📜Linear algebra intro.md
 ┃ ┃ ┃ ┣ 📜T1.png
 ┃ ┃ ┃ ┣ 📜T3.png
 ┃ ┃ ┃ ┣ 📜a1.png
 ┃ ┃ ┃ ┣ 📜cb1.png
 ┃ ┃ ┃ ┣ 📜cb2.png
 ┃ ┃ ┃ ┣ 📜cb3.png
 ┃ ┃ ┃ ┣ 📜cb4.png
 ┃ ┃ ┃ ┣ 📜cb5.png
 ┃ ┃ ┃ ┣ 📜cb6.png
 ┃ ┃ ┃ ┣ 📜cp1.png
 ┃ ┃ ┃ ┣ 📜cp2.png
 ┃ ┃ ┃ ┣ 📜cp3.png
 ┃ ┃ ┃ ┣ 📜cp4.png
 ┃ ┃ ┃ ┣ 📜cp5.png
 ┃ ┃ ┃ ┣ 📜cp6.png
 ┃ ┃ ┃ ┣ 📜cp7.png
 ┃ ┃ ┃ ┣ 📜cp8.png
 ┃ ┃ ┃ ┣ 📜cp9.png
 ┃ ┃ ┃ ┣ 📜cp10.png
 ┃ ┃ ┃ ┣ 📜cp11.png
 ┃ ┃ ┃ ┣ 📜cp12.png
 ┃ ┃ ┃ ┣ 📜cr1.png
 ┃ ┃ ┃ ┣ 📜cr2.png
 ┃ ┃ ┃ ┣ 📜cr3.png
 ┃ ┃ ┃ ┣ 📜cr4.png
 ┃ ┃ ┃ ┣ 📜cr5.png
 ┃ ┃ ┃ ┣ 📜cr6.png
 ┃ ┃ ┃ ┣ 📜d1.png
 ┃ ┃ ┃ ┣ 📜d2.png
 ┃ ┃ ┃ ┣ 📜d3.png
 ┃ ┃ ┃ ┣ 📜d4.png
 ┃ ┃ ┃ ┣ 📜d5.png
 ┃ ┃ ┃ ┣ 📜d6.png
 ┃ ┃ ┃ ┣ 📜d7.png
 ┃ ┃ ┃ ┣ 📜dp1.png
 ┃ ┃ ┃ ┣ 📜dp2.png
 ┃ ┃ ┃ ┣ 📜dp3.png
 ┃ ┃ ┃ ┣ 📜dp4.png
 ┃ ┃ ┃ ┣ 📜dp5.png
 ┃ ┃ ┃ ┣ 📜dp6.png
 ┃ ┃ ┃ ┣ 📜dp7.png
 ┃ ┃ ┃ ┣ 📜dp8.png
 ┃ ┃ ┃ ┣ 📜dp9.png
 ┃ ┃ ┃ ┣ 📜ee1.png
 ┃ ┃ ┃ ┣ 📜ee2.png
 ┃ ┃ ┃ ┣ 📜ee3.png
 ┃ ┃ ┃ ┣ 📜ee4.png
 ┃ ┃ ┃ ┣ 📜ee5.png
 ┃ ┃ ┃ ┣ 📜ee6.png
 ┃ ┃ ┃ ┣ 📜ee7.png
 ┃ ┃ ┃ ┣ 📜ee8.png
 ┃ ┃ ┃ ┣ 📜ee9.png
 ┃ ┃ ┃ ┣ 📜ee10.png
 ┃ ┃ ┃ ┣ 📜im1.png
 ┃ ┃ ┃ ┣ 📜img1.png
 ┃ ┃ ┃ ┣ 📜img2.png
 ┃ ┃ ┃ ┣ 📜img3.png
 ┃ ┃ ┃ ┣ 📜img4.png
 ┃ ┃ ┃ ┣ 📜img5.png
 ┃ ┃ ┃ ┣ 📜img6.png
 ┃ ┃ ┃ ┣ 📜img7.png
 ┃ ┃ ┃ ┣ 📜img8.png
 ┃ ┃ ┃ ┣ 📜img9.png
 ┃ ┃ ┃ ┣ 📜img10.png
 ┃ ┃ ┃ ┣ 📜img11.png
 ┃ ┃ ┃ ┣ 📜img12.png
 ┃ ┃ ┃ ┣ 📜mm1.png
 ┃ ┃ ┃ ┣ 📜mm2.png
 ┃ ┃ ┃ ┣ 📜mm3.png
 ┃ ┃ ┃ ┣ 📜mm4.png
 ┃ ┃ ┃ ┣ 📜ns1.png
 ┃ ┃ ┃ ┣ 📜ns2.png
 ┃ ┃ ┃ ┣ 📜ns3.png
 ┃ ┃ ┃ ┣ 📜ns4.png
 ┃ ┃ ┃ ┣ 📜ns5.png
 ┃ ┃ ┃ ┣ 📜ns6.png
 ┃ ┃ ┃ ┣ 📜t2.png
 ┃ ┃ ┃ ┣ 📜t3.png
 ┃ ┃ ┃ ┣ 📜t4.png
 ┃ ┃ ┃ ┣ 📜t5.png
 ┃ ┃ ┃ ┣ 📜t6.png
 ┃ ┃ ┃ ┣ 📜t7.png
 ┃ ┃ ┃ ┣ 📜t8.png
 ┃ ┃ ┃ ┗ 📜t9.png
 ┃ ┃ ┣ 📂OakD camera
 ┃ ┃ ┃ ┣ 📜OakD.md
 ┃ ┃ ┃ ┗ 📜oakd1.png
 ┃ ┃ ┣ 📂Road Surface Fitting
 ┃ ┃ ┃ ┣ 📂Main Theory
 ┃ ┃ ┃ ┃ ┣ 📜Fitting_Methods.md
 ┃ ┃ ┃ ┃ ┣ 📜bf1.png
 ┃ ┃ ┃ ┃ ┣ 📜bf2.png
 ┃ ┃ ┃ ┃ ┣ 📜11.png
 ┃ ┃ ┃ ┃ ┣ 📜l2.png
 ┃ ┃ ┃ ┃ ┣ 📜l3.png
 ┃ ┃ ┃ ┃ ┣ 📜l4.png
 ┃ ┃ ┃ ┃ ┣ 📜ref.md
 ┃ ┃ ┃ ┃ ┣ 📜wl1.png
 ┃ ┃ ┃ ┃ ┗ 📜wl2.png
 ┃ ┃ ┃ ┣ 📂ProjectionMatrices_LeastSquares
 ┃ ┃ ┃ ┃ ┣ 📜Projection Matrices and Least Squares.md
 ┃ ┃ ┃ ┃ ┣ 📜P1.png
 ┃ ┃ ┃ ┃ ┣ 📜P2.png
 ┃ ┃ ┃ ┃ ┣ 📜p3.png
 ┃ ┃ ┃ ┃ ┣ 📜p4.png
 ┃ ┃ ┃ ┃ ┣ 📜P5.png
 ┃ ┃ ┃ ┃ ┣ 📜p6.png
 ┃ ┃ ┃ ┃ ┣ 📜p7.png
 ┃ ┃ ┃ ┃ ┣ 📜p8.png
 ┃ ┃ ┃ ┃ ┣ 📜p9.png
 ┃ ┃ ┃ ┃ ┣ 📜p10.png
 ┃ ┃ ┃ ┃ ┣ 📜p11.png
 ┃ ┃ ┃ ┃ ┣ 📜p12.png
 ┃ ┃ ┃ ┃ ┣ 📜p13.png
 ┃ ┃ ┃ ┃ ┣ 📜P14.png
 ┃ ┃ ┃ ┃ ┣ 📜p15.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Robust Regression
 ┃ ┃ ┃ ┃ ┣ 📜Robust Regression.md
 ┃ ┃ ┃ ┃ ┣ 📜rr1.png
 ┃ ┃ ┃ ┃ ┣ 📜rr2.png
 ┃ ┃ ┃ ┃ ┣ 📜rr3.png
 ┃ ┃ ┃ ┃ ┣ 📜rr4.png
 ┃ ┃ ┃ ┃ ┣ 📜rr5.png
 ┃ ┃ ┃ ┃ ┣ 📜rr6.png
 ┃ ┃ ┃ ┃ ┣ 📜rr7.png
 ┃ ┃ ┃ ┃ ┗ 📜ref.md
 ┃ ┃ ┃ ┗ 📂Sample_Code
 ┃ ┃ ┃ ┃ ┣ 📜Best_line_code_tutorial.md
 ┃ ┃ ┃ ┃ ┣ 📜ed1.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┣ 📂Thesis-YaqiLi
 ┃ ┃ ┃ ┣ 📂Intoduction
 ┃ ┃ ┃ ┃ ┗ 📂Background
 ┃ ┃ ┃ ┃ ┃ ┣ 📜2 Background.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜s1.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜s2.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜s3.png
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂3-Approach to Pothole Detection System
 ┃ ┃ ┃ ┃ ┣ 📂3.1_Stereo Camera Caliberation
 ┃ ┃ ┃ ┃ ┃ ┣ 📜3.1_Stereo Camera Caliberation.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scc1.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scc2.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scc3.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scc4.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scc5.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜scc6.png
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┃ ┣ 📂3.2 Stereo Processing
 ┃ ┃ ┃ ┃ ┃ ┣ 📜RefPaper_Stereo Processing.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp.2.1.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp.2.2.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp.2.3.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp.2.4.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp.2.5.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp.2.6.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp.2.7.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp0.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp1.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp2.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp3.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp4.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp5.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜sp6.png
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┃ ┣ 📂3.3 Disparity Image Reprojection
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Disparity Image Reprojection.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜d3d1.jpg
 ┃ ┃ ┃ ┃ ┃ ┗ 📜d3d2.jpg
 ┃ ┃ ┃ ┃ ┣ 📂3.4 Road Surface Fitting
 ┃ ┃ ┃ ┃ ┃ ┣ 📜# Road surface Fiiting.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rf1.png
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┃ ┣ 📂3.5 Road Pothole Labelling
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Road Pothole Labelling.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rf2.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rf3.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rpl3.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rpl4.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜rpl5.png 
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┃ ┣ 📜3_Approach to Pothole Detection System.md
 ┃ ┃ ┃ ┃ ┣ 📜ap1.png
 ┃ ┃ ┃ ┃ ┣ 📜ap2.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂4-Experimental setup
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Experimental Setup.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜es1.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜es2.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜es3.png
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂5- Result
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Result.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜R1.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜R2.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜R3.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜R4.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜R5.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜R6.png
 ┃ ┃ ┃ ┃ ┃ ┣ 📜R7.png
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂6-Conclusion
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Conclusion.md
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂7&8-end
 ┃ ┃ ┃ ┃ ┃ ┣ 📜Possible upgrades and Code Implementation.md
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┗ 📂camera caliberation playlist
 ┃ ┃ ┃ ┣ 📂Camera Calibration
 ┃ ┃ ┃ ┃ ┣ 📜3_Camera caliberation.md
 ┃ ┃ ┃ ┃ ┣ 📜cc1.png
 ┃ ┃ ┃ ┃ ┣ 📜cc2.png
 ┃ ┃ ┃ ┃ ┣ 📜cc3.png
 ┃ ┃ ┃ ┃ ┣ 📜cc4.png
 ┃ ┃ ┃ ┃ ┣ 📜cc5.png
 ┃ ┃ ┃ ┃ ┣ 📜cc6.png
 ┃ ┃ ┃ ┃ ┣ 📜cc7.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Computing Depth
 ┃ ┃ ┃ ┃ ┣ 📜12_Computing Depth.md
 ┃ ┃ ┃ ┃ ┣ 📜cd1.png
 ┃ ┃ ┃ ┃ ┣ 📜cd2.png
 ┃ ┃ ┃ ┃ ┣ 📜cd3.png
 ┃ ┃ ┃ ┃ ┣ 📜cd4.png
 ┃ ┃ ┃ ┃ ┣ 📜cd5.png
 ┃ ┃ ┃ ┃ ┣ 📜cd6.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Epipolar Geometry
 ┃ ┃ ┃ ┃ ┣ 📜8_Epipolar Geometry.md
 ┃ ┃ ┃ ┃ ┣ 📜eg1.png
 ┃ ┃ ┃ ┃ ┣ 📜eg2.png
 ┃ ┃ ┃ ┃ ┣ 📜eg3.png
 ┃ ┃ ┃ ┃ ┣ 📜eg4.png
 ┃ ┃ ┃ ┃ ┣ 📜eg5.png
 ┃ ┃ ┃ ┃ ┣ 📜eg6.png
 ┃ ┃ ┃ ┃ ┣ 📜eg7.png
 ┃ ┃ ┃ ┃ ┣ 📜eg8.png
 ┃ ┃ ┃ ┃ ┣ 📜eg9.png
 ┃ ┃ ┃ ┃ ┣ 📜eg10.png
 ┃ ┃ ┃ ┃ ┣ 📜eg11.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Estimating Fundamental Matrices
 ┃ ┃ ┃ ┃ ┣ 📜10_Estimating Fundamental Matrices.md
 ┃ ┃ ┃ ┃ ┣ 📜efm1.png
 ┃ ┃ ┃ ┃ ┣ 📜efm2.png
 ┃ ┃ ┃ ┃ ┣ 📜efm3.png
 ┃ ┃ ┃ ┃ ┣ 📜efm4.png
 ┃ ┃ ┃ ┃ ┣ 📜efm5.png
 ┃ ┃ ┃ ┃ ┣ 📜efm6.png
 ┃ ┃ ┃ ┃ ┣ 📜efm7.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Finding Correspondences
 ┃ ┃ ┃ ┃ ┣ 📜11_finding Correspondences.md
 ┃ ┃ ┃ ┃ ┣ 📜fc1.png
 ┃ ┃ ┃ ┃ ┣ 📜fc2.png
 ┃ ┃ ┃ ┃ ┣ 📜fc3.png
 ┃ ┃ ┃ ┃ ┣ 📜fc4.png
 ┃ ┃ ┃ ┃ ┣ 📜fc5.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Intrinsic and Extrinsic Matrices
 ┃ ┃ ┃ ┃ ┣ 📜4_Intrinsic and Extrinsic Matrix.md
 ┃ ┃ ┃ ┃ ┣ 📜ei1.png
 ┃ ┃ ┃ ┃ ┣ 📜ei2.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Linear Camera Model
 ┃ ┃ ┃ ┃ ┣ 📜2_Linear camera model.md
 ┃ ┃ ┃ ┃ ┣ 📜lcm1.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm2.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm3.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm4.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm5.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm6.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm7.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm8.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm9.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm10.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm11.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm12.png
 ┃ ┃ ┃ ┃ ┣ 📜lcm13.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Overview
 ┃ ┃ ┃ ┃ ┗ 📂Uncalibrated Stereo
 ┃ ┃ ┃ ┃ ┃ ┣ 📜6_Uncaliberated stereo overview.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜uc1.png
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Overview
 ┃ ┃ ┃ ┃ ┃ ┣ 📜1_overview.md
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Problem of Uncalibrated Stereo
 ┃ ┃ ┃ ┃ ┃ ┣ 📜7_Problem in Uncaliberated Stereo.md
 ┃ ┃ ┃ ┃ ┃ ┣ 📜uc2.png
 ┃ ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂Simple Stereo
 ┃ ┃ ┃ ┃ ┣ 📜5_Stereo.md
 ┃ ┃ ┃ ┃ ┣ 📜s1.png
 ┃ ┃ ┃ ┃ ┣ 📜s2.png
 ┃ ┃ ┃ ┃ ┣ 📜s3.png
 ┃ ┃ ┃ ┃ ┣ 📜s4.png
 ┃ ┃ ┃ ┃ ┣ 📜s5.png
 ┃ ┃ ┃ ┃ ┣ 📜s6.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┣ 📂stereo vision in nature
 ┃ ┃ ┃ ┃ ┣ 📜9_stereo vision in nature.md
 ┃ ┃ ┃ ┃ ┣ 📜sn1.png
 ┃ ┃ ┃ ┃ ┣ 📜sn2.png
 ┃ ┃ ┃ ┃ ┣ 📜sn3.png
 ┃ ┃ ┃ ┃ ┣ 📜sn4.png
 ┃ ┃ ┃ ┃ ┣ 📜sn5.png
 ┃ ┃ ┃ ┃ ┗ 📜ref
 ┃ ┃ ┃ ┗ 📜reference
 ┃ ┗ 📂Prachi_notes		      #contains notes created by Prachi
 ┃ ┃ ┣ 📂Road_Surface_Fitting
 ┃ ┃ ┃ ┣ 📜Least_Squares_Fitting.md
 ┃ ┃ ┃ ┣ 📜Linear_Square_Regression.md
 ┃ ┃ ┃ ┗ 📜least_square_method.md
 ┃ ┃ ┣ 📜3b1b Notes upto lect 9.pdf
 ┃ ┃ ┣ 📜3b1b notes from dot product till end.pdf
 ┃ ┃ ┣ 📜Paper notes.pdf
 ┃ ┃ ┣ 📜Paper-Yaqi-Li.pdf
 ┃ ┃ ┗ 📜Sterio_notes.md
 ┣ 📂src                              #contains sorce codes
 ┃ ┣ 📂asset_npys		      #contains depth map in form of npys
 ┃ ┃ ┣ 📜depth_image_0.npy
 ┃ ┃ ┣ 📜depth_image_1.npy
 ┃ ┃ ┣ 📜depth_image_2.npy
 ┃ ┃ ┣ 📜depth_image_3.npy
 ┃ ┃ ┣ 📜depth_image_4.npy
 ┃ ┃ ┣ 📜image_0.npy
 ┃ ┃ ┣ 📜image_1.npy
 ┃ ┃ ┣ 📜image_2.npy
 ┃ ┃ ┣ 📜image_3.npy
 ┃ ┣ 📜Boxed.ipynb
 ┃ ┣ 📜DepthGenerator.ipynb
 ┃ ┣ 📜Detection.ipynb
 ┃ ┣ 📜Labelling.ipynb
 ┃ ┣ 📜MinimizeError.ipynb
 ┃ ┣ 📜Pothole_Detection.ipynb
 ┃ ┣ 📜Pothole_Detection.py
 ┃ ┣ 📜Result.ipynb
 ┃ ┣ 📜SurfaceFit.ipynb
 ┃ ┣ 📜data.ipynb
 ┃ ┗ 📜main.ipynb
 ┗ 📜README.md
```


<!-- GETTING STARTED -->  
## Getting Started  

### Prerequisites  
- Should have python environment. To establish python environment, refer [here](https://www.tutorialspoint.com/python/python_environment.htm) for the setup.  
OR   
You can create a virtual environment referring [this](https://docs.luxonis.com/en/latest/pages/tutorials/first_steps/#create-python-virtualenv-optional)   
- Python libraries  
    - [DepthAI](https://docs.luxonis.com/en/latest/#demo-script)  
    - [OpenCV](https://pypi.org/project/opencv-python/)   
`pip install opencv-python`  
    - [Scikit](https://scikit-learn.org/stable/install.html)   
`pip install scikit-learn`  
    - [numpy](https://numpy.org/install/)   
`pip install numpy`  
    - [Matplotlib](https://matplotlib.org/stable/index.html#installation)  
	`pip install matplotlib`  
    - Modulling

	`pip install ipynb`

### Installation   
Clone the repo      
    
    git clone https://github.com/Dhruvanshu-Joshi/Pothole-Detection.git
    

### Execution  
-	Connect the OAK-D camera   
-	Run [Save_Image]() code to capture the stereo images.  
-	Run [Rectification_Disparity]() code to get the disparity map  
-	For all further activities, run []() code  


<!-- THEORY AND APPROACH -->  
## Theory and Approach  
1.	The stereo images are captured using the depth camera.  
2.	They are then rectified using the DepthAI functions that are based on the traditional geometric methods.   
3.	Then the disparity map is generated using StereoSGBM (semi global matching algorithm). Given the disparity map and stereo camera parameters, the corresponding coordinates in 3-dimensional coordinate system can be calculated.  
4.	Given all 3D points in an image, a road surface can be fitted using the bi-squares weighted robust least-squares algorithm.   
5.	Then all the outliers can be labelled as road potholes.  

<!--Flowchart -->  
## Algorithm Flowchart  
Simplified code structure    
<img src ="https://user-images.githubusercontent.com/103961320/193153591-f62cc7c7-1151-419b-acc2-73f2bedf3319.png" width="50%" height="30%"/> 

<!-- RESULTS AND DEMO -->  
## Results and Demo

<img src ="https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/notes/Assets/Images/LeftImage_1.png" width="30%" height="30%"/> <img src ="https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/notes/Assets/Images/RightImage_1.png" width="30%" height="30%"/>

<img src ="https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/notes/Results/Pothole%20Detection/Pothole_depthimage_1.png" width="50%" height="50%"/>

<img src ="https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/notes/Assets/Images/LeftImage_2.png" width="30%" height="30%"/> <img src ="https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/notes/Assets/Images/RightImage_2.png" width="30%" height="30%"/>

<img src ="https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/notes/Results/Pothole%20Detection/Pothole_depthimage_2.png" width="50%" height="50%"/>

![Result_image_1](https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/main/Results/Pothole%20Detection/Resultwith21Matrix7.png)


<!-- FUTURE WORK -->  
## Future Work  
- [x] Detect Potholes in Images  
- [ ] Detect Potholes in Videos  
- [ ] Detect Potholes in Real-Time  

<!-- CONTRIBUTORS -->  
## Contributors  
* [Dhruvanshu Joshi]( https://github.com/Dhruvanshu-Joshi)  
* [Prachi Doshi]( https://github.com/Prachi-Doshi)  


<!-- ACKNOWLEDGEMENTS AND REFERENCES -->  
## Acknowledgements and Resources  
- [SRA VJTI](https://github.com/SRA-VJTI) Eklavya 2022  
- Our mentors [Toshan Luktuke](https://github.com/toshan-luktuke), [Dhruv Kunjadiya](https://github.com/Dhruv454000) and [Rishabh Bali](https://github.com/Ris-Bali) for their guidance throughout this project  
- [Yaqi-Li Research Paper](https://etd.ohiolink.edu/apexprod/rws_etd/send_file/send?accession=case1525708920748809&disposition=inline) for main refference  
- [John Lambert Research Paper](https://johnwlambert.github.io/stereo/) for stereo related reference  
- [Video](https://www.youtube.com/watch?v=bRkUGqsz6SI) to know more on stereo  
- [Video](https://www.youtube.com/watch?v=S-UHiFsn-GI&list=PL2zRqk16wsdoCCLpou-dGo7QQNks1Ppzo&index=3) on Camera Calibration  
- For more resources refer [References]() section in the Report.  
