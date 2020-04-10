mydic = {}
n=int(input())
b=[]

for i in range(0,n):
    a1,b1,c1,d1=input().split()
    b.append(float(b1))
    b.append(float(c1))
    b.append(float(d1))
    temp=b.copy()
    mydic[a1] = temp
    b.clear()



name = input()
numbers = mydic.get(name)

ans = float((numbers[0] + numbers[1] + numbers[2])/3)
final = str(ans)

if len(final)==5:
    print(ans)
elif len(final)>5:
    print(round(ans,2))
else:
    print(f"{ans}0")



