import numpy as np

if __name__=="__main__":
    a=str(input("输入第一个数字："))
    b=str(input("输入第二个数字："))
    max_len=max(len(a),len(b))
    A,B,C=list(),list(),list()
    for i in range(len(a)-1,-1,-1):
        A.append(int(a[i]))
    for i in range(len(b)-1,-1,-1):
        B.append(int(b[i]))
    for i in range(max_len):
        t=A[i]+B[i]
        C.append(t%10)
        t//=10
    Z=""
    for i in range(len(C)-1,-1,-1):
       Z+=str(C[i])
    print(Z)