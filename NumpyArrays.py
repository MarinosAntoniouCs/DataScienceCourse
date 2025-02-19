import numpy as np

l=[2,3,4,5] #A list
print(l)
print(type(l))
print()
arr=np.array(l) #Converting a list to a np array
print(arr)
print(type(arr))

a=np.array([1,2,3,4]) #np array has dimensions
b=np.array([[1,2,3,4],[5,6,7,8]])
print(a.ndim)
print(b.ndim)
print(b.shape) #Will give you the rows and then the collumns

# Python Program illustrating
# np.zeros method
 
b = np.zeros(2, dtype = int) #One dimension of two columns
print("Matrix b : \n", b)
 
a = np.zeros([2, 2], dtype = int) #Two dimensions of two columns
print("\nMatrix a : \n", a)
 
c = np.ones([3, 3]) #Three dimensions with three columns
print("\nMatrix c : \n", c)

# output array
out_arr = np.random.random(3) #np.random.random(columns) to give a one dimension array of #columns random columns
print ("Output 1D Array filled with random floats : ", out_arr)

print("A\n", np.arange(4).reshape(2, 2), "\n") #arange is like the range one , with the reshape you adjust rows/columns
print("A\n", np.arange(4, 10), "\n")
print("A\n", np.arange(4, 20, 3), "\n")#Third argument is for steps

print("B\n", np.linspace(2.0, 3.0, num=5, retstep=True), "\n") #Start and end given , also number of items. by having retstep True you print step size
 
# To evaluate sin() in long range
x = np.linspace(0, 2, 10)
print("A\n", np.sin(x))

maxC = np.max(c)
print(maxC)

minB = np.min(b)
print(minB)

# creating a two dimensional
# np array of integers
arr = np.array([[11, 2, 3],
                     [4, 5, 16],
                      [7, 81, 22]])
 
# finding the maximum and
# minimum element in the array
max_element_column = np.max(arr, 0) #with 0 we speak about columns
max_element_row = np.max(arr, 1)
 
min_element_column = np.amin(arr, 0) #with 1 we speak about rows
min_element_row = np.amin(arr, 1)
 
# printing the result
print('maximum elements in the columns of the array is:',
      max_element_column)
 
print('maximum elements in the rows of the array is:',
      max_element_row)
 
print('minimum elements in the columns of the array is:',
      min_element_column)
 
print('minimum elements in the rows of the array is:',
      min_element_row)