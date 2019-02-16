n = input("Enter a string : ")
loop_count= 0
while loop_count<1:
    count = 0
    for c in n :
        if c.isspace() != True:
            count = count + 1
    if (count<=8) or (n.isdigit()==True) or (n.isupper()==True) or (n.islower()== True) or (n.isalpha()==True):
        n = input("lam on hay nhap lai ")
    else:
        print("xin cam on")
        loop_count+=1
