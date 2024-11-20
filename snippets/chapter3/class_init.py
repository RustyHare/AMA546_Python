class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
        
# 最佳实践：在函数定义，类定义后面加一个空行。
x = Complex(3.0, -4.5)
print(x.r, x.i)