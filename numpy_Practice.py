
import numpy  as np

arr = np.arange(0,11)

print(np.ones(10)*5)

print(np.arange(10,50))

#get even number 
print(np.arange(10,50,2))

#create matrix 3*3 value from 0 to 8
print(np.arange(9).reshape(3,3))

#identity matrix
print(np.eye(3))


#generate randowm
print(np.random.rand(1))

mat = np.arange(1,26).reshape(5,5)

print(mat[:3,2].reshape(3,1))

