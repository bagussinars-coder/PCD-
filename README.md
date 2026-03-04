## 1. Penjelasan Program

Program ini digunakan untuk:
- Membuat pasangan kunci RSA (public key dan private key)
- Mengenkripsi pesan (plaintext) menjadi ciphertext
- Mendekripsi ciphertext kembali menjadi plaintext

Program bekerja dengan langkah-langkah utama:
1. Pengguna memasukkan dua bilangan prima (`p` dan `q`)
2. Program menghitung nilai `n` dan `phi`
3. Program memilih nilai `e` secara otomatis
4. Program menghitung nilai `d` sebagai kunci privat
5. Pengguna dapat memilih menu enkripsi atau dekripsi

Kunci yang dihasilkan:
- **Public Key (e, n)** → digunakan untuk enkripsi  
- **Private Key (d, n)** → digunakan untuk dekripsi  

---

## 2. Alur Program

Alur kerja program adalah sebagai berikut:

1. Program meminta pengguna memasukkan bilangan prima `p`  
2. Program meminta pengguna memasukkan bilangan prima `q`  
3. Program menghitung:
   - `n = p × q`
   - `phi = (p − 1)(q − 1)`
4. Program memilih nilai `e` secara otomatis sehingga relatif prima dengan `phi`
5. Program menghitung nilai `d` menggunakan invers modulo
6. Program menampilkan:
   - Public key `(e, n)`
   - Private key `(d, n)`
7. Program menampilkan menu:
   - 1 → Enkripsi  
   - 2 → Dekripsi  
   - 3 → Keluar  
8. Jika memilih enkripsi:
   - Pengguna memasukkan plaintext
   - Program mengubah plaintext menjadi ciphertext
9. Jika memilih dekripsi:
   - Pengguna memasukkan ciphertext
   - Pengguna memasukkan kunci privat `d` dan nilai `n`
   - Program mengubah ciphertext menjadi plaintext

---

## 3. Cara Menjalankan Program (Run Program)

### a. Persiapan
Pastikan:
- Python sudah terinstal di komputer  
- File program disimpan dengan nama misalnya:

- 
---

### b. Menjalankan Program

Buka terminal atau command prompt, lalu ketik:

```bash
python rsa.py

c. Contoh Penggunaan

Masukkan bilangan prima:

Masukkan bilangan prima p: 61
Masukkan bilangan prima q: 53

Program akan menampilkan:

Public Key  (e, n) = (17, 3233)
Private Key (d, n) = (2753, 3233)

Untuk enkripsi:

Pilih menu: 1
Masukkan plaintext: halo

Untuk dekripsi:

Pilih menu: 2
Masukkan ciphertext: ...
Masukkan kunci privat d: ...
Masukkan nilai n: ...
