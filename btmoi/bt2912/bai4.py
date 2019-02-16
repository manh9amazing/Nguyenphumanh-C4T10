n=int(input("nhap canh"))
from turtle import*

shape("turtle")
color("red")

for i in range (n+1):
    left(180-180*(n-2)/n)
    forward(100)
mainloop()