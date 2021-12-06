import random

n = 15
N = 1000000

strs = []
for i in range(N):
    print(i)
    s = ''
    for j in range(random.randint(6, n)):
        letter = random.randint(65, 123)
        s += str(chr(letter))
    strs.append(s)


f = open("small_input.txt", "a")
f.write("\n".join(strs))

def gcd(a,b):
    if (a < b):
        return gcd(b, a)
    if (a % b == 0):
        return b
    return gcd(b, a % b)

@staticmethod
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

find_carmichael_numbers(start, end)  
    
