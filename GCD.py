def gcd(d):
    if d[0] > d[1]:
        smaller = d[1]
    else:
        smaller = d[0]
    for i in range(1, smaller+1):
        if((d[0] % i == 0) and (d[1] % i == 0)):
            hcf = i

    return hcf

b =[]
c =[]

for i in range(0,2):
    x=int(input())
    b.append(x)
    
for i in range(0,2):
    x=int(input())
    c.append(x)

gcd1=gcd(b)
gcd2=gcd(c)

print(gcd1)
print(gcd2)



