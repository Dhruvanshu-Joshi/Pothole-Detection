# Estimating Fundamental Matrices

We find a set of corresponding features in the left and right image.

![efm1](efm1.png)

![efm2](efm2.png)

![efm3](efm3.png)

if we multiply the fundamental matrix with k , we define the same epipolar geometry.

![efm4](efm4.png)

![efm5](efm5.png)

We solve this as we solved for Eigenvectors using function F and then use vector f to find the fundamental matrix F

Compute Essential matrix from fundamental matrix and from this we calculate the Rotational and Transpose of the matrix. 

![efm6](efm6.png)

Hence , our stereo system is fully caliberated.

![efm7](efm7.png)