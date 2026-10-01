import time
import random

def begär_svar(text:str): #För jag är lat och orkar inte skriva allt detta varje gång
    while True:
        svar = input(text + " ").lower().strip()

        if svar == "y":
            return True
        elif svar == "n":
            return False
        else:
            print("Svara bara antingen y för ja eller n för nej")
            print()


namn = input("Vad vill du bli kallad? ")
print()

print(F"{namn} ligger i sin bädd och sover, som kapten har du din egen hytt på skeppet.")

time.sleep(3)

print("Plötsligt väcks du av din förste styrman...")

time.sleep(3)
print()

print(f"VAKNA KAPTEN {namn.upper()}!!!")
time.sleep(1.5)
print("Det finss ett skepp vid horisonten!")

time.sleep(3)
print()

print("Du springer upp till huvuddecket och mycket riktigt finns det ett skepp långt där borta")

time.sleep(3)

print()

if begär_svar(f"Förste styrman frågar dig: {namn}, ska vi försöka sänka det? (y/n)"):
    print("Okej, Vi tar och skjuter ner det!")

    time.sleep(3)
    print()

    print("Du styr skeppet närmare...")

    time.sleep(3)

    print("Kanonerna dundrar iväg några skott...")

    time.sleep(4)
    print()

    print("SKEPPET SKÖT TILLBAKA")

    time.sleep(2)

    print()

    print(f"Kapten {namn}! Vi blev rejält skadade efter de där skotten")
    if begär_svar("Vill du att vi ska överge skeppet? (y/n)"):
        print("Klokt val.")

        time.sleep(3)
        print()

        print("Du och din besättning flyr i livbåtarna")

        time.sleep(3)

        print("Ni kom ut med livet i behåll, men förlorade allt annat...")

    else: #Vill inte överge skepp
        print("Då ska ska vi försöka lassa vatten och forsätta strida!")
        time.sleep(3)

        print(".") #Dramatisk effekt
        time.sleep(0.5)
        print(".")
        time.sleep(0.5)
        print(".")

        time.sleep(2)

        if random.randint(0,1) == 0: #50/50 om det funkar
            print("Trots ert tappra försök sjönk skeppet ändå")
            time.sleep(3)
            print("Med hela besättningen i sig.")

        else:
            print("NI LYCKADES!!!!")
            time.sleep(2)

            print("Fiendeskeppet sjönk till slut!")

            time.sleep(3)

            print("Såklart fick ditt eget skepp några skråmor, men ni kom ut oskadda.")



else: #Du väljer avvaktning (inte skjuta skeppet)
    print("Som du vill, vi avvaktar.")

    time.sleep(3)

    print(".") #Dramatisk effekt
    time.sleep(0.5)
    print(".")
    time.sleep(0.5)
    print(".")

    time.sleep(2)

    print("Skeppet försvann bort i horisonten, ingen skada skedd!")

time.sleep(3)

print()
print("SLUT")