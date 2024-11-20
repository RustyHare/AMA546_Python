import array as arr
import numpy as np
a1=np.array([1,2,3,4,5],float)#通过numpy定义数组，第一个位置放数组元素，第二个位置放元素类型，此处类型定义为浮点数float
a=arr.array('d',[1,2,3,4,5])#通过array定义数组，第一个位置放元素类型，第二个位置放数组元素
print(a,a1)
print(type(a),type(a1))

#答案是：
#array('d', [1.0, 2.0, 3.0, 4.0, 5.0]) [1. 2. 3. 4. 5.]
#<class 'array.array'> <class 'numpy.ndarray'>