import random

def main():
    drzave_v_mesta = {
        "Slovenija": "Ljubljana",
        "Italija": "Rim",
        "Avstrija": "Dunaj",
        "Hrvaska": "Zagreb",
        "Nemcija": "Berlin",
        "Francija": "Paris",
        "Nizozemska": "Amsterdam",
    }

    for drzava in drzave_v_mesta:
        random_num = random.randint(0, 6)
        drzava = drzave_v_mesta.keys()[random_num]
        uganjeno_mesto = raw_input("Katero je glavno mesto drzave " + drzava + ": ")

        preveri(drzava, uganjeno_mesto, drzave_v_mesta)

def preveri(drzava, uganjeno_mesto, drzave_v_mesta):
    dejansko_mesto = drzave_v_mesta[drzava]
    if uganjeno_mesto == dejansko_mesto:
        print ("Pravilno")
    else:
        print ("Napacno")

if __name__ == '__main__':
    main()
