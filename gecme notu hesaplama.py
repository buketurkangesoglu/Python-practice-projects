print("""******************

Geçme Notu Hesaplama*****************

""")

vize1= int(input("Vize 1.Notu Giriniz : "))
vize2 = int(input("Vize 2.notu Giriniz : "))
final = int(input("final Notunu Giriniz :"))
Toplam = ((vize1 * 30) / 100) + ((vize2 * 30) / 100) + ((final * 40 ) / 100)

print("Notunuz: {}".format(Toplam))
if Toplam >= 90:
    print("Geçme Notu:AA")
elif Toplam >= 85:
    print("Geçme Notu:BA")
elif Toplam >= 80:
    print("Geçme Notu:BB")
elif Toplam >= 75:
    print("Geçme Notu:CB")
elif Toplam >= 70:
    print("Geçme Notu : CC")
elif Toplam >= 65:
    print("Geçme Notu : DC")
elif Toplam >= 60:
    print("Geçme Notu : DD")
elif Toplam >= 55:
    print("Geçme Notu : FD")
elif Toplam < 55:
    print("Geçme Notu : FD", "Kaldınız")