
'''You are given a cubic dice with 6 faces. All the individual faces have a number printed on them. The numbers are in the range of 1 to 6, like any ordinary dice. You will be provided with a face of this cube, your task is to guess the number on the opposite face of the cube.

Input:
The first line of the input contains a single integer T, denoting the number of testcases. Then T test case follows, a single line of the input containing a positive integer N.

Output:
For each testcase, print the number that is on the opposite side of the given face.

Constraints:
1 <= T <= 100
1 <= N <= 6

Example:
Input:
2
6
2

Output:
1
5

Explanation:
Testcase 1: For dice facing number 6 opposite face will have the number 1.

** For More Input/Output Examples Use 'Expected Output' option **
'''

a=int(input())

b =[]
c =[]

for i in range(0,a):
    x=int(input())
    b.append(x)

for i in range(0,a):
    if(b[i]==1):
       c.append(6)
    elif(b[i]==2):
       c.append(5)
    elif(b[i]==3):
       c.append(4)
    elif(b[i]==4):
       c.append(3)
    elif(b[i]==5):
       c.append(2)
    elif(b[i]==6):
       c.append(1)
        
for i in range(0,a):
    print(c[i])

