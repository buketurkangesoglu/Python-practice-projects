toplam = 0
while True:
    sayı = input("sayı: ")
    if (sayı == 'q'):
        break
    sayı = int(sayı)

    toplam += sayı
    print("Girdiğiniz sayıların Toplamı:", toplam)