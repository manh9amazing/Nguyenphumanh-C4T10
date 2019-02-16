n=[{"name":"xxx"},
{"year": "kkk"},
{"main":["aaa","bbb","ccc"]},]
for i in range(2):
    for k,v in n[i].items():
        print(k,"-",v)
    for k in n[i].keys():
        print (k)
for k,v in n[2].items():
    print(k,"-",end="")
    print(*v,sep=",")



