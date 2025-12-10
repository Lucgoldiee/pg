
def bin_to_dec(binarni_cislo):
    # Funkce přijme binární číslo jako int nebo str a vrátí jeho decimální hodnotu.
    # 111 -> 7
    # "101" -> 5

    # převedeme vstup na string (protože může přijít i jako int)
    bin_str = str(binarni_cislo)

    # ověření, že vstup obsahuje jen 0 a 1
    if not all(c in "01" for c in bin_str):
        raise ValueError("Vstup není platné binární číslo.")

    # vlastní převod pomocí int() s base=2
    return int(bin_str, 2)


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128

    # Príklad z úkolu:
    assert bin_to_dec("10011101") == 167

    print("Všechny testy úspěšně proběhly!")


