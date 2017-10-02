
import datetime
geboortejaar = int(input("Wat is uw geboortejaar? "))

limiet = datetime.datetime.now().year -18

if (geboortejaar > limiet):
    print("Je bent te jong")
else:
    print("let's drink")

