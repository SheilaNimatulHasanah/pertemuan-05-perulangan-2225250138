# File: latihan/04_hitung_genap.py

# Input batas n
n = int(input("n: "))

# Inisialisasi pencacah
jumlah_genap = 0

# Pengecekan setiap bilangan dari 1 sampai n
for i in range(1, n + 1):
    if i % 2 == 0:
        jumlah_genap += 1

# Menampilkan total bilangan genap
print(f"Banyak bilangan genap: {jumlah_genap}")