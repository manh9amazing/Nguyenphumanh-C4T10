n = str(input("dap an cua ban la"))
loop_count = 0 
while loop_count<1:

    if  n=="1":
        loop_count += 1
    elif n=="2":
        loop_count += 1
    elif n=="3":
        loop_count += 1
    elif n=="4":
        loop_count += 1
    else:
        print("the answer must be 1,2,3 or 4 ")
        n = str(input("enter again :"))
if n in ["1" or "2" or "4"]:
    print("wrong the answer must be 3:4 legs")
else:
    print("you are right")