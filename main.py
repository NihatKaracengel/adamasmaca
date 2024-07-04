"""Bu kodları chatgpt yazdı"""
import random
from gorseller import gorsel_hata

# Kelime listesini oluştur
kelimeler = ["elma", "armut", "muz", "kiraz", "karpuz", "üzüm", "kavun"]

def kelime_sec():
    return random.choice(kelimeler)

def adam_asmaca():
    kelime = kelime_sec()
    tahmin_edilen = ["_"] * len(kelime)
    hatalar = 0
    tahminler = []

    print("Adam asmaca oyununa hoş geldiniz!")
    print("Bir kelime tahmin etmeye çalışın.")
    print(gorsel_hata(hatalar))
    print(" ".join(tahmin_edilen))

    while hatalar < 6 and "_" in tahmin_edilen:
        tahmin = input("Bir harf tahmin edin: ").lower()

        if tahmin in tahminler:
            print("Bu harfi zaten tahmin ettiniz.")
        elif tahmin in kelime:
            tahminler.append(tahmin)
            for index, harf in enumerate(kelime):
                if harf == tahmin:
                    tahmin_edilen[index] = tahmin
        else:
            tahminler.append(tahmin)
            hatalar += 1
            print(f"Yanlış tahmin! {6 - hatalar} hakkınız kaldı.")

        print(gorsel_hata(hatalar))
        print(" ".join(tahmin_edilen))

    if "_" not in tahmin_edilen:
        print("Tebrikler! Kelimeyi doğru tahmin ettiniz:", kelime)
    else:
        print("Kaybettiniz! Kelime:", kelime)

adam_asmaca()
