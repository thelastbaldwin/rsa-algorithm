import math

def isPrime(number):
    if number < 1:
        return False
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True

def getLargest(list):
    return list[-1]

# returns true if greatest common divisor is 1
def areCoprime(a, b):
    return math.gcd(a, b) == 1

# used for e value
def getCoprimes(max):
    primes = []
    for i in range(2, max):
        if areCoprime(i, max):
            primes.append(i)
    return primes

# count of coprimes between known factors
def phi(p, q):
    return (p - 1) * (q - 1)

# mod value used for both keys
def getMod(p, q):
    return p * q

# return list of all potential d values up to max
def getDValues(e, totient, max):
    dees = []
    for i in range(2, max):
        if areValidConstants(i,e, totient):
            dees.append(i)
    return dees

def areValidConstants(e, d, totient):
    return (d * e) % totient == 1

def encryptRSA(val, e, mod):
    return (val ** e) % mod

def decryptRSA(val, d, mod):
    return (val ** d) % mod

def encryptMessage(message, e, mod):
    encryptedMessage = []

    for m in message:
        encryptedMessage.append(encryptRSA(ord(m), e, mod))

    return encryptedMessage

def decryptMessage(message, d, mod):
    decryptedMessage = []

    for m in message:
        decryptedMessage.append(chr(decryptRSA(m, d, mod)))

    return "".join(decryptedMessage)

def getPrimeInput(name):
    p = None

    while p is None or isPrime(p) != True:
        p = int(input("Enter a prime number for {}: ".format(name)))
        if isPrime(p) != True:
            print("{} is not prime".format(p))
    return p

def outputValue(name, value):
    print("{} = {}".format(name, value))

def bar(length):
    return("*" * length)

lineLength = 30
print(bar(lineLength))
print("RSA Encryption Demo:")
print(bar(lineLength))

# while this works with smaller numbers it's best if these are > 11
p = getPrimeInput("p")
q = getPrimeInput("q")

mod = getMod(p, q)
totient = phi(p, q)
e = getLargest(getCoprimes(totient))
d = getLargest(getDValues(e, totient, e * 200))

print(bar(lineLength))
print("Values for this example:")
outputValue("p", p)
outputValue("q", q)
outputValue("mod", mod)
outputValue("totient", totient)
outputValue("e (largest)", e)
outputValue("d (largest)", d)
print(bar(lineLength))

message = input("Enter your message to be encrypted: ")
secretMessage = encryptMessage(message, e, mod)
decryptedMessage = decryptMessage(secretMessage, d, mod)
print("Original Message: {}".format(message))
print("Secret Message: {}".format(secretMessage))
print("Decrypted Message: {}".format(decryptedMessage))