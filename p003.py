def largestprime(num):
    
    prime = list()
    
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            k = True
            for j in range(2, int(i**0.5)+1):
                if i%j == 0:
                    k = False
                    break
            if k == True:
                prime.append(i)
            
    return prime[-1]
    

print(largestprime(600851475143))

#Solution 1
#number = 600851475143
#div = 2

#while True:
#    if number % div == 0 and number // div != 1:
#        number //= div
#    div += 1
#    if number < div:
#        break
#
#print(number)

#Solution 2
#N = 600851475143
#n = 2
#while n < N//2:
#    q, r = divmod(N, n)
#    if r: n += 1
#    else: N = q
#print(N)
