# Oef 2: Schrijf onderstaande functies.
# Elke functie heeft één parameter van het datatype String.
# - Functie ‘swap_lower_upper’: wisselt hoofdletters met kleine letters (en omgekeerd)
# binnen de doorgegeven string.
# Het resulaat wordt teruggegeven.
# - Functie ‘shuffle’: verwisselt de woorden binnenin de doorgegeven string.
# Het resultaat wordt teruggegeven.


import random

string = input("Geef een string op: ")

def swap_lower_upper(string):
    for x in string:
        if x.isupper():
            result += x.lower()
        else:
            result += x.upper()

def shuffle(string):
    random.shuffle(string)

string1 = swap_lower_upper(string)
string2 = shuffle(string)


print(string1)
print(string2)