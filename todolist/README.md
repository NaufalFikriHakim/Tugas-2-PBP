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
