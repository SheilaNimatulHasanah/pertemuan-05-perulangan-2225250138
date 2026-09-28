# Pertemuan 05 Perulangan Python

Nama: Sheila Ni'matul Hasanah
NIM: 2225250138
Kelas: 3B

## Tujuan
Menggunakan for dan while untuk menyelesaikan masalah iteratif.

## Cara Menjalankan
python3 kuis/kuis2_deret_aritmetika.py

## Algoritma Kuis 2
1. Input a (suku pertama), d (beda) sebagai float, dan n (banyak suku) sebagai int.
2. Validasi n dengan while n <= 0 hingga input bernilai positif.
3. Set total = 0 sebelum perulangan.
4. Perulangan for i in range(n): hitung suku = a + i * d, tambahkan ke total, lalu tampilkan suku.
5. Tampilkan total akhir dengan format dua angka di belakang koma.

## Hasil Pengujian

| Input (a, d, n) | Keluaran Diharapkan | Keluaran Aktual | Status |
| :--- | :--- | :--- | :--- |
| 2, 3, 5 | Suku: 2, 5, 8, 11, 14 \| Jumlah: 40.00 | Suku: 2.00, 5.00, 8.00, 11.00, 14.00 \| Jumlah: 40.00 | Berhasil |
| 10, -2, 4 | Suku: 10, 8, 6, 4 \| Jumlah: 28.00 | Suku: 10.00, 8.00, 6.00, 4.00 \| Jumlah: 28.00 | Berhasil |
| 1.5, 0.5, 3 | Suku: 1.5, 2.0, 2.5 \| Jumlah: 6.00 | Suku: 1.50, 2.00, 2.50 \| Jumlah: 6.00 | Berhasil |

## Refleksi
Kesalahan yang ditemui adalah menempatkan total = 0 di dalam loop for sehingga nilai selalu ter-reset. Solusinya adalah memindahkan inisialisasi total = 0 ke luar (sebelum) loop.