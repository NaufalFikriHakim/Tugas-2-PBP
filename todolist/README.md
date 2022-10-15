# Tugas 4
Link Website: https://tugas-2-pbp-naufalfikrihakim.herokuapp.com/todolist
## Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
CSRF atau cross-site request forgery berguna untuk melindungi web dari serangan CSRF. Token ini bernilai unik dan acak yang membuat peretas sulit untuk menebak nilai dari token ini. Token ini di-generate seriap user melakukan sesi. Jika tidak terdapat token itu, maka peretas dapat mendapatkan nilai yang kita masukan kedalam form.
## Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
Kita dapat membuat elemen <form> secara manual dengan menggunakan tag <input><\input>
## Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
Disaat form diisi oleh user dan tombol untuk submit di klik, data akan dicocokan dengan fungsi yang terdapat pada views.py dan kemudian akan dibuat objek dari models.py dan disimpan ke dalam database
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Buat aplikasi baru dengan menjalankan python manage.py startapp todolist dan masukkan nama startapp kedalam setting.py
2. Menambahkan path yang dibutuhkan kedalam urls.py
3. Membuat model di models.py yang memiliki nama Task dan memiliki attribute yang dibutuhkan sesuai dengan soal
4. Membuat form registrasi, login, dan logout dan menyimpan hasilnya
5. Membuat templates untuk ditampilkan
5. Menambahkan urlpatterns sesuai soal
6. Melakukan deployment dan memasukkan 2 akun pengguna
Username = naufal, password = Haha7214
Username = fikri, password = Haha7214
# Tugas 5
## Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
| | Inline | Internal | External |
|-|--|--|--|
|Perbedaan|Style hanya diaplikasikan pada 1 elemen saja|Styling oleh CSS berada pada file html yang sama| Styling oleh CSS berada pada file tersendiri
|Kelebihan|Mempermudah modifikasi elemen yang spesifik|Mempermudah styling pada html yang mencakup 1 halaman| Styling dapat dilakukan secara global dengan mudah
|Kekurangan|Tidak efisien karena bisa saja menulis kode yang sama berulang kali| Tidak efisien ketika ingin menggunakan style yang sama di beberapa file| Tampilan html akan rusak apabila styling yang kita lakukan gagal


## Jelaskan tag HTML5 yang kamu ketahui.
1. `<a>` Tag untuk mendefinisakn hyperlink
2. `<b>` Tag untuk menampilkan text secara bold
3. `<body>` Tag untuk mendefinisikan body dari html
4. `<br>` Tag untuk membuat satu baris kosong
5. `<button>` Tag untuk membuat tombol
6. `<div>` Tag untuk memberi batas bagian
7. `<form>` Tag untuk meminta input
8. `<head>` Tag untuk mendefinisikan bagian head dari html
9. `<html>` Tag untuk mendefinisikan root
10. `<style>` Tag untuk mengatur tampilan

## Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. Selektor Universal (*), akan memilih semua elemen 
2. Selektor Tag, akan memilih elemen yang sesuai dengan tag
3. Selektor ID, akan memilih elemen berdasarkan ID
4. Selektor Class (didahului .), akan memilih elemen berdasarkan class yang dipilih

## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Masukkan <link> bootstrap kepada base.html
2. Menerapkan style dan bootstrap kepada halaman login, register, create-task, dan todolist
3. Menerapkan efek ketika cards di halama todolist di hover
4. Membuat keempat halaman responsif dengan memasukkan media query pada base.html
5. Melakukan push dan deploy kepada heroku
