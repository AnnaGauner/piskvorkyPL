from random import randrange
import util
import ai

pole = 20*"-"
print(
    "Zahraj si piskvorky. Pro vyhru je treba mit tri znaky vedle sebe. Vyber si znak (x nebo o) a zapisuj pozice (0-19}, "
    "na ktere chces tahnout.")
print(pole)

znak_hrace = input("Znak: ")
if znak_hrace == "x":
    znak_pocitace = "o"
if znak_hrace == "o":
    znak_pocitace = "x"

def vyhodnot(pole):
    if "xxx" in pole:
        print("Vyhral hrac se znakem x!")
        return "x"
    elif "ooo" in pole:
        print("Vyhral hrac se znakem o!")
        return "o"
    elif '-' in pole:
        return "-"
    else:
        print("Remiza!")
        return "!"

def tah_hrace(pole):
    pozice = int(input("Pozice: "))

    while True:
        if pozice < 0 or pozice > 19: #overeni, zda je pozice v oblasti 0-19
            pozice = int(input("Zadej pozici od 0 do 19. "))
        if pole[pozice] != "-": #overeni, zda je pozice neobsazena
            pozice = int(input("Tato pozice je jiz obsazena. Zadej neobsazenou pozici od 0 do 19. "))
        else:
            break

    pole = util.tah(pole, pozice, znak_hrace)  # samotny tah hrace
    return pole

def piskvorky(pole):
    vysledek = vyhodnot(pole)
    while vysledek == "-":
        pole = tah_hrace(pole)
        vysledek = vyhodnot(pole)
        if vysledek == "x" or vysledek == "o":
            print(pole)
            break

        pole = ai.tah_pocitace(pole, znak_pocitace)
        vysledek = vyhodnot(pole)
