# zahlenreihe.py

n = input("Bitte n eingeben: ")
n = int(n)
# n = 1000

for i in range(1, n+1):
    if (i < n):
        print(i, end=" < ")
    else:
        print(i)

# alle geraden Zahlen von 1..n ausgeben
print("")
for i in range(1, n+1):
    if (i % 2 == 0):
        print(i, end=" ")

# alle ungeraden Zahlen von 1..n ausgeben
print("")
for i in range(1, n+1):
    if (i % 2 != 0):
        print(i, end=" ")

# alle Zahlen von 1..n ausgeben, die durch 9 teilbar sind
print("")
for i in range(1, n+1):
    if (i % 9 == 0):
        print(i, end=" ")
