

d = int(input("Geef het aantal dagen op: "))
u = int(input("Geef het aantal uren op: "))
m = int(input("Geef het aantal minuten op: "))
s = int(input("Geef het aantal seconden op: "))

totaal = d * 86400 + u * 3600 + m *60

print("Het totale aantal seconden is:" %totaal)