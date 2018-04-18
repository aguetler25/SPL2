# unterprogramme.py

def isPrime(zahl):
    if (zahl <= 1):
        return False
    for i in range (2, zahl):
        if (zahl % i == 0):
            return False
    return True

print ("Primzahlen von 1 bis 1000 berechnen")
for i in range(1, 1001):
    if (isPrime(i)):
        print(i, end=" ")

