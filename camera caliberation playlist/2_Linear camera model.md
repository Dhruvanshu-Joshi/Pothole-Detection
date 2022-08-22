# Linear camera model 

Forward imaging model: 3D to 2D

![lcm1](lcm1.png)

As derived in the stereo.md , we can find depth as 

![lcm2](lcm2.png)

where z is the depth of object , xi and yi are coordinates of projection of point p onto the image plane

![lcm3](lcm3.png)

where u and v are the projectibe projection on image plane

ox and oy are center coordinates of image

mxf and myf can be written as fx and fy where fx represents the focal length of camera in x axis amd fy represents the focal length of camera in y coordinate.

These are the Intrinsic parameters of the camera.

![lcm3](lcm4.png)

Though camera typically has only one focal length, too compensate for unequal pixel values in x and y axis (as in case of rectangular pixel), we consider focal length in x and y direction seperately.

but this model is non linear!

To go from non-linear model to linear model,we usr homogenous coordinate.
we assume a w(tilda) coordinate axis such that our plane lies on w(tilda)=1.

![lcm3](lcm5.png)

Linear models are a way of describing a response variable in terms of a linear combination of predictor variables

![lcm3](lcm6.png)

![lcm3](lcm7.png)

This whole matrix is called an intrinsic matrix.

![lcm3](lcm8.png)

Hence we succesfully mapped coordinates of camera coordinates to image coordinates.

Now we proceed to map world coordinates to camera coordinates.

![lcm3](lcm9.png)

Two vectors are said to be orthonormal if on linear transformation of one vector about the other , the basis vectors of that vector remain perpendicular. Two vectors are orthonormal if and only if their dot product is zero. For more: refer Linear Algebra notes 8)Non-Squre matrices as transformation

![lcm3](lcm10.png)

![lcm3](lcm11.png)

But again , this model is non-linear.

To make it linear we use homogenous coordinates.

![lcm3](lcm12.png)

Therefore we can now figure out mapping of point of world coordinate frame to image frame.

![lcm3](lcm13.png)