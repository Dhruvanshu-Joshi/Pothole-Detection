# Possible upgrades and Implementation

## **Possible upgrades**

**Hardware Improvement**

    1)When it comes to industry application, we can use Internet Protocol cameras(IP cameras).

    The IP cameras can communicate via computer network and internet within the car.

    The cameras have a high-resolution which is useful to obtain more featurs on road surface which gives more accurate disparity image.

    2)Led laser light can be added to the setup so as to get better performance in evening and when there is no light.

    If the road surface is flat, the projection of LED light will be straight. Otherwise, the projection of the LED light should be curved at the pothole region.

    3)The disparity calculation algorithm applied has some limitations.
    
        1)Its accuracy in the texture-less area and occlusion boundaries area might decrease for less features in these area.

        2)For well rectified stereo image pairs, corresponding pixels might exist in the same line only.Therefore, we can reduce the search range for searching corresponding pixels.A smaller search range might reduce the matching errors and reduce the matching time as well.

## **Code Implementation**

There are 2 versions implementation of the proposed system. We firstly implement it in MATLAB. Compared with the accuracy of detection with OpenCV, the accuracy of detection with MATLAB is higher. The reason is that the accuracy of the matching for corresponding pixels is higher in MATLAB. 

However, as trade off, the detection in MATLAB take around 4 times longer. In MATLAB, the detection of potholes taking 20 seconds to detect the pothole, compared with 5 seconds to detect the same pothole in the OpenCV.

Besides, MATLAB need a license to use. However, the OpenCV is an open source computer vision library. It is more flexible to apply in the industry