#计算字典长度(元素个数)
dic1={"Key1":1,"Key2":"123"}
print(len(dic1))

#以字符串的格式输出字典元素
dic1={"Key1":1,"Key2":"123"}
print(str(dic1))

#复制字典，进行浅拷贝
dic1={"Key1":1,"Key2":"123"}
dic2=dic1.copy()
print(dic2)

#判断某个Key是否在目标字典里
dic1={"Key1":1,"Key2":"123"}
print("Key1" in dic1)

#输出字典中所有的Key和所有的键值对元素
dic1={"Key1":1,"Key2":"123"}
print(dic1.keys())
print(dic1.items())