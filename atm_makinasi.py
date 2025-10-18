print("""**************************
ATM Makinasına Hoşgeldiniz


işlemler:

1.Bakiye Sorgulama
2.Para Yatırma 
3.Para Çekme

Programdan Çıkmk İçin 'q'ya basın 
**************************
""")

bakiye = 500000
while True:
    işlem  = input("işlemi giriniz:")

    if (işlem == "q"):
        print("yine bekleriz")
        break
    elif (işlem == "1"):
        print("Bakiyeniz: {} TL idir".format(bakiye))
    elif (işlem == "2"):
        miktar = int(input("Miktar Giriniz"))
        bakiye += miktar
    elif (işlem == "3"):
        miktar = int(input("Çekmek İstediğiniz Miktarı Giriniz: "))
        if (bakiye < miktar):
            print("Bakiyeniz Yetersiz..")
        else:
            bakiye -= miktar
    else:
        print("Geçersiz İşlem...")


