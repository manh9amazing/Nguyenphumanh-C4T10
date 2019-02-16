x=['xyz','dwd']
n=str(input('nhap cac thu ban thich '))
y=n.split(',')
print(y)
x.extend(y)
len(x)
for i in range(len(x)) :
    print(x[i])
