


sayı = int(input("Bir sayı Giriniz:"))
toplam = 0

for i in range(1, sayı):
    if sayı % i == 0:   # i sayının böleni mi?
        toplam += i

if toplam == sayı:
    print(sayı, "mükemmel bir sayıdır.")
else:
    print(sayı, "mükemmel bir sayı değildir.")