import random

def yilbasi_cekilisi():
    
    katilimcilar = []
    
    print("Yılbaşı Çekilişine Hoş Geldiniz!")
    print("Katılımcı isimlerini teker teker girin. Katılımcı eklemeyi bitirmek için 'bitir' yazın.")
    
    while True:
        isim = input("Katılımcı ismi girin: ")
        if isim.lower() == 'bitir':
            break
        katilimcilar.append(isim)
    
    if len(katilimcilar) == 0:
        print("Katılımcı yok. Çekiliş yapılamaz!")
    else:

        kazanan = random.choice(katilimcilar)
        print(f"Tebrikler! Yılbaşı çekilişini kazanan: {kazanan}")


yilbasi_cekilisi()
