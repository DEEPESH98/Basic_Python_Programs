
a = int(input())
list1 = list(map(int,input().split()))
myset = set(list1)
b = int(input())
list2 = list(map(int,input().split()))
myset2 = set(list2)

final1 = myset.symmetric_difference(myset2)
final=list(final1)
final.sort()
for i in range(0,len(final)):
    print(final[i])
