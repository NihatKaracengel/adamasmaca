"""Main2deki kodları fonksiyonlu yazmaya çalış"""

import random
from gorseller import gorsel_hata

kelime_listesi = ["nihat","karaçengel","karpuz","levrek","fofana"]

def kelime():
    return random.choice(kelime_listesi)

kalan_can = 0
harf_tahminleri = []
adam_asmaca_kelime = list("_" * len(kelime()))

while kalan_can < 7:
    print(adam_asmaca_kelime)
    print(gorsel_hata(kalan_can))
    tahmin = input("Harf tahmini yapınız: ").lower()
    if tahmin in harf_tahminleri:
        print("{} harfini daha önce kullandınız!".format(tahmin))
    elif tahmin in kelime:
        harf_tahminleri.append(tahmin)
        for indeks,harf in enumerate(kelime):
            if tahmin == harf:
                adam_asmaca_kelime[indeks] = harf
    else:
        harf_tahminleri.append(tahmin)
        kalan_can += 1
        print("{} harfi kelimede yok. Kalan hak: {}".format(tahmin, kalan_can))

if kalan_can == 7:
    print("Oyun bitti. Doğru kelime: {}".format(kelime))





