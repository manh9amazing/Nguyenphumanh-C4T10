n=[
{'Name:':'Huy',
'Role':'Waiter',
'Hours':12,
'Salary per Hour($)':0.8},
{'Name:':'Tung',
'Role':'Cook',
'Hours':24,
'Salary per Hour($)':1.5},
{'Name:':'M.Duc',
'Role':'Manager',
'Hours':20,
'Salary per Hour($)':2},
]
print("-----------------------------------------------")
print("bang luong nhan vien")
for a in n:
    print(a)
b={
    'Name':'Don',
    'Role':'Waiter',
    'Hours':12,
    'Salary per Hour($)':0.9
}
c={
    'Name':'H.Duc',
    'Role':'Waiter',
    'Hours':14,
    'Salary per Hour($)':0.7,
}
n.append(b)
n.append(c)
print("-----------------------------------------------")
print('bang thong tin moi sau khi them thong tin la-')
for a in n:
    print(a)
print("-----------------------------------------------")
print('thong tin hang thu 3 cua bang luong ')
print(n[2])
n[0]={
    'Name':'Huyen',
    'Role':'Waitress',
    'Hours':14,
    'Salary per Hour($)':1,
}
print("-----------------------------------------------")
print('bang thong tin sau khi thay the la')
for a in n:
    print(a)
n.pop(len(n)-1)
print("-----------------------------------------------")
print('bang thong tin sau khi xoa phan tu cuoi la')
for a in n:
    print(a)
print("-----------------------------------------------")
print('gia su 1 thang nhan vien lam viec 4 tuan\nvay nen 1 nam nhan vien lam viec 48 tuan khong tinh nghi le')
k=0
for i in range(len(n)):
    x=n[i]['Hours']*n[i]['Salary per Hour($)']*4
    y=12*x
    n[i]['Salary per Month']=x
    n[i]['Salary per Year']=y
    k=k+y
print('bang thong tin co thong tin moi ve luong la')
for a in n:
    print(a)
print("-----------------------------------------------")
print('tong so tien can tra trong 1 nam la($): ',k)

