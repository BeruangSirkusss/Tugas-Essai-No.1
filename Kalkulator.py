a = int(input("Masukan Harga Awal : "))
b = int(input("Masukan Berapa Tahun Manfaat :"))
c = int(input("Masukan Masa Pakai :"))
d = int(input("Masukan Sisa Nilai Setelah Tahun Manfaat :"))

ST = (a - d) / b
j = ST * c
HS = a - j

print(HS)