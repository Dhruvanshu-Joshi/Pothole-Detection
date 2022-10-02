# Projection Matrix
$P = A (A^T A)^-1 A^T$

If b is in the column space -> $Pb = b$  
Since $$b=Ax$$
Therefore, $$Pb = A (A^T A)^-1 A^T Ax$$  
$$Pb = Ax = b$$
.  

If b is perpendicular to the column space -> $Pb = 0$  
Because if b is perpendicular to the columnspace then b is in the null space of $A^T$ and hence  
$$A^T b = 0$$
Therefore $$Pb = A (A^T A)^-1 A^T b = 0$$  

Hence b = p + e  
i.e. b = Projection on Column space + Projection on Null Space  
.
![image](https://user-images.githubusercontent.com/103961320/188918351-104142a5-935e-4774-8068-c06e4fd475b6.png)
