import random

f = open("small_input.txt", "r")
interval = f.readline().split(" ")
start = int(interval[0])
end = int(interval[1])

def gcd(a,b):
    if (a < b):
        return gcd(b, a)
    if (a % b == 0):
        return b
    return gcd(b, a % b)

def is_prime(n):
    if n <= 2:
        return n == 2

    if n % 2 == 0:
        return False

    for divisor in range(3, int(n ** 0.5) + 1, 2):
        if n % divisor == 0:
            return False

    return True

def is_Carmichael(n):
    if n <= 2 or n % 2 == 0 or is_prime(n):
        return False

    for a in range(3, n, 2):
        if gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False

    return True

      
def find_carmichael_numbers(start, end):
    res = []
    for n in range(start, end):
        if is_Carmichael(n):
            res.append(n)

    return res

res = find_carmichael_numbers(start, end)
print(res)  
    
