#oefening 04

getal1 = int(input("Geef de leeftijd op van u hond: "))

if (getal1 < 0):
    print("Error ")
elif(getal1 == 1):
    print("Deze leeftijd komt overeen met 14 mensenjaren")
elif(getal1 == 2):
    print("Deze leeftijd komt overeen met 22 mensenjaren")
else:
    resultaat = 22 + (getal1 -2) * 5
    print(resultaat)




