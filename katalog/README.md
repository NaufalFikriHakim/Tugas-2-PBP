# Tugas 2 PBP
https://tugas-2-pbp-naufalfikrihakim.herokuapp.com/katalog/

## Bagan Request Client ke Web Aplikasi Berbasis Django
![Django Frameworks drawio](https://user-images.githubusercontent.com/94209114/190227175-6e35bf36-e783-4a9e-b4e3-3f1c7c5a06aa.png)

## Virtual Environment
Virtual environment berguna untuk menciptakan environment yang terpisah dari env lainnya. Sistem yang kita ciptakan akan berjalan pada suatu lingkungan yang terisolasi. Pengisolasian ini berguna untuk memisahkan dependency dari satu sisten terhadap sistem lainnya.

Kita tetap dapat membuat aplikasi web tanpa menggunakan virtual environment, namun terdapat kemungkinan terjadinya konflik antara depedency suatu projek terhadap depedency project lainnya

## Penjelasan Implementasi
### Implementasi fungsi pada ```views.py```
Di dalam file ini terdapat fungsi ```show_katalog(req)``` yang digunakan untuk mengambil semua data yang terdapat di ```CatalogItem``` dan melakukan rendering data tersebut pada template ```katalog.html```
### Implementasi routing pada```urls.py```
Pada file ini, kita menambahkan ```urlpatterns``` untuk memetakan request pada /katalog ke fungsi pada file ```views.py```
### Implementasi pemetaan data ke file HTML
Dengan memanfaatkan iterasi, kita dapat menampilkan semua data yang kita miliki kedalam file HTML. Kita dapat menggunakan Django template tags yang sesuai agar data dapat ditampilkan.
### Implementasi ```deployment``` ke Heroku
Yang harus kita lakukan untuk melakukan ```deployment``` adalah membuat aplikasi baru terlebih dahulu di Heroku, kemudian kita buat variabel secrets baru yang bernama ```HEROKU_APP_NAME``` yang terdapat pada secrets di github projek kita. Kemudian kita juga membutuhkan ```API_KEY``` yang terdapat di account kita di heroku yang kemudian nilai dari ```API_KEY``` tersebut kita simpan di variabel secrets baru yang bernama ```HEROKU_API_KEY``` yang juga terdapat pada secrets di github project kita. Dan langkah terakhir adalah me-run ulang job pada actions.
