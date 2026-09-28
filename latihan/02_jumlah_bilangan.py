# File: latihan/02_jumlah_bilangan.py

# Input bilangan bulat positif n
n = int(input("n: "))

# Inisialisasi variabel akumulator
total = 0

# Penjumlahan berulang dari 1 sampai n
for i in range(1, n + 1):
    total += i

# Menampilkan hasil akhir
print(f"Jumlah = {total}")