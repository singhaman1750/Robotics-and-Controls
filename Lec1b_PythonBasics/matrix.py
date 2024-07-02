import numpy as np

A = np.array(
    [[2, 3],
     [4,-6]]
)

print("A:", A)

b = np.array([3,4])

print("b:",b)

c = A.dot(b)

print("c:", c)

A_trnsp = A.transpose()
print("A transpose:", A_trnsp)

Ainv = np.linalg.inv(A)

print("Ainv:", Ainv)

A_mult_Ainv = np.matmul(Ainv,A)
print("A_mult_Ainv:", A_mult_Ainv)

I = np.identity(3)

print("identity matrix:", I)

