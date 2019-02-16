from random import*
point=0
while True:
    x=randint(1,10)
    y=randint(1,10)
    n=x+y
    lis=[n-1,n,n+1]
    f=choice(lis)
    print(x,"+",y,"=",f)
    w=str(input("True or False?"))
    # quy uoc 1 la True ; 2 la False
    if w=="1":
        if f==n:
            point+=1
        else:
            break
    if w=="2":
        if f!=n:
            point+=1
        else:
            break
print("game over")
print("diem cua ban la",point)