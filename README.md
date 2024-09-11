# SweetBites Bakery

Proyek ini adalah platform e-commerce yang dibuat menggunakan Django, memungkinkan pengguna untuk melihat dan membeli produk seperti kue dan pastry. Berikut adalah langkah-langkah implementasi proyek ini secara step-by-step, serta penjelasan mengenai konsep-konsep terkait Django, Git, dan ORM.

## Tautan Deployment
Aplikasi belum di-deploy di PWS

---

## Implementasi Step-by-Step

1. **Membuat Proyek Django**:
   - Saya memulai proyek Django baru menggunakan perintah `django-admin startproject e-commerce`. Perintah ini membuat struktur proyek dasar yang mencakup `settings.py`, `urls.py`, dan beberapa file konfigurasi lainnya.

2. **Membuat Aplikasi Utama**:
   - Di dalam proyek, saya membuat aplikasi bernama `main` dengan perintah `python manage.py startapp main`. Aplikasi ini digunakan untuk mengelola data produk dan halaman untuk toko roti (bakery).

3. **Mendefinisikan Model Product**:
   - Di dalam `models.py`, saya membuat model `Product` dengan field seperti `name`, `price`, `description`, `stock`, `category`, dan `customizable`. Model ini digunakan untuk merepresentasikan data produk di dalam database.

4. **Migrasi**:
   - Setelah mendefinisikan model, saya menjalankan perintah `python manage.py makemigrations` untuk membuat skema database berdasarkan model yang sudah dibuat, dan `python manage.py migrate` untuk menerapkan perubahan tersebut ke database.

5. **Membuat Views dan Template**:
   - Saya membuat fungsi `product_list` di `views.py` yang mengambil semua data produk dari database dan menampilkannya di file template `main.html`. View ini mengirimkan data konteks (seperti daftar produk, nama, dan kelas saya) ke template untuk ditampilkan.

6. **Routing URL**:
   - Di dalam `urls.py`, fungsi view yang sesuai akan dipanggil, dan halaman yang benar akan ditampilkan.

7. **Deployment ke PWS**:
   - Setelah aplikasi selesai, saya melakukan deployment ke PWS dengan menambahkan URL deployment di `ALLOWED_HOSTS` pada file `settings.py` dan menjalankan perintah `git push pws main` untuk mem-push kode saya ke PWS.

---

## Bagan Request-Response Django

Berikut adalah bagan alur request client ke aplikasi Django beserta responsnya:
Client Request -> urls.py -> views.py -> models.py (optional) -> templates HTML -> Client Response


Penjelasan:
- **urls.py**: Berfungsi untuk memetakan URL yang diminta oleh client ke fungsi yang sesuai di `views.py`.
- **views.py**: Mengambil data (jika diperlukan, melalui `models.py`), memproses logika aplikasi, dan mengembalikan hasil ke template HTML.
- **models.py**: Berfungsi sebagai ORM untuk berinteraksi dengan database, misalnya untuk mengambil atau menyimpan data produk.
- **HTML template**: Menampilkan data yang sudah diambil dan diproses dari views ke halaman web yang dilihat oleh pengguna.

---

## Penjelasan Mengenai Git

Git adalah sistem pengontrol versi (version control system) yang sangat berguna dalam pengembangan perangkat lunak. Dengan Git, kita dapat melacak setiap perubahan yang dilakukan pada kode, memungkinkan rollback ke versi sebelumnya jika ada kesalahan, serta memungkinkan kolaborasi dengan tim pengembang lain. Fitur seperti branch dan merge sangat membantu dalam mengelola berbagai fitur dan bug fix secara paralel.

---

## Mengapa Django Dipilih Sebagai Framework Awal?

Django sering dipilih sebagai framework awal untuk pembelajaran pengembangan perangkat lunak karena sifatnya yang "batteries included," yang berarti Django sudah menyediakan banyak fitur bawaan seperti ORM, admin panel, sistem autentikasi, dan routing yang memudahkan pengembang pemula. Django juga menggunakan pola arsitektur yang jelas (MVT - Model-View-Template), yang membantu memahami alur kerja aplikasi web secara terstruktur.

---

## Mengapa Model pada Django Disebut Sebagai ORM?

ORM (Object-Relational Mapping) pada Django memungkinkan pengembang untuk berinteraksi dengan database menggunakan objek Python, tanpa harus menulis query SQL secara langsung. Setiap model Django merepresentasikan tabel dalam database, dan kita dapat melakukan operasi CRUD (Create, Read, Update, Delete) menggunakan metode Python yang sederhana. ORM mengabstraksi interaksi dengan database sehingga lebih mudah dipahami dan digunakan oleh pengembang.


