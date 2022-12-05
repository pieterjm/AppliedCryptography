import math
import random # Why????

# returns true if a number (p) is a prime
def isPrime(p):
    if p in [ 1, 2 ]: return True
    for d in range(2, int(math.ceil(math.sqrt(p))+1)):
        if p % d == 0: return False

    return True

# genereer een priemgetal van lengte n bits
def genPrime(n):
    while True:
        p = random.randint((2**(n-1)), (2**n)-1)
        if isPrime(p): return p
    return # Not reached

# generate random number between start and stop
def genRandom(start, stop):
    return random.randint(start,stop)

# Two integers are co-prime if the only common divisor is 1
# Berekend of p en q co-prime zijn (de grootste divisor is 1)
def isCoPrime(p, q):
    return math.gcd(p, q) == 1

def genSecret(p, n):
    while True:
        g = genPrime(n)
        if g < p:
            return g    

nbits = 32

# Kies grondgetal p, 
shared_p = genPrime(nbits)

# Grondgetal g, moet co-prime zijn met p?
# Als p is prime dan is het zowieso 1
# which is a primitive root modulo p
shared_g = genSecret(shared_p,nbits)

# Alice kiest random getal kleiner dan p
alice_a = genRandom(1,shared_p)

# berekenen g^a mod p
shared_A = pow(shared_g,alice_a,shared_p)

# bob kiest een random getal kleiner dan p: b
bob_b = genRandom(1,shared_p)

# bob berekent g^b mod p
shared_B = pow(shared_g,bob_b,shared_p)

# alice berekent B^a mod p
alice_sa = pow(shared_B,alice_a,shared_p)
print(alice_sa)

# bob doet hetzelfde met zijn secret
bob_sb = pow(shared_A,bob_b,shared_p)
print(bob_sb)
print(alice_sa == bob_sb)
