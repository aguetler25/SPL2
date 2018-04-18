# regen.py
regnetEs = input("Regnet es? ")
if (regnetEs == "ja"):
    regen = True
    regenschirm = input("Hast du einen Regenschirm? ")
    if (regenschirm == "nein"):
        while (regen):
            print("warten bis der Regen aufhört...")
            eingabe = input("Regnet es noch? (ja/nein) ")
            if (eingabe == "nein"):
                regen = False
                print("es hat aufgehört zu regnen...")
            elif (eingabe == "ja"):
                print("es regnet noch immer...")
            else:
                print("bitte nur ja oder nein eingeben")
print("Geh nach draussen.")