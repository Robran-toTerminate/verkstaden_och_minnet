def begär_svar(text:str):
    while True:
        svar = input(text).lower().strip()

        if svar == "y":
            return True
        elif svar == "n":
            return False
        else:
            print("Svara bara antingen y eller n")



print()

if begär_svar("Vill du spela?"):
    print("Bra")
else:
    print("Tråkigt")