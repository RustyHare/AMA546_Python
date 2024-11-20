a = list(map(int, list(input("输入a："))))[::-1]
b = int(input("输入b:"))

t = 0   # 进位
c = []
for i in range(len(a)):
    t += a[i] * b
    c.append(t % 10)
    t //= 10

while t:  # 可能有多的进位
    c.append(t % 10)
    t //= 10

while len(c) > 1 and c[-1] == 0:  # 可能存在前导0
    c.pop()

print(''.join(map(str, c[::-1])))