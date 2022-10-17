# TUGAS 6
## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
Synchronous Programming berarti program berjalan secara sekuensial. Program dijalankan baris perbaris, apabila suatu baris membutuhkan suatu nilai dari baris sebelumnya, makan baris tersebut akan benar-benar menunggu hingga baris sebelumnya selesai dieksekusi. Sedangkan asynchronous programming adalah program yang dapat berjalan secara bersamaan tanpa menunggu proses antrian. Biasanya program yang menggunakan asynchronous programming berjalan lebih cepat daripada programn yang menggunakan synchronous programming.
## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
Event-Driven Programming adalah suatu paradigma programming dimana alur dari program ditentukan oleh event-event seperti user actions(mouse clicks, key presses), sensor outputs, atau message passing dari program lain. Penerapan pada tugas kali ini adalah saat button ditekan, makan program akan mengirimkan data task baru.
## Jelaskan penerapan asynchronous programming pada AJAX.
Salah satu penerapannya terdapat pada saat button tambah task ditekan. pada saat button tambah task ditekan, AJAX POST akan digunakan.
## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat fungsi bernama `show_json` dan `add_task` di views
2. Melakukan routing `show_json` dan add_task di `urls.py`
3. Membuat <script> di `todolist.html` untuk membuat card lalu mengarahkannya ke fungsi `add_task` untuk membuat object task baru dan mereturn hasil POST
4. Melakukan request GET ke `todolist/json` lalu map ke data. Setiap iterasi akan menambahkan card sehingga dapat muncul pada halaman
5. Membuat modal untuk membuat card baru dan membuat fungsi POST yang akan berjalan saat button `Tambah Task` diklik. Apabila POST sukses, data akan ditambah dengan card yang baru dibuat.
