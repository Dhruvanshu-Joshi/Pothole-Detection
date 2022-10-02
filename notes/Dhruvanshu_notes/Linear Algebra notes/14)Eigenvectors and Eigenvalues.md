# Eigenvectors and Eigenvalues

When linear transformation is applied on a 2d space , various vectors get knocked of thier span.
![ee1](ee1.png)
However certain vectors maintain thier span and are only scaled.
![ee2](ee2.png)
These special vectors are kknown as the **Eigenvectors** with thier own **Eigenvalue** representing the ammount by which it is scaled.
![ee3](ee3.png)
Eigenvalue negative means that the vector is flipped and scaled.

Computation:
![ee4](ee4.png)
![ee5](ee5.png)
Therefore the transformation associated with the vector squishes it to a line for product to be zero.

![ee6](ee6.png)

Having Eigenvectors is not necessary!
![ee6](ee7.png)
Also we have a single Eigenvalue for multiple Eigenvectors.
![ee6](ee8.png)

**Eigenbasis**: if the basis vectors i a coordinate system is its eigenvector , the basis vectors are called Eigenbasis.

ex:
![ee6](ee9.png)

In cases like these we first change the basis vectors to Eigenbasis then carry out the computation and then convert back to our standard system as we are sure to get a diagonal matrix after conversion and it is much easier to work on this matrix.
![ee10](ee10.png)
But for this , there must be enough number of Eigen vectors possible.
