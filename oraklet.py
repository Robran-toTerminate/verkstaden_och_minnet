import random

svar = ["Ja helt klart","Absolut inte"]


fråga = "hejsan" #input("Fråga oraklet ")

print("Du frågade:", fråga)

print(random.choice(svar))

if random.random() < 0.1:
    print("Men om du betalar 1000 kr kan jag ge dig ett mer exakt svar.")
