import numpy as np
#定义num,num1
num = np.array([1,2,3,4,5],float)
num1 = np.array([6,7,8,9,10],float)
#数组索引
print(num[2])
#数组切片
print(num[1:])
print(num[:-1])
#检查成员
print(3 in num)
print(8 in num)
#查询长度
print(np.size(num))
print(len(num))
print(np.size([[1,2],[1,3]]))
print(len([[1,2],[1]]))
#查询数组形状
print(np.shape([[1,2],[1,3]]))
#查询最大最小值
print(num.max(),num.min())