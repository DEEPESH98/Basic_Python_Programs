a=['A', 'app','a', 'd', 'ke', 'th', 'doc', 'awa']
b=['y','tor','e','eps','ay',None,'le','n']
b.reverse()
c=[]
d=[]

for i in range(0,len(a)):
    if(a[i]==None):
        d=b[i]
        c.append(d)
    elif(b[i]==None):
        d=a[i]
        c.append(d)
    else:
        d=a[i]+b[i]
        c.append(d)

print('"',end="")
for i in range(0,len(c)):
    print(c[i],end=" ")
print('"',end="")
