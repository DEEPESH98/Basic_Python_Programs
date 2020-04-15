# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
import math

c=complex(input())


p = c.real**2 + c.imag**2
print(math.sqrt(p))
print(cmath.phase(complex(c.real,c.imag)))


