# Epipolar Geometry

Epipole: The intersection of line joining the origin of one camera with the origin if the other camera is known as epipole.

![eg1](eg1.png)

Epipolar plane

![eg2](eg2.png)

there is a vector that is perpendicular to the epipolar plane

![eg3](eg3.png)

![eg4](eg4.png)

![eg5](eg5.png)

Important property of essential matrix is that we can decompose it into translational matrix and rotational matrix

![eg6](eg6.png)

How do we find E?

We find coordinates of object in the left camera and in the right camera

![eg7](eg7.png)

![eg8](eg8.png)

We substitute this in the epipolar constraint

![eg9](eg9.png)

zl and zr are depth of object throgh the left and right camera.

However , for any point in the world until nd unless it lies on the camera , it is not zero.Hence we can eliminate them!

![eg10](eg10.png)

kl and kr are 3 by 3 matrix and hence product of all the matrices is another 3 by 3 matrices which is zero.

![eg11](eg11.png)