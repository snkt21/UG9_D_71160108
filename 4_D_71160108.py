#Surya Nathaniel Kattu
#Nim: 71160108
#Soal No 4

a = int(input("Nilai suku pertama (U1) : "))
u2 = int (input("Nilai u2: "))
n = int(input("Suku ke : "))
r = u2/a #rasio didapatkan dari suku ke-2 dibagi suku ke-1 (a)

un = (a * r ** (n-1))

print(un)