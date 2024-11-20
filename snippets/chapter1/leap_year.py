if __name__=="__main__":
    x=int(input("输入年份："))
    if x%4==0 and x%100!=0:
        print("YES")
    elif x%400==0:
        print("YES")
    else:
        print("NO")