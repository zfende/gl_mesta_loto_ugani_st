# -*- coding: utf-8 -*-
import random
print ("Pozdravljeni v igri ugani skrito stevilo!")

def main():
    skrivno_stevilo = random.randint(1, 100)

    while True:
        ugani_stevilo = int(raw_input("Izberite stevilo med 1 in 100: "))
        if ugani_stevilo == skrivno_stevilo:
            print ("BRAVO USPELO TI JE!")
            nova_igra = raw_input("Nova igra? ").lower()
            if nova_igra == "da":
                main()
            else:
                print ("Adijo")
                break
        elif ugani_stevilo > skrivno_stevilo:
            print ("Nizje, ugani stevilo se enkrat: ")
        else:
            print ("Visje, ugani stevilo se enkrat: ")

if __name__ == "__main__":
    main()