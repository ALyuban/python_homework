from smartphone import Smartphone

catalog = [
    Smartphone("siemens", "K75", "+79631073151"),
    Smartphone("nokia", "3310", "+79623984556"),
    Smartphone("alkatel", "pozition", "+79085206378"),
    Smartphone("apple", "promax", "+79674455858"),
    Smartphone("xiaomi", "256x", "+79273682354")]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
