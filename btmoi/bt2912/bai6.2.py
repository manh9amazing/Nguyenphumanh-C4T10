
d=str(input("hay nhap password cua ban"))
while True :
    if len(d)<8 or d.isdigit()==True or d.isalpha()==True:
        print("mat khau ko hop le")
        d=str(input(" nhap lai password cua ban"))
    else:
        break
