

def celcius (T_in_fahrenheit):
    return (T_in_fahrenheit - 32) * 5 / 9

def fahrenheit (T_in_celsius):
    return (T_in_celsius * 9 / 5) + 32

eenheid = int(input("Welke eenheid gebruikt u? C: Celsius, F: Fahrenheit  "))

if(eenheid == C):
    print("Geef een temperatuur in celsius op: ")

elif(eenheid == F):
    print("Geef een temperatuur in fahrenheit op: ")

else:
    print("ERROR: Geef de eerste letter op van de gebruikte eenheid Celsius of Fahrenheit")

eenheid = input("Welke eenheid gebruikt u? [C: celsius, F: fahrenheit] ")
opgegeven_eenheid = "celsius" if (eenheid == "C")

