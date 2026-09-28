print("Deret Aritmetika")

# 1. Membaca input a dan d sebagai float
a = float(input("Suku pertama a: "))
d = float(input("Beda d: "))

# 2. Membaca input n sebagai integer
n = int(input("Banyak suku n: "))

# 3. Validasi n berulang menggunakan while (harus bilangan bulat positif)
while n <= 0:
    print("n harus bilangan bulat positif.")
    n = int(input("Banyak suku n: "))

# 4. Inisialisasi akumulator total sebelum loop
total = 0

# 5. Perulangan for untuk menghasilkan n suku dan menghitung jumlah
for i in range(n):
    suku = a + i * d
    total += suku
    print(f"Suku ke-{i + 1}: {suku:.2f}")

# 6. Menampilkan jumlah akhir dengan dua angka di belakang koma
print(f"Jumlah: {total:.2f}")