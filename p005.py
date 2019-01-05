def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n

        m = old_n
        n = old_m % old_n
    return n

def lcm(m, n):
    lcm = (m*n)//gcd(m,n)
    return lcm

def smallestMultiple(num):    
    j = 2
    for i in range(3, num+1):
        j = lcm(j,i)
    return j
    
print(smallestMultiple(20))
