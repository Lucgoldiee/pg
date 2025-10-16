
import math

def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False.
    """
    # Prvočíslo je větší než 1
    if cislo <= 1:
        return False
    # 2 a 3 jsou prvočísla
    if cislo <= 3:
        return True
    # Sudá čísla a násobky 3 nejsou prvočísla
    if cislo % 2 == 0 or cislo % 3 == 0:
        return False
    # Test dělitelnosti do odmocniny čísla
    for i in range(5, int(math.sqrt(cislo)) + 1, 2):
        if cislo % i == 0:
            return False
    return True


def vrat_prvocisla(maximum):
    """
    Funkce spocita vsechna prvocisla v rozsahu 1 az maximum a vrati je jako seznam.
    """
    try:
        maximum = int(maximum)
    except ValueError:
        return []

    prvocisla = []
    for i in range(2, maximum + 1):
        if je_prvocislo(i):
            prvocisla.append(i)
    return prvocisla


if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
