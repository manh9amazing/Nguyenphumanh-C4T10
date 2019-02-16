a=str(input("hay nhap email cua ban"))
b=str(input("hay nhap lai email cua ban"))
c=str(input("hay nhap ten dang nhap cua ban"))
d=str(input("hay nhap password cua ban"))
loop_count=0
while a!=b:
    print("email ko giong nhau")
    a=str(input("hay nhap email cua ban"))
    b=str(input("hay nhap lai email cua ban"))
while True:
    if "@" not in  a or "." not in a:
        print("email ko hop le")
        a=str(input("hay nhap email cua ban"))
        b=str(input("hay nhap lai email cua ban"))
    else: 
        break
loop_count=0
while loop_count<1:
    if len(d)<8 or d.isdigit()==True or d.isalpha()==True:
        print("mat khau ko hop le")
        d=str(input(" nhap lai password cua ban"))
    else:
        print("welcome")
        loop_count+=1
        

    
