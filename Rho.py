import random, cryptomath, time,sys
from euclid import gcd
def Rho(n):    
    if(n==1): return n
    if(n%2 == 0): return 2
    x= random.randint(2, n)
    y=x
    c=random.randint(1,n-1)
    d=1
    while(d==1):
        x=(x**2+c)%n
        y=(y**2+c)%n
        y=(y**2+c)%n
        d=gcd(abs(x-y),n)
        if(d==n): return Rho(n)
    return d
print("Insert n")
n=int(input())
start=time.time()
p=Rho(n)
end=time.time()
print("p = ", p)
q=int(n/p)
print("q = ", q)
print("Time: ", end-start)
print("Insert the public exponent")
e= int(input())
d = cryptomath.findModInverse(e, (p - 1) * (q - 1))
print("d= ",d )




