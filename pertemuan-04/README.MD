# Pertemuan 4 — Metadata dan Interoperabilitas

## Identitas sumber
- Judul: Dasar-Dasar Pemrograman 1 dengan Python
- Pembuat: Dr. Fariz Darari
- Deskripsi: Mata kuliah terbuka tingkat dasar yang membahas konsep dasar pemrograman menggunakan Python. Materinya meliputi komputer dan pemrograman, variabel dan tipe data, sistem bilangan, percabangan, perulangan, string, fungsi, struktur data, rekursi, pemrograman berorientasi objek, pewarisan, dan GUI.
- Tanggal: 2020
- Jenis: LearningResource
- Bahasa: id
- Hak: Hak cipta Universitas Indonesia / UI OpenCourseware; lisensi spesifik tidak dicantumkan pada halaman sumber.
- URI sumber: https://ocw.ui.ac.id/course/view.php?id=142

## Pemetaan Dublin Core Terms

| Properti | Nilai | Alasan pemilihan |
| --- | --- | --- |
| dcterms:title | Dasar-Dasar Pemrograman 1 dengan Python | Digunakan untuk mencatat nama resmi sumber belajar agar mudah dikenali. |
| dcterms:creator | Dr. Fariz Darari | Digunakan untuk mencatat pengajar atau pembuat materi yang tercantum pada informasi mata kuliah. |
| dcterms:publisher | Universitas Indonesia — UI OpenCourseware | Digunakan untuk mencatat institusi dan platform yang menyediakan sumber belajar secara daring. |
| dcterms:description | Mata kuliah terbuka tingkat dasar yang membahas konsep dasar pemrograman menggunakan Python, meliputi variabel, tipe data, percabangan, perulangan, fungsi, struktur data, rekursi, dan pemrograman berorientasi objek. | Digunakan untuk memberikan ringkasan isi dan cakupan sumber kepada pengguna. |
| dcterms:created | 2020 | Digunakan untuk menyatakan tahun acuan pembuatan atau penyelenggaraan materi mata kuliah. |
| dcterms:type | LearningResource | Digunakan untuk menunjukkan bahwa sumber ini merupakan materi atau sumber pembelajaran, bukan satu artikel atau dokumen biasa. |
| dcterms:language | id | Digunakan untuk menyatakan bahwa bahasa utama sumber adalah bahasa Indonesia. |
| dcterms:rights | Hak cipta Universitas Indonesia / UI OpenCourseware; lisensi spesifik tidak dicantumkan pada halaman sumber. | Digunakan untuk menjelaskan status hak penggunaan sumber tanpa mengklaim lisensi yang tidak tercantum. |


## Hasil validasi
- JSON-LD Playground: Validasi berhasil tanpa galat (error) sintaks. Pada tampilan N-Quads, URI subjek yang dihasilkan (`<https://ocw.ui.ac.id/course/view.php?id=142>`) sudah sama dan selaras dengan URI subjek yang ada pada file Turtle.
- Schema Markup Validator: Validasi berhasil dengan hasil 0 ERRORS dan 0 WARNINGS setelah melakukan perbaikan pada properti `license` (yang awalnya teks biasa) diubah menjadi `copyrightNotice` agar sesuai dengan standar skema.

## Refleksi
1. Mengapa URI yang sama penting untuk Turtle dan JSON-LD?
URI bertindak sebagai identitas unik global. Menggunakan URI yang sama memastikan bahwa mesin atau aplikasi mengenali kedua file tersebut sedang mendeskripsikan satu entitas/sumber belajar yang persis sama, meskipun ditulis dengan format bahasa yang berbeda (interoperabilitas).

2. Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?
DC Terms (Dublin Core) berperan sebagai kosakata standar yang umum digunakan untuk mendeskripsikan properti dasar suatu karya (seperti pembuat, judul, tanggal) pada web semantik (seperti di file Turtle). Sementara itu, schema.org adalah kosakata yang secara spesifik dirancang dan distandarisasi untuk membantu mesin pencari (seperti Google) memahami struktur konten halaman web agar bisa ditampilkan sebagai *rich snippet*.

3. Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.
Risiko utamanya adalah fragmentasi data atau kebingungan pada mesin pencari. Sistem akan menganggap informasi tersebut merujuk pada benda atau sumber yang berbeda-beda, yang pada akhirnya dapat merusak integrasi data (*Linked Data*) dan menurunkan kualitas pengindeksan di mesin pencari (SEO).

## Catatan akhir
Metadata pada HTML, Turtle, dan JSON-LD telah dipastikan konsisten. Ketiganya kini menggunakan URI subjek utama yang sama (`https://ocw.ui.ac.id/course/view.php?id=142`), serta menjaga elemen inti seperti judul, pembuat, dan deskripsi tetap selaras tanpa merubah maknanya di berbagai format representasi.
