'''

Find number of factors for a given integer N.

Input:
The first line of input contains an integer, the number of testcases T. Each testcase should contain a positive integer N.

Output:
In each separate line print the number of factors (including 1 and the number itself).

Constraints:
1 <= T <= 30
1 <= N <= 100

Example:
Input:
1
5

Output:
2

Explanation:
Testcase 1: Factors of 5 are: 1 and 5.
'''

a=int(input())

b=[]
d=[]


for i in range(0,a):
    x=int(input())
    b.append(x)
    
for i in range(0,a):
    c=1
    for j in range(1,b[i]):
        if (b[i])>=j:
            if b[i]%j==0:
                c=c+1
    d.append(c)
    
for i in range(0,a):
    print(d[i])
