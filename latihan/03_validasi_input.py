# File: latihan/03_validasi_input.py

# Input nilai awal
nilai = float(input("Nilai 0-100: "))

# Perulangan berjalan selama nilai tidak valid (< 0 atau > 100)
while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = float(input("Nilai 0-100: "))

# Menampilkan nilai yang berhasil diterima
print(f"Nilai diterima: {nilai}")