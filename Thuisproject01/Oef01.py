# Oef 1: Schrijf onderstaande functies.
# Elke functie heeft één parameter van het datatype String.
# - Functie ‘tel_cijfers’: geeft het aantal cijfers uit de string terug
# - Functie ‘tel_kleine_letters’: geeft het aantal kleine letters terug
# - Functie ‘tel_hoofdletters’: geeft het aantal hoofdletters terug.



tekst = input("Geef de tekst op die je wil onderzoeken: ")


def tel_cijfers(tekst):
    cijfers = sum(x.isdigit() for x in tekst)
    return cijfers
def tel_kleine_letters(tekst):
    kleine_letters = sum(x.islower() for x in tekst)
    return kleine_letters

def tel_hoofdletters(tekst):
    hoofdletters = sum(x.isupper() for x in tekst)
    return  hoofdletters

print("De onderzochte string is: {}".format(tekst))
print("Het aantal cijfers in deze zin is: {}".format(tel_cijfers(tekst)))
print("Het aantal kleine letters in deze zin is: {}".format(tel_kleine_letters(tekst)))
print("Het aantal hoofdletters in deze zin is: {}".format(tel_hoofdletters(tekst)))