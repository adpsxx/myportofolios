Nama: Andranu Dhawy Purditya

NPM: 2506584893

Kelas: PBP D

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