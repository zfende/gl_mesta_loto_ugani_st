# -*- coding: utf-8 -*-
import random
print ("Pozdravljeni v LOTO Generatorju")

def main():
    koliko_stevil = int(raw_input("Koliko naključnih števil želite: "))
    stevila = []
    while len(stevila) < koliko_stevil:
        novo_stevilo = random.randrange(1, 51)
        if not novo_stevilo in stevila:
            stevila.append(novo_stevilo)
    loto_stevilke = sorted(stevila)
    print loto_stevilke

if __name__ == "__main__":
    main()