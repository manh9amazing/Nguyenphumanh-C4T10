x="xxx"
n= str(input("password"))
loop_count=0
while loop_count<1:
    for i in range(10):
        if str(i) in n:
            x="ok"
            print(x)
            break
    if x == "ok":
        loop_count +=1
    if x != "ok":
        n= str(input("try again"))
        loop_count = 0
            
      

        