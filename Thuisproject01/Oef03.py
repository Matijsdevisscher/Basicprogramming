# Oef 3: Schrijf een functie ‘controleer_paswoord’ met één string-parameter die een kandidaatpaswoord
# voorstelt. Deze functie controleert of het paswoord aan volgende voorwaarden
# voldoet:
# 1. Minimum één letter tussen [a-z]
# 2. Minimum één cijfer tussen [0-9]
# 3. Minimum één letter tussen [A-Z]
# 4. Minimum één karakter uit [$#@]
# 5. Minimum lengte van 6 karakters
# 6. Maximum lengte van 12 karakters
# Test de functie meermaals uit.



import re

password = input("Geef je paswoord op: ")
x = True

def controleer_paswoord(password):
    while x:
        if(len(password) >5 and len(password) <13):
            break
        elif not re.search("[a-z]", password):
            break
        elif not re.search("[0-9]", password):
            break
        elif not re.search("[A-Z]", password):
            break
        elif not re.search("[$#@]", password):
            break
        elif re.search("\s", password):
            break
        else:
            print("Valid Password")
            x = False
            break

    if x:
        print("Not a Valid Password")
