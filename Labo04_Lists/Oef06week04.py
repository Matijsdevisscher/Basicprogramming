#Maak een functie ‘kies_element’ aan met als parameter een list. De functie kiest een
#willekeurig element uit de doorgegeven list en geeft deze terug. Test deze functie met
# een list met strings, nl. de verschillende maanden
# een list met getallen
#Print telkens het gekozen element af

my_list = ["ma", "di", "wo", "do", "vr", "za", "zo"]

import random

def get_random_nmbr(my_list):
    random_nmbr = random.randint(0, len(my_list)-1)
    return (my_list)

print(get_random_nmbr(my_list))