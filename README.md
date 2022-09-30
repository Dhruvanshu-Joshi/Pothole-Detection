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
This project aims at detecting Potholes present on the road surface and then show whether there is a single pothole or there are multiple potholes present in the region.  

###  Description   
We have used OAK-D camera to get the monochromatic stereo images of the surface which are then rectified using the inbuilt functioning of the camera. We have implemented stereo image processing algorithms to generate disparity maps and then labelled the appropriate areas in the image as pothole using the connected component labelling algorithm.  

### Tech Stack  
- [OpenCV](https://opencv.org/)  
- [Matplotlib](https://matplotlib.org/)  
- [Scikit Learn](https://scikit-learn.org/stable/)  
- [DepthAI](https://docs.luxonis.com/en/latest/)  


### File Structure  
```
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

### Installation   
Clone the repo      
    ```git
    git clone https://github.com/Dhruvanshu-Joshi/Pothole-Detection.git
    ```

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
![Pothole_Detection_Flowchart](https://user-images.githubusercontent.com/103961320/193153591-f62cc7c7-1151-419b-acc2-73f2bedf3319.png)

<!-- RESULTS AND DEMO -->  
## Results and Demo
![Result_image_1](https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/main/Results/Pothole%20Detection/Resultwith21Matrix7.png)

![Result_image_2](https://raw.githubusercontent.com/Dhruvanshu-Joshi/Pothole-Detection/main/Results/Pothole%20Detection/Resultwith21Matrix8.png)

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
