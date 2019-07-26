'''
Given a string S, check if it is palindrome or not.

Input:
The first line contains 'T' denoting the number of test cases. T testcases follow. Each testcase contains two lines of input. The first line contains the length of the string and the second line contains the string S.

Output:
For each testcase, in a new line, print "Yes" if it is a palindrome else "No". (Without the double quotes)

Constraints:
1 <= T <= 30
1 <= N <= 100

Example:
Input:
1
4
abba
Output:
Yes
'''
def reverse(b): 
  str = "" 
  for i in b: 
    str = i + str
    
  return str

a=int(input())

b=[]
c=[]

for i in range(0,a):
    d=int(input())
    x=input()
    b.append(x)
    c.append(reverse(x))

for i in range(0,a):
    if c[i]==b[i]:
        print('Yes')
    else:
        print('No')



