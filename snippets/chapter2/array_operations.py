import numpy as np
#定义num,num1
num = np.array([1,2,3,4,5],float)
num1 = np.array([6,7,8,9,10],float)
#数组相加
print(num+num1)
#数组相乘
print(num*num1)
print(num*4)
print(np.dot(num,num1))
print(np.dot([[1,2],[3,4]],[[1,2],[3,4]]))
