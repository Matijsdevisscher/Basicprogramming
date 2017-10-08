

def geef_celcius (getalcelsius):
    temp = (t_in_fahrenheit - 32) * 5 / 9
    print(temp)

def geef_fahrenheit (getalfahrenheit):
    temp = (temp_in_celsius * 9 / 5) + 32
    print(temp)

eenheid = int(input("Welke eenheid gebruikt u? C: Celsius, F: Fahrenheit  "))

if(eenheid == C):
    print("Geef een temperatuur in celsius op: ")

elif(eenheid == F):
    print("Geef een temperatuur in fahrenheit op: ")

else:
    print("ERROR: Geef de eerste letter op van de gebruikte eenheid Celsius of Fahrenheit")


