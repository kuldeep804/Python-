import numpy as np 

array=np.array([1, 2, 3,4])
print("Original Array:")
print(array)
print(type(array))

#doubling the array
doubled_array = array * 2
print("Doubled Array:")
print(doubled_array)

#dimensions of array 
new=np.array([[1, 2, 3], [4, 5, 6]])
print("Dimensions of new :")
print(new.ndim)
print("Shape of new:")
print(new.shape)
