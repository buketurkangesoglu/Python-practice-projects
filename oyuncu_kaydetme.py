print("Oyuncu Kaydetme Programı")

ad = input("Adı:")
soyad = input("Soyadı:")
yas = int(input("Yaşı:"))
takim = input("Takımı:")
ayak = input("Ayak:")
pozisyon = input("Pozisyon:")


bilgiler = [ad,soyad,yas,takim,ayak,pozisyon]

print("Bilgiler Kaydediliyor.....")

print("Adı: {}\nSoyadı: {}\nYaşı: {}\nTakımı: {}\nAyak: {}\nPozisyon: ".format(bilgiler[0],bilgiler[1],bilgiler[2],bilgiler[3],bilgiler[4],bilgiler[5]))

print("Bilgiler Kaydedildi")