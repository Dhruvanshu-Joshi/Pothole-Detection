# What is STEREO

Single camera captures the flat image of an object.

In order to get 3D depth image of an object ,  we use stereo csmera. The two cameras used in stereo vision have all possible type of distortion.To remove this distortion we caliberate the camera according to a known frame i.e. checkerboard.

Now we take the image of the object in any orientation and take the image of the object in both the cameras at the same time.

Object whose depth is required is selected in left image plane. We use epipolar geometry to get a small region of interest in the right image plane.

![ref image 1](https://scontent-bom1-1.xx.fbcdn.net/v/t39.30808-6/300047900_798334438248341_8868216963068833691_n.jpg?stp=dst-jpg_p552x414&_nc_cat=104&ccb=1-7&_nc_sid=730e14&_nc_ohc=lra4Kh2AitMAX-xLjxL&tn=kUlyq_1UMr9Vo7RK&_nc_ht=scontent-bom1-1.xx&oh=00_AT9arlXlTXCtWuRkmP4o7hFXu2FeLjxf7UhiPVWhKmURzQ&oe=63046FEC)

![ref image 2](https://scontent.fbom3-1.fna.fbcdn.net/v/t39.30808-6/299155110_798331481581970_6067365097503398892_n.jpg?_nc_cat=108&ccb=1-7&_nc_sid=0debeb&_nc_ohc=1wWnqoT3u2oAX8dHNMK&_nc_ht=scontent.fbom3-1.fna&oh=00_AT99-c_cIg2JskB1wXdE6RZgeq_e9zrjOlMrTxyfL_fRmQ&oe=63052218)

Now we compare pixel feature from the left image plane with the pixels in the region of interest in the right image plane and get the corresponding pixel in right image plane. Now from these two pixels we calculate the depth.

![depth image](https://scontent-bom1-1.xx.fbcdn.net/v/t39.30808-6/300171893_798334414915010_4963760495110182852_n.jpg?stp=dst-jpg_p552x414&_nc_cat=105&ccb=1-7&_nc_sid=730e14&_nc_ohc=qQ_kS_dWpCAAX8RkKvN&_nc_ht=scontent-bom1-1.xx&oh=00_AT_kzKfkt1BTAPf5dVnoUlTJ4xezm5h-QxrJVmFjM_G3nw&oe=63042E92)

To understand better XL and XR raise your right hand and view it from the left eye only. XL is the distance between the leftmost point and the hand. Now close the left eye and view it from right eye only. XR is the distance between the leftmost point and the hand. The distance between the two images is XL - XR

Basically we use 2 camera at known certain distance to find out the depth of the object in a image. Its important to know thw camera positions.

This concept is based on our human eye where the brain knows where the two eyes are and percieves image depth accordingly.

![reference 1](https://www.youtube.com/watch?v=O7B2vCsTpC0)

![reference 2](https://www.youtube.com/watch?v=EDeHyb21L2M)

![reference 3](https://www.youtube.com/watch?v=bRkUGqsz6SI&t=119s)

An ir dot pattern sensor is also provided in intel realsense camera so that a dotted pattern is produced by which we can also perform depth calculation for smooth walls(because smooth walls have no other features) and general depth images with more accuracy.

Stereo vision is used in deep learning.For eg:object saliency.