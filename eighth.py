def bin_to_dec(binarni_cislo):
    """
    Funkce spočítá hodnotu předávaného binárního čísla.
    binarni_cislo může být str i int.

    Příklady:
    111 -> 7
    "101" -> 5
    """
    
    s = str(binarni_cislo).strip()

    vysledek = 0
    for znak in s:
        if znak not in ("0", "1"):
            raise ValueError("Vstup musí být binární číslo složené jen z 0 a 1.")
       
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
    
    test_bin_to_dec()
    print("Všechny testy proběhly v pořádku.")
  
    print("10100111 v desítkové soustavě je:", bin_to_dec("10100111"))



