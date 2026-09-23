# Tugas 2 - Modularisasi

## File

- `app.py` menjadi titik masuk aplikasi dan menghubungkan CLI dengan storage.
- `domain/` berisi aturan validasi user dan interface sederhana untuk storage.
- `services/` berisi proses membuat dan mengambil data user.
- `adapters/` berisi penyimpanan data menggunakan file JSON.
- `cli.py` menangani input dan output pada terminal.
- `tests/` berisi test untuk setiap bagian aplikasi.
- `users.json` berisi contoh data user.

## Tujuan Refactoring

Starter project awalnya hanya terdiri dari satu file Python. Aturan validasi,
proses pembuatan user, penyimpanan JSON, serta input dan output terminal berada
di file yang sama. Project tersebut kemudian dipisahkan menjadi beberapa
module agar setiap bagian mempunyai tanggung jawab yang lebih jelas.

## Dependency Map Sebelum Refactoring

```text
app.py
|-- input dan output CLI
|-- aturan validasi user
|-- proses pembuatan user
`-- baca dan tulis file JSON
```

Semua bagian bergantung pada satu file. Akibatnya, perubahan pada penyimpanan
atau tampilan terminal dapat ikut memengaruhi aturan dan proses utama aplikasi.
Kode juga lebih sulit diuji karena proses pembuatan user langsung terhubung
dengan file dan input terminal.

## Dependency Map Sesudah Refactoring

```text
app.py
|-- adapters/file_storage.py
`-- cli.py
    |-- services/user_service.py
    |   |-- domain/rules.py
    |   `-- domain/ports.py
    `-- domain/ports.py
```

Setelah refactoring, dependency bergerak dari bagian luar menuju bagian inti.
`domain` tidak bergantung pada CLI atau file JSON. `user_service.py` juga tidak
mengetahui cara data disimpan karena hanya menggunakan interface `Loader` dan
`Saver` dari `domain/ports.py`. Implementasi file berada di adapter, kemudian
dipasangkan dengan CLI melalui `app.py`.

## Alasan Pembagian Module

- `domain/rules.py` dipakai khusus untuk aturan validasi nama dan email.
- `domain/ports.py` menjadi batas sederhana antara service dan storage.
- `services/user_service.py` mengatur pembuatan user, ID, email duplikat, dan
  pengambilan daftar user.
- `adapters/file_storage.py` menangani proses membaca dan menulis JSON.
- `cli.py` hanya menangani komunikasi dengan pengguna melalui terminal.
- `app.py` merangkai semua bagian tanpa menyimpan aturan bisnis.

Pembagian ini membuat fungsi lebih mudah dibaca dan diuji. Jika jenis storage
diganti, aturan domain dan service tidak perlu ikut diubah. Anggota kelompok
juga dapat mengerjakan module yang berbeda dengan risiko konflik yang lebih
kecil.

## Cara Menjalankan

Dari folder `tugas-2-monolitik`, jalankan aplikasi dengan perintah:

```bash
python3 app.py
```

Jalankan seluruh test dengan perintah:

```bash
python3 -m unittest discover -s tests -v
```

## Hasil Testing

Terdapat 9 test yang terdiri dari 3 test aturan domain, 3 test service, 2 test
file storage, dan 1 test CLI. Test domain dan service menggunakan data di
memori, sedangkan test storage memakai folder sementara agar tidak mengubah
`users.json`. Seluruh test berhasil dijalankan.

## Refleksi

Dari tugas ini kami belajar bahwa modularisasi bukan hanya memindahkan fungsi
ke file yang berbeda. Kami juga perlu memperhatikan arah dependency agar
aturan utama tidak bergantung pada bagian teknis seperti terminal dan file
JSON. Interface `Loader` dan `Saver` membantu service menggunakan storage tanpa
mengetahui detail penyimpanannya.

Bagian yang paling terasa adalah saat testing. Test setiap module sempat lulus
ketika dijalankan sendiri, tetapi test penuh menemukan bahwa hasil dari service
belum memiliki `id` yang dibutuhkan oleh CLI. Setelah kontrak keduanya
disamakan, seluruh 9 test dapat lulus. Dari masalah tersebut kami memahami
bahwa test per module penting untuk mencari kesalahan secara cepat, sedangkan
test penuh tetap diperlukan untuk memastikan semua module dapat bekerja sama.

Tugas ini juga melanjutkan pembelajaran dari Tugas 1. Pada Tugas 1 kami
memperbaiki nama dan membagi fungsi agar lebih mudah dibaca. Pada Tugas 2 kami
menerapkan prinsip yang sama dalam lingkup project dengan membagi kode
berdasarkan tanggung jawabnya.
