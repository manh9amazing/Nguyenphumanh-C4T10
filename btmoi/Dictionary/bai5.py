from random import*
a=['an octopus', 'a cat','a dog', 'a human', 'an unicycle']
b=['1 leg', '2 legs', '4 legs', '8 legs']
points=0
for i in range (5):
    h=[]
    print('Question',i+1,':')   
    d=randint(0,3)
    c=choice(a)
    print("how many legs",c,'have')
    for j in range (4):
        l=b[d-j]
        print(j+1,".",l)
        h.append(l)
    k=int(input("what is your answer?"))
    if c=='an octopus':
        if str(h[k-1])=="8 legs":
            print("true") 
            points+=1
        else:
            print("false")
    if c=='a cat':
        if str(h[k-1])=="4 legs":
            print("true") 
            points+=1
        else:
            print("false")
    if c=='a dog':
        if str(h[k-1])=="4 legs":
            print("true") 
            points+=1
        else:
            print("false")
    if c=='a human':
        if str(h[k-1])=="2 legs":
            print("true") 
            points+=1
        else:
            print("false")
    if c=='an unicycle':
        if str(h[k-1])=="1 leg":
            print("true") 
            points+=1
        else:
            print("false")
print('ban da tra loi dung',points,'cau, ti le dung la',points/5*100,'phan tram')

