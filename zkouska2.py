
# Příklad 2: Práce s externími daty a výpočty
# Zadání:
# Napište funkci `convert_to_czk`, která:
# 1. Přijme částku (`amount`) jako desetinné číslo a kód měny (`currency`) jako řetězec (např. "USD", "EUR").
# 2. Stáhne aktuální kurzovní lístek z URL:
#    http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt
# 3. Načte příslušný kurz podle zadaného kódu měny a provede převod zadané částky na české koruny (CZK).
# 4. Funkce vrátí výslednou částku v CZK zaokrouhlenou na dvě desetinná místa.
# Pokud zadaná měna v kurzovním lístku neexistuje, vyhoďte výjimku `ValueError`.

import requests
URL = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"

def convert_to_czk(amount, currency):
    resp = requests.get(URL)
    if not resp.ok:
        raise ConnectionError(
            f"Failed to fetch exchange rates (HTTP {resp.status_code})."
        )

    lines = resp.text.splitlines()[2:]

    for line in lines:
        if not line.strip():
            continue

        parts = line.split("|")
        if len(parts) != 5:
            continue

        _, _, unit_str, code, rate_str = parts

        if code == currency:
            unit = int(unit_str)
            rate = float(rate_str.replace(",", "."))
            return round(amount * rate / unit, 2)

    raise ValueError(f"Currency {currency} not found in the exchange rate list.")

# Unit testy
from unittest.mock import patch, MagicMock

def test_convert_to_czk():
    mock_response = """31.10.2025 #237
země|měna|množství|kód|kurz
Austrálie|dolar|1|AUD|14,894
EMU|euro|1|EUR|25,480
USA|dolar|1|USD|23,000
Velká Británie|libra|1|GBP|29,745
"""
    with patch("requests.get") as mock_get:
        mock_get.return_value = MagicMock(ok=True, status_code=200, text=mock_response)

        assert convert_to_czk(100, "USD") == 2300.00
        assert convert_to_czk(50, "EUR") == 1274.00
        assert convert_to_czk(200, "AUD") == 2978.80
        
        try:
            convert_to_czk(100, "XYZ")
        except ValueError as e:
            assert str(e) == "Currency XYZ not found in the exchange rate list."

if __name__ == "__main__":
    test_convert_to_czk()
    print(convert_to_czk(100, "USD"))
    print(convert_to_czk(50, "EUR"))
    print(convert_to_czk(200, "AUD"))
