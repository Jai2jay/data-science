import numpy as n
# a = n.array([1,2,3])
# print(a)

# print(n.zeros((3,3)))
# print(n.ones((2,2)))


a=n.arange(0,11,2)
print("original:",a)

b = a.reshape((2,3))
print("reshaped:\n",b)