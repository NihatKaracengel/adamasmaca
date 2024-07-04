"""BU KODLARI BEN YAZDIM"""
import random
from gorseller import gorsel_hata

kelime_listesi = ["nihat","karaçengel","karpuz","levrek","fofana"]
kelime = random.choice(kelime_listesi)
kalan_can = 0
harf_tahminleri = []
adam_asmaca_kelime = list("_" * len(kelime))

print("Adam Asmaca Oyununa Hoşgeldiniz.")
print("Oyunda Toplam 7 Hakkınız vardır!")

while kalan_can < 7 and "_" in adam_asmaca_kelime:
    print(" ".join(adam_asmaca_kelime)) # _ _ _ _ _ _
    #print(adam_asmaca_kelime) # ['_', '_', '_', '_', '_', '_']
    print(gorsel_hata(kalan_can))
    tahmin = input("Harf tahmini yapınız: ").lower()
    if tahmin in harf_tahminleri: #tahmin daha önceki tahminlerdense:
        print("{} harfini daha önce kullandınız!".format(tahmin))
    elif tahmin in kelime: # tahmin kelime içindeyse:
        harf_tahminleri.append(tahmin) #tahmini tahmin edilen harflere ekle
        for indeks,harf in enumerate(kelime): #0:n ,1:i, 2:h ...
            if tahmin == harf:
                adam_asmaca_kelime[indeks] = harf # _ _ _ _ _ => n _ _ _ _
                print("Doğru. Kalan can: {}".format(kalan_can))
    else:
        harf_tahminleri.append(tahmin)
        kalan_can += 1
        print("{} harfi kelimede yok. Kalan hak: {}".format(tahmin, 7- kalan_can))

if kalan_can == 7:
    print("Oyun bitti. Doğru kelime: {}".format(kelime))
else:
    print(adam_asmaca_kelime)
    #print(" ".join(adam_asmaca_kelime))
    print("Oyun bitti kazandınız!")





