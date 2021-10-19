import numpy as np
from icecream import ic

# convert to numpy array
mylist = [1,2,3,4,5]
ic(np.array(mylist))

# create a range list
ic(np.arange(0,10))

# create a range list with frequency
ic(np.arange(0,10,2))

# 2d array
ic(np.zeros((5,5)))

# random arrays
ic(np.random.randint(0,100))

# matrix of random integers
ic(np.random.randint(0,100,(5,5)))

# linearly spaced array
ic(np.linspace(0,10,6))
ic(np.linspace(0,10,30))

# setting random seed
np.random.seed(101)
ic(np.random.randint(0,100,10))

# max, mix
arr = np.random.randint(0,100,10)
ic(arr)
ic(arr.max())
ic(arr.min())
ic(arr.mean())
ic(arr.argmax()) # max value's index
ic(arr.argmin())

# reshape array
ic(arr.reshape(2,5))
reshaped_2d_arr = (np.arange(0,100).reshape(10,10))
ic(reshaped_2d_arr)
ic(reshaped_2d_arr[5,2]) # select value based on row,column

# conditional filter/mask
ic(reshaped_2d_arr[reshaped_2d_arr>50])