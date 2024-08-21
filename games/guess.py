import random

def sayi_tahmin_oyunu():
    gizli_sayi = random.randint(1, 100)
    tahmin_hakki = 5

    print("Sayı Tahmin Oyununa Hoş Geldiniz!")
    print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")

    while tahmin_hakki > 0:
        tahmin = int(input(f"{tahmin_hakki} tahmin hakkın kaldı. Bir sayı gir: "))

        if tahmin < gizli_sayi:
            print("Daha büyük bir sayı tahmin etmelisin!")
        elif tahmin > gizli_sayi:
            print("Daha küçük bir sayı tahmin etmelisin!")
        else:
            print("Tebrikler! Sayıyı doğru tahmin ettin!")
            break

        tahmin_hakki -= 1

    if tahmin_hakki == 0:
        print(f"Maalesef tahmin hakkın bitti. Doğru sayı {gizli_sayi} idi.")

sayi_tahmin_oyunu()
