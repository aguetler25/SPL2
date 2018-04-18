def berechnen(zahl):
    zahl = zahl**2
    zahl = zahl**3
    zahl = zahl+17**23
    return zahl

zahl = input("Bitte eine Zahl eingeben: ")
zahl = int(zahl)
print(berechnen(zahl))