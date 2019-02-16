n= {
   'raichu':'raichu has a regional variant that is Electric/Psychic. It evolves from Pikachu when exposed to a Thunder Stone. All Pikachu in Alola will evolve into this form regardless of their origin.',
   'onix': 'Onix resembles a giant chain of gray boulders that become smaller towards the tail. It has a rocky spine on its head and a pair of black eyes right beneath it. This Pokémon has a magnet in its brain that serves as an internal compass. Its body absorbs many hard objects, making its body very solid. As it grows older, it becomes more rounded and smoother, eventually becoming similar to black diamonds.'

}
b=[]
h=[]
for key in n.keys():
        h.append(key)
print('pokedex-ver1.0')
w=input("Does this dictionary have? ")
if w.lower() in h:
    print("yes")
else:
    print("no")
a=str(input('do you want to see the whole dictionary?\n Input Yes No'))
if a=='yes':
    for key in n.keys():
        b.append(key)
    for i in range(len(b)):
        print(b[i],":",end=" ")
        c=n[b[i]]
        d=c.split(' ')
        len(d)
        for i in range(len(d)):
            if (i+1) %20 ==0:
                print(d[i],end='\n')
            else:
                print(d[i],end=" ")
        print("")
count=0
while count<1:
    p=str(input('Enter the pokemon name: '))
    l=n[p.lower()]
    z=l.split(' ')
    len(z)
    for i in range(len(z)):
        if (i+1) %20 ==0:
            print(z[i],end='\n')
        else:
            print(z[i],end=" ")
    print("")
    q=input("Do you want to search more:\n Press Yes No ")
    if q.lower()=="yes":
        count=0
    if q.lower()=="no":
        count+=1
print("Thank you for using our service")



