import random

target_number = random.randrange(0,10)

MAX_TRIES = 3


print("Vilket tal mellan 0 och 10 tänker datorn på?")

tries = 0
while tries < MAX_TRIES:
    while True:
        try:
            gissning = int(input("Vad gissar du? "))
            break
        except ValueError:
            print("Använd nummer i din gissning.")

    if gissning == target_number:
        print("Rätt!")
        break
    else:
        print("Fel")
        if gissning < target_number:
            print("Gissa ett högre nummer")
        else:
            print("Gissa ett lägre nummer")

        tries += 1

if tries == MAX_TRIES:
    print("Otur men du förlorade!")
    print(f"Rätt svar var {target_number}")