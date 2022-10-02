# Conclusion

Using this thesis, we can correctly detect the road pothole in 5 seconds under good lighting condition.

We achieved this performance with three insights. 

The first is using the stereo camera, which can provide the 3-dimensional information in the image plane. Therefore, the geometric information of potholes can be obtained alongwith the distance from the pothole to car.

The second is to apply the Semiglobal Matching Algorithm. It is an effective way to find the corresponding pixels in the stereo image pairs. Once we obtain the corresponding pixels, the disparity image can be calculated easily.

The third is that model the road surface using bi-square weighted robust least-squares method. All the outliers below the modeled road surface can be detected as road pothole regions.