
# Pertemuan 07 Fungsi Python

Nama: Laila Fadhilah  
NIM: 2225250030  
Kelas: 3A

## Tujuan

Mempelajari fungsi, parameter, return value, dan scope
untuk membuat program Python yang modular dan mudah diuji.

## Struktur Folder

- `latihan/01_salam.py`: fungsi salam dengan parameter.
- `latihan/02_luas_persegi_panjang.py`: menghitung luas.
- `latihan/03_jumlah_n.py`: menjumlahkan bilangan 1 sampai n.
- `latihan/04_statistik_sederhana.py`: menghitung minimum,
  maksimum, dan rata-rata.
- `latihan/05_scope.py`: mempelajari local scope dan global scope.
- `praktik/utilitas_matematika.py`: program menu utilitas matematika.

## Cara Menjalankan

Jalankan latihan dengan perintah:

`python latihan/01_salam.py`

Ganti nama file sesuai latihan yang ingin dijalankan.

Untuk menjalankan program utama:

`python praktik/utilitas_matematika.py`

## Struktur Fungsi

- `salam(nama, kelas)` menampilkan salam dan kelas.
- `luas_persegi_panjang(p, l)` mengembalikan hasil p × l.
- `jumlah_n(n)` mengembalikan jumlah bilangan 1 sampai n.
- `statistik(data)` mengembalikan minimum, maksimum,
  dan rata-rata.
- `demo(x)` menunjukkan penggunaan variabel lokal.
- `luas_segitiga(a, t)` mengembalikan luas segitiga.
- `faktorial(n)` mengembalikan hasil faktorial.
- `tampilkan_menu()` menampilkan pilihan operasi.

## Hasil Pengujian

| Pengujian | Input | Hasil Aktual | Status |
|---|---|---|---|
| Luas persegi panjang | 8, 5 | 40 | Berhasil |
| Luas segitiga | 10, 6 | 30.0 | Berhasil |
| Jumlah 1 sampai n | 10 | 55 | Berhasil |
| Faktorial | 5 | 120 | Berhasil |
| Faktorial | 0 | 1 | Berhasil |

## Refleksi

Penggunaan fungsi membuat program lebih terstruktur karena
setiap fungsi memiliki tugas tertentu. Parameter digunakan
untuk menerima data, sedangkan return mengirimkan hasil
agar dapat digunakan kembali. Pemahaman scope juga membantu
membedakan variabel lokal dan global.
