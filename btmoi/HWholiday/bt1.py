
b=str(input("mat khau"))
d=str(input("nhap lai mat khau"))
loop_count= 0
while loop_count<1:
    if b != d or len(b)<8 or b.isdigit()==True or b.isalpha()==True  :
        print("loi da xay ra")
        b=str(input("mat khau"))
        d=str(input("nhap lai mat khau"))
    else:
        print("welcome")
        loop_count+=1
    
