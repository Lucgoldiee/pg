
def _na_sachovnici(p):
    """Vrať True, pokud je pozice na šachovnici 1..8 × 1..8."""
    r, c = p
    return 1 <= r <= 8 and 1 <= c <= 8


def _cesta_volna(start, cil, obsazene):
    
    sr, sc = start
    tr, tc = cil
    dr = tr - sr
    dc = tc - sc

    
    step_r = 0 if dr == 0 else (1 if dr > 0 else -1)
    step_c = 0 if dc == 0 else (1 if dc > 0 else -1)

    
    if not (dr == 0 or dc == 0 or abs(dr) == abs(dc)):
        return False

    r, c = sr + step_r, sc + step_c
    while (r, c) != (tr, tc):
        if (r, c) in obsazene:
            return False
        r += step_r
        c += step_c
    return True


def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
    """
    Ověří, zda se figurka může přesunout na danou pozici.

    :param figurka: Slovník s informacemi o figurce (typ, pozice).
    :param cilova_pozice: Cílová pozice na šachovnici jako n-tice (řádek, sloupec).
    :param obsazene_pozice: Množina obsazených pozic na šachovnici.
    
    :return: True, pokud je tah možný, jinak False.

    """
    typ = figurka.get("typ")
    start = figurka.get("pozice")

  
    if not _na_sachovnici(start) or not _na_sachovnici(cilova_pozice):
        return False

   
    if cilova_pozice in obsazene_pozice:
        return False

    sr, sc = start
    tr, tc = cilova_pozice
    dr, dc = tr - sr, tc - sc
    adr, adc = abs(dr), abs(dc)

    if typ == "pěšec":
        
        if dc != 0:
            return False
        
        if dr == 1:
            return True
        
        if sr == 1 and dr == 2:
            mezi = (sr + 1, sc)
            return mezi not in obsazene_pozice
        return False

    if typ == "jezdec":
        return (adr, adc) in {(1, 2), (2, 1)}

    if typ == "věž":
        if sr == tr or sc == tc:
            return _cesta_volna(start, cilova_pozice, obsazene_pozice)
        return False

    if typ == "střelec":
        if adr == adc and adr != 0:
            return _cesta_volna(start, cilova_pozice, obsazene_pozice)
        return False

    if typ == "dáma":
        if (sr == tr or sc == tc) or (adr == adc and adr != 0):
            return _cesta_volna(start, cilova_pozice, obsazene_pozice)
        return False

    if typ == "král":
        return max(adr, adc) == 1

    
    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}

    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))  # True
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))  # False (mezi musí být volno a pesec z 1. řady)
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))  # False (pěšec nemůže couvat)

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))  # False (není to L)
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))  # False (cílové pole obsazené)
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))  # True
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))  # False (mimo šachovnici)

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))  # False (v cestě stojí jiná figura)
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))  # False (v cestě stojí jiná figura)
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))  # True
