logid = [
{"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Kasutaja sisenes süsteemi."},
{"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Ülesanne lõppes edukalt."},
{"aeg": "2025-03-10", "tüüp": "hoiatus", "sõnum": "Kõvakettal on vähe vaba ruumi."},
{"aeg": "2025-03-10", "tüüp": "error", "sõnum": "Andmebaasi ühendus ebaõnnestus."},
{"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Süsteemi värskendus on valmis."},
{"aeg": "2025-03-10", "tüüp": "error", "sõnum": "Faili laadimine ebaõnnestus."},
{"aeg": "2025-03-10", "tüüp": "info", "sõnum": "Logimine on lõpetatud."}
]
info_count = 0
for elem in logid:
    if elem["tüüp"] ==  "info":
        info_count2 = info_count + 1
print(info_count2)