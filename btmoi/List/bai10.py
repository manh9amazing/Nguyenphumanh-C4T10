a = [int(x) for x in input("nhap cac so").split(',')]
b=[]
print(a)
print("cac so chan la")
for y in a:
    if y % 2 ==0:
        b.append(y)
print(b)

