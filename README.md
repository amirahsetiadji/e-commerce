## TUGAS 2
# SweetBites Bakery

Proyek ini adalah platform e-commerce yang dibuat menggunakan Django, memungkinkan pengguna untuk melihat dan membeli produk seperti kue dan pastry. Berikut adalah langkah-langkah implementasi proyek ini secara step-by-step, serta penjelasan mengenai konsep-konsep terkait Django, Git, dan ORM.

## Tautan Deployment
Aplikasi belum di-deploy di PWS

---

1. ## Implementasi Step-by-Step

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


## TUGAS 3
## Pertanyaan dan Jawaban

### 1. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Data delivery memungkinkan server mengirimkan data ke klien secara efisien, menjaga aplikasi tetap dinamis dan interaktif tanpa perlu memuat ulang halaman.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON lebih baik untuk aplikasi modern karena lebih ringan, mudah dibaca, dan diproses oleh browser, sementara XML lebih kompleks.

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
`is_valid()` memeriksa apakah data yang dimasukkan ke dalam form sesuai dengan aturan yang telah ditetapkan. Ini penting untuk validasi sebelum menyimpan data ke database.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` mencegah serangan CSRF. Tanpa itu, penyerang bisa memaksa pengguna yang telah login untuk mengirim permintaan tanpa sepengetahuan mereka.

## Screenshot Postman
## Screenshot Hasil XML

![Screenshot 1](images/Screenshot1.png)

![Screenshot 2](images/Screenshot2.png)

## SCreenshot Hasil JSON

![Screenshot 1](images/Screenshot3.png)

![Screenshot 2](images/Screenshot4.png)


## TUGAS 4
### 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?
`HttpResponseRedirect()` dan `redirect()` adalah dua fungsi yang digunakan untuk mengarahkan ulang pengguna ke URL tertentu, tetapi ada sedikit perbedaan cara penggunaannya. `HttpResponseRedirect()` memerlukan URL secara eksplisit sebagai argumen. Sebaliknya, `redirect()` adalah fungsi yang lebih fleksibel karena dapat menerima URL, nama view, atau objek model sebagai argumen. `redirect()` akan menentukan URL berdasarkan argumen yang diberikan dan secara internal menggunakan `HttpResponseRedirect()` untuk melakukan pengalihan.

### 2. Jelaskan cara kerja penghubungan model Product dengan User!
Penghubungan model `Product` dengan `User` biasanya dilakukan menggunakan relasi *foreign key* dalam Django. Pada model `Product`, kita dapat menambahkan `ForeignKey` yang merujuk ke model `User` sebagai pemilik produk atau pengguna yang membuat produk tersebut. Misalnya:
```python
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField()
    category = models.CharField(max_length=100)
    customizable = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
```
Relasi ini memungkinkan setiap produk dikaitkan dengan pengguna tertentu, dan dengan `on_delete=models.CASCADE`, jika pengguna dihapus, produk yang mereka buat juga akan dihapus.

### 3. Apa perbedaan antara authentication dan authorization, apakah yang dilakukan saat pengguna login? Jelaskan bagaimana Django mengimplementasikan kedua konsep tersebut.
- **Authentication** adalah proses memverifikasi identitas pengguna, misalnya dengan mengecek username dan password saat login. 
- **Authorization** adalah proses pengecekan apakah pengguna yang sudah terverifikasi memiliki izin untuk mengakses sumber daya tertentu.

Saat pengguna login, proses **authentication** dilakukan untuk memastikan pengguna memiliki kredensial yang benar. Django mengelola proses ini melalui `django.contrib.auth`, di mana `authenticate()` digunakan untuk memeriksa kredensial, dan `login()` untuk mencatat sesi pengguna.

**Authorization** dalam Django diimplementasikan dengan memeriksa izin pengguna, misalnya dengan menggunakan dekorator seperti `@login_required` atau metode `has_perm()` untuk memeriksa apakah pengguna memiliki akses ke tindakan tertentu.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan?
Django mengingat pengguna yang telah login dengan menggunakan **session cookies**. Ketika pengguna berhasil login, Django menyimpan sesi pengguna di server dan cookie yang terkait dengan sesi tersebut dikirim ke browser pengguna. Cookie ini berisi informasi yang memungkinkan Django untuk mengidentifikasi sesi pengguna di setiap permintaan selanjutnya.

**Kegunaan lain dari cookies** meliputi:
- Menyimpan preferensi pengguna, seperti pengaturan bahasa atau tema.
- Melacak keranjang belanja dalam aplikasi e-commerce.

Namun, **tidak semua cookies aman**. Cookie yang tidak dienkripsi atau diberi atribut keamanan (seperti `HttpOnly` dan `Secure`) rentan terhadap serangan seperti pencurian cookie. Oleh karena itu, sangat penting untuk memastikan cookie yang berisi informasi sensitif dienkripsi dan aman.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Berikut jawaban terakhir yang sesuai dengan file HTML dan proses yang Anda lampirkan:

### 9. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

Berikut langkah-langkah yang saya lakukan secara mandiri untuk menyelesaikan tugas ini:
1. **Membuat Form Registrasi**:
   - Saya membuat form registrasi menggunakan `UserCreationForm` dari Django. View `register` menangani pembuatan akun pengguna baru dan setelah pendaftaran berhasil, pengguna akan diarahkan ke halaman login. Saya menggunakan template `register.html` untuk menampilkan form registrasi ini, serta `messages.success` untuk memberikan notifikasi setelah pengguna berhasil membuat akun.

2. **Membuat Fungsi Login**:
   - Fungsi `login_user` menangani autentikasi pengguna yang mencoba login. Di dalam view ini, saya menggunakan `AuthenticationForm` untuk memvalidasi form login. Jika valid, saya menggunakan `login(request, user)` untuk mencatat sesi pengguna yang sedang login, dan mengarahkan pengguna ke halaman utama menggunakan `HttpResponseRedirect(reverse("main:show_main"))`. Template `login.html` digunakan untuk menampilkan form login.

3. **Membuat Fungsi Logout**:
   - Fungsi `logout_user` menangani proses logout. Ketika pengguna logout, sesi pengguna dihapus dengan `logout(request)` dan cookie `last_login` juga dihapus menggunakan `response.delete_cookie('last_login')`. Setelah itu, pengguna diarahkan kembali ke halaman login dengan `redirect()`.

4. **Restriksi Akses Halaman**:
   - Saya menambahkan dekorator `@login_required` pada view `show_main` untuk memastikan hanya pengguna yang sudah login yang dapat mengakses halaman utama. Jika pengguna belum login, mereka akan diarahkan ke halaman login.

5. **Menghubungkan `Product` dengan Pengguna**:
   - Saya menambahkan foreign key `User` pada model `Product` sehingga setiap produk yang dibuat dapat diasosiasikan dengan pengguna yang membuatnya. Saya juga memodifikasi form di `create_product.html` agar produk yang ditambahkan terkait dengan pengguna yang sedang login dengan menyimpan `product.user = request.user` sebelum memanggil `product.save()`.

6. **Menggunakan Cookie `last_login`**:
   - Setelah pengguna berhasil login, saya menyimpan waktu terakhir mereka login di cookie bernama `last_login`. Cookie ini di-set menggunakan `response.set_cookie('last_login', str(datetime.datetime.now()))` dan ditampilkan di halaman utama setelah login. Jika pengguna logout, cookie ini akan dihapus. Cookie `last_login` ini ditampilkan di halaman `main.html`.

7. **Menerapkan Deployment dan Versi Kontrol Git**:
   - Setelah menyelesaikan seluruh fitur, saya melakukan migrasi dengan `python manage.py makemigrations` dan `python manage.py migrate`. Kemudian saya melakukan add, commit, dan push ke GitHub dengan perintah Git. Setelah itu, saya mengonfigurasi `settings.py` untuk deployment di PWS dengan menyesuaikan `ALLOWED_HOSTS` dan melakukan `git push pws main` untuk mempublikasikan aplikasi.

Dengan langkah-langkah ini, saya berhasil mengimplementasikan autentikasi, session, cookie, serta pengelolaan produk dalam aplikasi Django secara mandiri, sesuai dengan checklist yang diberikan.