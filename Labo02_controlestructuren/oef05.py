#oefening 5 week02

import math
score = float(input("Geef jouw decimale score van de module op: "))

deelNaKomma = score - int(score)

if (deelNaKomma<=0.5):
    score = math.floor(score)
    print("U bent geslaagd")
else:
    score = math.ceil(score)
    print("U bent niet geslaagd")
if (score<10):
    print(str(round(score)) + "Sorry. Niet geslaagd")
else:
    print(str(round(score)) + "Perfect")

print(score)

