# Projection matrix
![P1](P1.png)

If a vector b is such that:

    it is entirely in this column space , Pb=b
        
        now b is entirely in the column space hence we can write b = AX
   ![P1](P1.png)
        
    it is perpendicular to the column space Pb=0
        
        perpendicular to the column space means I am in the null space of A transpose

![P3](p3.png)

question: Find the best straight line

![P4](p4.png)

We assume  a line y = C+ Dt which does not go through these lines.

TO find the best straight line we need to minimize the error.

assume the line to pass through the points given in question

we get:
   
   C + D = 1
   
   C + 2D = 2
   
   C + 3D = 2
    
 ![P5](P5.png)
 
 replace 3 with 2 in soln matrix.
 
 Here the we get no soln.
 
 We want to make thw error small hence we try to make AX -b as small as possible which is the length of the vector
  
  ![P6](p6.png)
 
 Now what is this error in the picture.
  
  ![P7](p7.png) 
  
 we are trying to minimize: e1^2 + e2^2 + e3^2
 
 This is linear regression
 
 Let P be the point on the line , b be the base vectors and e be the distance b/w them.
 
 Hence we have p1,b1,e1,p2,e2,b2,p3,e3 and b3.
 
 ![P9](p9.png)
 ![P8](p8.png) 
 
 P is the closest point on the column space  

back to the question

![P10](p10.png)

we use this estimate of x whenever we solbve for error or noise

![P11](p11.png)

A^tA is expected to be symmetrical and inversible

![P12](p12.png)

Now A^t x is: [5]
              [11]

we write the whole sole as an augumented matrix:

![P13](p13.png)

On solving , we get D = 1/2 and C = 2/3

Hence the best line is: y  = 2/3 + 1/2t

P1 = 7/6  , b1=1  ---> e1 = -1/6

P2 = 5/3  , b2=2  ---> e2 = 1/3

P3 = 13/6 , b3=2  ---> e3 = -1/6

![P14](P14.png)

Also , the projection vector and the error vector are perpendicular

hence, P1e1 + P2e2 + P3e3 = 0

Hence , the error vector is perpendicular to the whole column space

Also , A = Px

To prove that A transpose A is invertible because A has independent columns, ![P15](p15.png)

To prove : A^tA is invertible

suppose A^tAx = 0

![P16](p16.png)

Columns are definitely independent if they are perpendicular unit vectors(orthonormal vectors).
