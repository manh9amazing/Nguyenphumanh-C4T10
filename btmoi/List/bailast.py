
a = [int(x) for x in input("nhap cac so diem cua cac ban").split(',')]
print("high score")
a.sort(reverse=True)
if len(a)<5:
    for i in range(5-len(a)):
        a.append(0)
for i in range(5):
    print(i+1,".",a[i])
z= str(input("do you want to add new score?"))
if z=="yes":   
    x = int(input("your new score"))
    a.append(x)
    print("new top score")
    a.sort(reverse=True)
    for i in range(5):
        print(i+1,".",a[i])

    
