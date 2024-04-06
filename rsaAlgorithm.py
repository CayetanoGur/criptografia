import random
import math

'''
How does it works?

1) You have to pick two prime numbers (p and q)
2) N = p * q
3) phi_n = (p-1) * (q-1)
4) Choose e ->  1 < e < phi_n
                coprime with N, phi_n
    Here you get the public key (e,N)
5) Choose d -> d*e(mod phi_n) = 1  
    Here you get the private key (d,N)

'''


def is_prime(number):
    if number <2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True

def generate_prime(min, max):
    prime = random.randint(min,max)
    while not is_prime(prime):
        prime = random.randint(min,max)
    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    raise ValueError("mod inverse no existe")

p = generate_prime(1000, 5000)
q = generate_prime(1000, 5000)
#1
while p == q:
    q = generate_prime(1000, 5000)
#2
n = p * q
#3
phi_n = (p-1) * (q-1)
#4
e = random.randint(3, phi_n-1)
#Busco un randome entre e y phi que sea coprimo. math.gcd -> gratest common denominator. 
while math.gcd(e, phi_n) != 1:
    e = random.randint(3, phi_n-1)
#5
d = mod_inverse(e, phi_n)
#DONE ---------------------

print("Public key: ", e)
print("Privare key: ", d)
print("n: ", n)
print("Phi of n: ", phi_n)
print("p ", p)
print("q ", q)

message = input()

#ord() built in function that accepts a string containing a single Unicode character and returns an integer representing the Unicode point of that character
#transfor message into ascii (encoding)
message_encoded = [ord(c) for c in message]
# (m ^ e) mod n = c -> asi se encripta
# pow(c,e,n) == (c^e)mod n
ciphertext = [pow(c, e, n) for c in message_encoded]

print("ciphertext: ", ciphertext)
#Decripted with the private key d
message_encoded = [pow(c, d, n) for c in ciphertext]
message = "".join(chr(c) for c in message_encoded)

print(message)
