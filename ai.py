import util
from random import randrange

def tah_pocitace(pole, znak_pocitace):
    while True:
        pozice = randrange(0, 20)
        if pole[pozice] == "-":
            break

    pole = util.tah(pole, pozice, znak_pocitace)  # samotny tah pocitace
    print(pole)
    return pole