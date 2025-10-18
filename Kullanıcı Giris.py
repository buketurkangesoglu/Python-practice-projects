print("""****************************
Kullanıcı Giriş Ekranı
****************************
""")

sys_kullanici_adi = "Türkan"
sys_kullanici_soyadi = "Gesoğlu"
sys_parola = "1234"

kullanici_adi = input("Kullanıcı Adı:")
parola = input("Parola:")

if (kullanici_adi == sys_kullanici_adi and parola != sys_parola):
    print("Parola Hatalıdır...")

elif(kullanici_adi != sys_kullanici_adi and parola == sys_parola):
    print("Kullanıcı Adı Hatalıdır")

elif(kullanici_adi != sys_kullanici_adi and parola != sys_parola):
    print("Kullanıcı Adı ve Parola Hatalı")

else:
    print("Bu Bilgileri Doldurmak Zorunludur!")