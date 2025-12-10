def bin_to_dec(binarni_cislo):
    """
    Funkce spočítá hodnotu předávaného binárního čísla.
    binarni_cislo může být str i int.

    Příklady:
    111 -> 7
    "101" -> 5
    """
    # Převedeme vstup na řetězec (abychom uměli pracovat s int i str)
    s = str(binarni_cislo).strip()

    vysledek = 0
    for znak in s:
        if znak not in ("0", "1"):
            raise ValueError("Vstup musí být binární číslo složené jen z 0 a 1.")
        # posuneme dosavadní číslo doleva (vynásobíme 2) a přičteme aktuální bit
        vysledek = vysledek * 2 + int(znak)

    return vysledek


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128


if __name__ == "__main__":
    # Spuštění jednoduchého testu při přímém spuštění souboru
    test_bin_to_dec()
    print("Všechny testy proběhly v pořádku.")
    # ukázkový výpočet (můžeš si libovolně změnit)
    print("10011101 v desítkové soustavě je:", bin_to_dec("10011101"))



