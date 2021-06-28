
sum =0
for i in range(1,1000):
    if i%3 == 0 or i%5==0:
        sum +=i

print(sum)

# best approach
def sumn(n, d):  # Sum natural numbers ≤ n that are divisible by d
    n //= d
    return d*n*(n+1) // 2
L = int(input('Enter an upper bound? '))
a, b = 3, 5
s = sumn(L-1, a) + sumn(L-1, b) - sumn(L-1, a*b)
print ("Sum of multiples of", a, "or", b, "below", L, "=", s)