print("""
**************************************
Vücut Kitle İndeksi Hesaplama Programı
**************************************
""")
boy = float(input("Boy:"))
kilo = int(input("Kilo"))
VKI = float(kilo / (boy ** 2))
print("VKI:{:.1f} idir".format(VKI))

if (VKI < 18.5):
    print("Zayıf")
elif(18.5 < VKI < 25):
    print("Normal Aralık")
elif(VKI > 30):
    print("Fazla Kilolu")