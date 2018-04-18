print ("Hallo, ich bin ein Computer.")
name = input("Wie ist dein Name? ")
print ("Schön dich zu treffen ", name, ".", sep="")
print ("Dein Name ist ", len(name), "Zeichen lang.")
alter = input("Wie alt bist du? ")
alter = int(alter)
if (alter > 100):
    print ("Das ist wohl ein Scherz - oder? ;-)")
    print("test")
else:
    print ("Nächstes Jahr wirst du", alter+1, "Jahre alt sein.")
print ("tschüsss...")

