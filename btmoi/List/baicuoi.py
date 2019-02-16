x=['ST','BĐ','BTL','CG','ĐĐ','HBT']
y=[117.43,9.224,43.35,12.04,9.96,10.09]
z=[150300,247100,333300,266800,420900,318000]
d=[]
max=z[0]
b=0
for i in range (6):    
    if z[i]>max:
        max=z[i]
        b=i+1
if b==0:
    b=1
print("quan co so dan nhieu nhat la",x[b-1],"so thu tu la",b)
min=z[0]
c=0
for j in range (6):    
    if z[j]<min:
        min=z[j]
        c=j+1
if c==0 :
    c=1
print("quan co so dan it nhat la",x[c-1],"so thu tu la",c)
for p in range(6):
    k=z[p]/y[p]
    d.append(k)
print("mat do dan so lan luot la",d)
h=sum(d)/len(x)
print("mat do dan cu trung binh",h)
