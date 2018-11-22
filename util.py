def tah(pole, pozice, znak):  # tah
    pole = pole[:pozice] + znak + pole[pozice + 1:]
    return pole
