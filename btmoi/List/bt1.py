from random import*
items=["Sports","LOL","BTS"]
x=str(input("1 thu ban thich : "))
items.append(x)
print(*items,sep="|")
for i in range (3):
    print(items[i].upper())
y=str(input("1 bo phim ban thich : "))
z=str(input("1 bo truyen ban thich : "))
t=str(input("sua 1 phan tu bat ky : "))
items[0]=y
items[3]=z
items[randint(0,3)]
items.pop(1)
if "LOL" not in items:
    print("da xay ra loi")
else:
    items.remove("LOL")
a=int(input("nhap vi tri can xoa : "))
items.pop(a-1)
print("list moi la",items)
b=str(input("nhap tu can xoa : "))
items.remove(b)
print("list moi la",items)
