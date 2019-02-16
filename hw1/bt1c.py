a = float(input("so a la "))
b = float(input("so b la "))
c = float(input("so c la "))
if a == 0:
    if b == 0:
        if c == 0:
            print("phuong trinh vo so nghiem")
        else:
            print("phuong trinh vo nghiem")
    else:
        x = -c/b
        print("phuong trinh co 1 ngiem  la", x)
else:
    d = b*b-4*a*c
    if d < 0:
        print("phuong trinh vo nghiem")
    elif d == 0:
        print("phuong trinh co nghiem kep la ", -b/(2*a))
    else:
        x1 = (-b+d**(1/2))/(2*a)
        x2 = (-b-d**(1/2))/(2*a)
        print("phuong trinh co 2 ngiem")
        print("phuong trinh co nghiem thu 1 la ", x1)
        print("phuong trinh co nghiem thu 2 la ", x2)
