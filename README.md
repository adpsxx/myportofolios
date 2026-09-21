# Deskripsi
Website ini adalah website portfolio personal menggunakan framework Django yang menampilkan profil, pengalaman volunteer/organisasi, dan beberapa proyek yang sudah saya buat. Website ini menerapkan model MTV (Model-Template-View) yang memisahkan secara jelas antara pengelolaan data, logika alur aplikasi, dan interface. Selain menerapkan arsitektur MTV, website ini juga mengimplementasikan mekanisme form dan data delivery untuk memfasilitasi interaksi yang lebih efisien.

website url: andranu-dhawy-myportofolio.pws.cs.ui.ac.id

# Struktur Program
```text
myportofolios/
├── manage.py                 
├── requirements.txt           
├── .env                       
├── .env.prod                  
├── .gitignore
│
├── portofolio/                
│   ├── settings.py            
│   ├── urls.py                
│   ├── wsgi.py                
│   └── asgi.py                
│
├── main/                      
│   ├── models.py              
│   ├── views.py              
│   ├── urls.py               
│   ├── forms.py              
│   ├── admin.py               
│   └── tests.py               
│
├── templates/                 
│   ├── base.html              
│   ├── index.html            
│   ├── experience.html        
│   ├── experiences_form.html  
│   ├── experiences_edit_form.html
│   ├── project.html           
│   ├── projects_form.html     
│   ├── project_edit_form.html
│   └── components/
│       ├── experience_delete_modal.html
│       └── project_delete_modal.html
│
└── static/                   
    ├── css/style.css          
    └── img/        
```           

# Setup Instruction
1. Clone repository Github
```bash
git clone https://github.com/adpsxx/myportofolios.git
cd myportofolios
```

2. Aktifkan Virtual Environment

Windows:
```bash
python -m venv env
env\Scripts\activate
```

Linux/macOS:
```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependensi yang diperlukan
```bash
pip install -r requirements.txt
```

4. Konfigurasi environment variable. Buat file .env di root proyek:
```env
PRODUCTION=False
```

5. Jalankan migrasi database
```bash
python manage.py makemigrations
python manage.py migrate
```
5. Jalankan delopment server
```bash
python manage.py runserver
```

6. Buka browser dan akses: 
http://127.0.0.1:8000/

# Weekly Progress
## Week 0
- Setup git repositori dan instalasi Django.

## Week 1
- Inisiasi projek awal.
- Merancang halaman utama website menggunakan HTML dan CSS.
- Menggunakan bootstrap sebagai navbar.
- Deploy website ke PWS.

## Week 2
- Implementasi MVT (Mode-View-Template) website.
- Membuat model untuk "Experience" dan "Project".
- Membuat masing-masing page untuk menampilkan "Experience" dan "Project".

## Week 3
- Implementasi Form dan Data Delivery pada website.
- Menggunakan Form dan Data Delivery untuk menambah, mengedit, dan menghapus data pada model.

### Tugas 1
1. Saya tidak menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside> dalam merancang dan membuat website portofolio ini. Berdasarkan sumber yang saya baca di internet, elemen-elemen semantik tersebut digunakan untuk menambah readability kode dan juga menambah aksesibilitas bagi pembaca. Menggunakan atau tidak menggunakan elemen-elemen semantik tersebut tidak akan mengubah fungsionalitas website, karena kita masih bisa meggunakan <div> sebagai penggantinya.

Meskipun saya tidak menggunakan elemen-elemen semantik tersebut di website saya, saya tetap menggunakan <div> dengan rapih agar readability kode saya masih dapat dijaga. 

2. Tantangan yang saya dapatkan adalah ketika ada elemen yang tidak mau berubah dan bergerak posisinya meskipun kita sudah mengubah CSS nya. Setelah saya pelajari lebih lanjut, hal tersebut disebabkan oleh elemen yang berada pada suatu container (div) dan membatasi pergerakannya. Solusi yang saya dapatkan adalah dengan mengubah CSS untuk container luar terlebih dahulu (seperti menambah tinggi dan lebar) agar elemen-elemen didalamnya dapat kita ubah posisinya. 

Saat mengubah tampilan dari desktop ke mobile, elemen yang diprioritaskan adalah nama dan foto profil. Hal tersebut disebabkan karena ukuran mereka yang sangat besar pada tampilan desktop. Jika ukuran mereka tidak mengecil seiring mengecilnya layar, layar tidak akan cukup untuk menampilkan seluruh nama dan foto profil secara utuh dan rapih.

3. Website static adalah website yang dimana isinya akan identik dan sama persis dengan yang tersimpan. Sedangkan pada website dengan fungsionalitas dinamis, isi dari website dapat berubah dan diperbarui tanpa mengubah strukturnya akibat pemrosesan data terlebih dahulu melalui server.

Batasan yang saya rasakan pada website statis ini adalah mengubah isi dari website memerlukan waktu dan effort yang lumayan besar. Misalkan saya ingin menambah atau mengubah deskripsi saya, saya harus mengubah kode HTML dan CSS saya, lalu men-deploy-nya ulang. Saya ingin menambahkan fungsionalitas dinamis seperti opsi untuk mengubah isi website saya tanpa harus mengubah kode HTML/CSS dan men-deploy ulang.

AI Disclosure:
Saya menggunakan AI dengan model Gemini 3.8 Flash untuk membantu saya dalam pengerjaan Tugas Individu 1. 
Saya menggunakan AI untuk membantu saya dalam mengintegrasikan fitur-fitur bootstrap (seperti icon dan navbar) dan juga untuk memperbaiki beberapa layout/tampilan elemen dari website saya.
Saya juga menggunakan AI untuk meminta inspirasi untuk desain website saya.

chat log:
https://share.gemini.google/kjSPSM4bpVzj

### Tugas 2
1. Saat pengguna membuka tampilan halaman portofolio, pengguna mengetik URL dari web portofolio, yang kemudian mengirimkan request ke server. Pada proyek, urls.py menerima request tersebut, membaca URL, lalu mencocokannya untuk diteruskan menuju urls.py pada aplikasi. Setelah itu, urls.py pada aplikasi akan mencocokkan URL tersebut kembali untuk diteruskan dengan tampilan sesuai dengan URL yang diberikan. Komponen view yang berada sesuai dengan alamat URL tersebut akan mengambil data dari model. Data yang sudah terkumpul oleh model kemudian akan diteruskan pada view yang kemudian akan diteruskan pada template. Template menggabungkan struktur HTML dengan data tersebut lalu membentuk struktur visual yang akan ditampilkan. Template lalu dikirimkan kembali oleh server kepada pengguna sehingga pengguna dapat melihat tampilan web yang sudah jadi.

2. Penyimpanan data sebaiknya dituliskan pada model ketimbang langsung pada template untuk memudahkan dalam penambahan dan penghapusan data yang ada di dalamnya. Hal tersebut juga sesuai dengan prinsip Separation of Concerns (SoC), yaitu memisahkan program kedalam beberapa bagian, dan setiap bagian tesebut memiliki tugasnya masing-masing.

Menyimpan data pada model dan memisahkannya dari template sangat membantu dalam pengembangkan dan memelihara web kita. Misalnya ketika ingin menambah data proyek baru pada portfolio, kita cukup menambah data pada database melalui model tanpa perlu mengubah kode HTML sama sekali. Hal ini juga mempersingkat dan menambah readability kode karena kita tidak perlu menuliskan data satu persatu pada template. Tidak hanya itu, menyimpan data pada model juga mempermudah kita jika web kita ingin diintegrasikan dengan platform lain. Data pada model dapat diexport dalam format JSON jika web kita ingin diakses melalui aplikasi mobile.

3. Fungsi makeimigrations berfungsi untuk membuat file blueprint untuk perubahan database yang kita lakukan. Sedangkan fungsi migrate berfungsi untuk mengeksekusi dan melakukan perubahan pada database sesuai dengan file tersebut, bisa berupa penambahan maupun penghapusan. 

Kedua fungsi tersebut tidak wajib untuk dijalankan secara bersamaan, tergantung dengan kondisi yang ingin kita lakukan. Misalkan jika kita ingin menambah suatu field baru pada model, kita harus menjalakan fungsi makeimigrations untuk merekam perubahan lalu menjalankan fungsi migrate agar field baru tersebut dapat benar-benar ditambahkan pada database.

AI Disclosure:
Saya menggunakan AI dengan model Gemini 3.8 Flash dan Claude Sonnet 5 untuk membantu saya dalam pengerjaan Tugas Individu 2. 
Penggunaan AI yang saya lakukan kebanyakan untuk membantu saya dalam mengatur desain, seperti cara memindahkan dan mengubah posisi objek.
Saya juga menggunakan AI untuk membantu saya untuk lebih mengerti mengenai syntax CSS.
Strategi saya dalam melakukan prompting adalah dengan menanyakan pertanyaan saya lalu mengkonfirmasi pemahaman saya kembali pada AI tersebut. 

Chat log:
https://claude.ai/share/376c9a5e-2edd-401e-b1fe-70eca23b3dac
https://share.gemini.google/XP0GkGhm3LFB
https://share.gemini.google/gOkQZTMmPLcz

### Tugas 3
#### 1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!

    ModelForm digunakan karena dapat menghubungkan form HTML secara langsung dengan Model Django. 
    Dengan ModelForm, kita tidak perlu mendefinisikan setiap field form secara manual karena masing-masing field dapat dibuat berdasarkan field yang sudah ada pada model. 
    Hal tersebut mengurangi jumlah kode, memudahkan penyimpanan data, dan mempermudah validasi data yang dimasukkan.

    {% csrf_token %} digunakan untuk menjaga agar form kita tidak diakses oleh pihak asing yang tidak memiliki akses atau yang dinamakan oleh serangan Cross-Site Request Forgery (CSRF). 
    Tanpa adanya {% csrf_token %}, pihak lain dapat mengirim request ke website kita dan memanipulasi atau menghapus data pada website. 
    {% csrf_token %} berperan sebagai validator yang memastikan bahwa setiap request yang diterima website memang berasal dari form yang sah.

#### 2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?

    JSON lebih banyak digunakan pada pengembangan aplikasi web modern karena JSON yang memiliki sintaks yang lebih sederhana sehingga lebih mudah dibaca oleh manusia dan juga diproses oleh program. 
    Struktur data yang digunakan pada JSON juga sudah tersedia pada bahasa pemrograman backend seperti Python (menggunakan dictionary). 
    Sedangkan XML menyimpan semua data sebagai teks murni dan elemen/atribut, sehingga memerlukan langkah konversi tipe data tambahan.

#### 3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?

    Saat menggunakan fungsi view untuk mengembalikan data portofolio dalam bentuk JSON, alurnya secara umum adalah:
    1. Browser mengirim request ke URL tertentu
    2. urls.py menerima dan mencocokkan request tersebut dan mengarahkannya ke fungsi view yang sesuai.
    3. View mengambil data dari model.
    4. Data yang diperoleh masih dalam bentuk suatu objek, sehingga belum bisa dikirim.
    5. Dilakukan serialization, yaitu mengubah objek tersebut menjadi format data yang dapat direpresentasikan, yaitu sebagai JSON.
    6. View mengembalikan data yang sudah dalam format JSON tersebut.
    7. Browser menerima data dan menampilkannya.

    Serialization diperlukan karena model Django tidak menggunakan format JSON secara langsung, alih-alih dalam bentuk objek. 
    Serilization bertugas untuk mengkonversi data dari objek menjadi format yang dapat dikirim dan dimengerti oleh client, yaitu JSON. 
    Jika tidak ada serilization, data tidak tersebut menjadi tidak valid karena tidak bisa dibaca oleh server.

#### AI DISCLOSURE (Tugas 3)
    Pada tugas individu 3 ini, saya menggunakan AI dengan model Gemini 3.8 Flash untuk membantu saya dalam mengerjakan tugas.
    Penggunaan AI yang saya lakukan kebanyakan untuk membantu dalam menyusun desain dan layout (seperti memindahkan letak objek).
    Saya juga menggunakan AI untuk menanyakan beberapa konsep yang saya kurang pahami mengenai Form dan Data Delivery.
    Dalam penggunaan AI, saya kebanyakan hanya meminta AI untuk meminta cara/contoh dari program, tidak langsung meminta jawaban akhir.  

    chat log:
    https://share.gemini.google/TqlgE5cWlofv
    https://share.gemini.google/ZqF4iKFeL6f9
