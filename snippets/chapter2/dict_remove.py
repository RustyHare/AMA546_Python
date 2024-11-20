#字典Key的删除(字典元素删除)
dic1={"Key1":1,"Key2":"123"}
del dic1["Key2"]
print(dic1)
#结果1：
# {'Key1': 1}

#字典内容清空
dic1={"Key1":1,"Key2":"123"}
dic1.clear()
print(dic1)
#结果2：
# {}

#字典完全删除
dic1={"Key1":1,"Key2":"123"}
del dic1
print(dic1)
#结果3：应该会得到一个错误。