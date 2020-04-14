n = int(input())
for i in range(0,n):
    a = int(input())
    a1 = list(map(int,input().rsplit()))
    a2 = set(a1)
    b = int(input())
    b1 = list(map(int, input().rsplit()))
    b2 = set(b1)
    print(a2.issubset(b2))
