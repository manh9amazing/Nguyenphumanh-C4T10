from random import*
n ={
    "name":"sherlock",
    "description":"action",
    "episode":23

}
b=[]
x=str(input("nhap key"))
y=input("nhap value")
n[x]=y
print(n)
print(n["name"])
print(n["description"])
z=str(input("thong tin can biet"))
print(n[z])
l=str(input("key muon duoc them"))
k=str(input("thong tin them"))
n[l]=n[l],k
print(n)
for key in n.keys():
    b.append(key)
c=choice(b)
del n[c]
print("dictionary moi la")
print(n)
d=input("key ban muon xoa")
print("dictionary moi la")
del n[d]
print(n)

    