
a = 1
b = 1
fibonocci = [a,b]
for i in range(20):
    a,b = b,a+b
    fibonocci.append(b)
print(fibonocci)