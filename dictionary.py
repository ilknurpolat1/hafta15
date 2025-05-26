def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n - 1)

n = int(input("Sayı seçiniz:"))
d = dict()
toplam = 0

for x in range(1, n + 1):
    d[x] = faktoriyel(x)
    toplam += d[x]

print("Faktöriyel:", d)
print("Toplam faktöriyel :", toplam)