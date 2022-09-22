# Tugas 3
Link website:
## Perbedaan antara JSON, XML, dan HTML
JSON adalah turunan JavaScript yang digunakan dalam transfer dan penyimpanan data. Kekinian, bahasa ini sering dimanfaatkan dalam pembuatan aplikasi web. XML adalah Extensible Markup Language yang digunakan untuk menyederhanakan pertukaran dan penyimpanan data. HTML adalah bahasa standar pemrogaman yang digunakan untuk membuat halaman website, yang diakses melalui internet. JSON dan XML sama-sama digunakan untuk pengiriman data, namun perbedaan mereka terdapat pada penulisan syntax. Sedangkan, HTML bertujuan untuk menampilkan data yang disimpan kepada user.
## Pentingnya data delivery dalam pengimplemantasian sebuah platform
Data delivery sangat dibutuhkan dalam pengembangan sebuah platform. Data delivery digunakan untuk proses pengiriman data. Proses pengiriman data tersebut dilakukan oleh satu user ke user lainnya.
## Implementasi
1. Membuat aplikasi bari mywatchlist dengan comman `python manage.py startapp mywatchlist`
2. Melakukan routin pada file `project_django/urls.py` dengan menambahkan `path('mywatchlist/', include('mywatchlist.urls'))` pada `urlpatterns`. Lalu, lakukan routing pula pada `mywatchlist/urls.py` sesuai path yang diminta.
3. Membuat model MyWatchList pada `mywatchlist/models.py` dengan fiels yang telah ditentukan pada soal
4. Membuat fungsi show_watchlist, show_xml, dan show_json pada `mywatchlist/views.py` untuk menampilkan data dengan format yang benar
5. Lakukan mikrasi model dengan menjalankan `python manage.py makemigrations` dan `python manage.py migrate`
## Postman
### HTML
![Screenshot 2022-09-22 095612](https://user-images.githubusercontent.com/94209114/191658480-7067b53f-4de8-4f3e-b54b-88df17ac569c.jpg)
### JSON
![Screenshot 2022-09-22 095640](https://user-images.githubusercontent.com/94209114/191658501-f925c825-2db1-4775-81de-5a22570d67e8.jpg)
### XML
![Screenshot 2022-09-22 095703](https://user-images.githubusercontent.com/94209114/191658532-9f010979-ea6f-4ddc-8e71-97691408bc77.jpg)
