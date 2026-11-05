# Pertemuan 9 - SPARQL Dasar: Tell & Ask dan Endpoint
## Langkah 1 – Tabel Binding

| Tahap | ?dosen | ?mk | ?namaMK |
|---|---|---|---|
| Pola 1, baris 1 | ex:budi | ex:tif2305 | – |
| Pola 1, baris lain | ex:sari | ex:tif2410 | – |
| Pola 1, baris lain | ex:sari | ex:tif2305 | – |
| Pola 2 | – | ex:tif2305 | "Web Semantik" |
| Pola 2 | – | ex:tif2410 | "Data Mining" |
| Hasil akhir | ex:budi | ex:tif2305 | "Web Semantik" |
| Hasil akhir | ex:sari | ex:tif2410 | "Data Mining" |
| Hasil akhir | ex:sari | ex:tif2305 | "Web Semantik" |

Jumlah baris hasil akhir : 3 baris

Peran `?mk` : berfungsi sebagai penghubung (join variable) antara Pola 1 dan Pola 2. Kedua pola digabungkan berdasarkan nilai `?mk` yang sama. Meskipun `?mk` tidak ditampilkan karena tidak dicantumkan dalam bagian `SELECT`, variabel tersebut tetap digunakan untuk mencocokkan data pada kedua pola di bagian `WHERE`.

---
<br><br>


## Langkah 2 – ASK dan Asumsi Terbuka

---

### 1. Apa hasil `ASK { ex:budi ex:mengajar ex:tif2410 }`? Bagaimana tafsir yang tepat menurut asumsi dunia terbuka?

* **Hasil:** `false` (salah) karena tripel tersebut tidak ditemukan di dalam grafik RDF yang ada. Berdasarkan data Langkah 1, `ex:budi` hanya mengajar `ex:tif2305`, sedangkan `ex:tif2410` diajar oleh `ex:sari`.
* **Tafsir Menurut Asumsi Dunia Terbuka (Open World Assumption - OWA):** 
  Dalam OWA, ketiadaan informasi di dalam basis pengetahuan **tidak berarti** bahwa informasi tersebut salah atau tidak pernah terjadi di dunia nyata. Hasil `false` hanya menunjukkan bahwa di dalam graf saat ini, fakta tersebut belum dinyatakan atau belum tercatat. Bisa jadi di dunia nyata Budi memang mengajar mata kuliah tersebut, tetapi data itu belum dimasukkan ke dalam sistem.

---

### 2. Berapa baris hasil `SELECT ?a ?b WHERE { ?a ex:mengajar ?mk . ?b ex:mengajar ?mk }`? Mengapa muncul baris dengan `?a` sama dengan `?b`?

* **Hasil:** Menghasilkan **5 baris** berdasarkan kombinasi pencocokan nilai `?mk` dari data `ex:mengajar` (yaitu mata kuliah `ex:tif2305` yang diajar oleh Budi & Sari, serta `ex:tif2410` yang diajar oleh Sari).
* **Mengapa muncul baris dengan `?a` sama dengan `?b`?**
  Variabel `?a` dan `?b` bersifat independen dalam pola kueri SPARQL tersebut. Ketika mesin kueri mencocokkan data, sebuah entitas (misalnya `ex:sari`) dapat berpasangan dengan dirinya sendiri pada variabel `?a` dan `?b` untuk mata kuliah yang sama (`ex:sari` dicocokkan ke `?a` dan `ex:sari` dicocokkan ke `?b`), sehingga menghasilkan baris refleksif di mana `?a` bernilai sama dengan `?b`.

---

### 3. Pola `?mk ex:nama "Web Semantik"` menghasilkan nol baris pada graf yang menulis `"Web Semantik"@id`. Jelaskan penyebabnya.

* **Penyebab:** Terjadi ketidakcocokan bentuk literal (*mismatch*) antara kueri yang dicari dengan data yang tersimpan di dalam graf:
  * Pola kueri mencari literal string polos tanpa penanda (*plain literal*), yaitu `"Web Semantik"`.
  * Sementara itu, data yang tersimpan di dalam graf menggunakan *language-tagged literal*, yaitu `"Web Semantik"@id` (memiliki tag bahasa `@id`). 
  Di dalam standar Semantic Web / RDF, literal dengan tag bahasa dianggap sebagai nilai yang berbeda secara ketat dari string polos, sehingga kueri gagal menemukan kecocokan dan menghasilkan nol baris.

---
<br><br>

## Langkah 3 - Query lokal
- IRI dasar graf: [https://vshndrr-code.github.io/web-semantik/251402019/usu#]
- Jumlah triple awal / akhir: [28] / [30]
- Fakta yang ditambahkan: [ex:ida ex:mengajar ex:kecerdasan_buatan dan ex:kecerdasan_buatan foaf:name "Kecerdasan Buatan"@id]

## Langkah 4 - Wikidata
- Jumlah baris Q1 dengan wdt:P31: 20
- Jumlah baris Q1 dengan wdt:P31/wdt:P279*: 27
- Penjelasan perbedaan: Jumlah hasil dapat bertambah karena wdt:P31/wdt:P279* juga mengambil entitas yang merupakan subclass dari University, sehingga cakupan pencariannya lebih luas dibanding hanya menggunakan wdt:P31.

## Langkah 5 - Endpoint dari Python
- agent=UA: Mengirim header User-Agent yang mengidentifikasi program dan kontak pemilik (email). Wikidata mewajibkan ini agar admin dapat menghubungi pengguna dan tidak memblokir permintaan anonim.
- setReturnFormat(JSON): Meminta endpoint mengembalikan hasil dalam format SPARQL JSON, sehingga `queryAndConvert()` menghasilkan dict Python (`results` -> `bindings`) yang mudah diolah.
- b.get("kotaLabel", {}): Variabel `?kotaLabel` bisa tidak terikat pada sebuah baris, sehingga kuncinya tidak ada di dict. `get` dengan default `{}` mencegah KeyError, lalu `.get("value", "")` menghasilkan string kosong.
  
---
<br><br>
## Refleksi 


### 1. Di titik mana SPARQL berbeda dari SQL?

SPARQL dan SQL pada dasarnya digunakan untuk query data, namun terdapat perbedaan mendasar pada model data, struktur query, serta penanganan data yang hilang:

* **Model Data:** SQL beroperasi pada **model relasional** (tabel, baris, dan kolom yang terstruktur kaku), sedangkan SPARQL beroperasi pada **graf RDF** berupa pasangan tripel (`Subject - Predicate - Object`).
* **Fleksibilitas Skema:** SQL membutuhkan skema tabel yang didefinisikan secara eksplisit sejak awal (*schema-on-write*). Sebaliknya, SPARQL bekerja pada graf tanpa skema yang mengikat (*schema-on-read*), sehingga penambahan entitas atau hubungan baru dapat dilakukan secara dinamis.
* **Asumsi Pengetahuan (OWA vs CWA):** 
  * SQL mengadopsi **Closed World Assumption (CWA)**: jika data tidak ada di basis data, maka dianggap tidak ada/salah.
  * SPARQL mengadopsi **Open World Assumption (OWA)**: jika fakta tidak ada di dalam graf, artinya fakta tersebut *belum diketahui*, bukan pasti salah.
* **Identifikasi Sumber Daya:** SPARQL menggunakan **IRI/URI** global untuk mengidentifikasi entitas dan relasi secara universal di web, sedangkan SQL umumnya menggunakan kunci lokal (`Primary Key` / `Foreign Key`) yang terbatas pada lingkup satu basis data.

<br><br>

### 2. Kapan Anda memakai graf lokal (rdflib) dan kapan endpoint publik?

* **Kita menggunakan Graf Lokal pada saat (`rdflib`):**
  * **Pengembangan & Pengujian (Development/Testing):** Saat membuat skema ontologi baru, melakukan *debugging*, atau uji coba query secara lokal tanpa memerlukan koneksi internet.
  * **Data Sensitif/Privat:** Ketika mengolah dataset internal organisasi atau data pribadi yang tidak boleh dipublikasikan ke jaringan luar.
  * **Ukuran Data Terbatas:** Cocok untuk dataset kecil hingga menengah yang dapat ditampung sepenuhnya di dalam memori komputer.

* **Sedangkan Endpoint Publik digunakan saat (misal: DBpedia, Wikidata):**
  * **Integrasi Data Global (Linked Open Data):** Saat membutuhkan data eksternal berskala masif (seperti referensi geografi, data sejarah, atau taksonomi publik) untuk memperkaya data lokal.
  * **Query Terdistribusi (Federated Query):** Ketika perlu menggabungkan informasi dari berbagai sumber di seluruh dunia secara *real-time* tanpa harus mengunduh seluruh isi dataset-nya.
  * **Data Berskala Masif:** Untuk mengueri dataset berukuran terabita yang dikelola oleh *triplestore* server berkinerja tinggi.

<br><br>

### 3. Sebutkan satu hasil query yang mengejutkan dan jelaskan penyebabnya.

* **Hasil Query yang Mengejutkan:**
  Pola query `?mk ex:nama "Web Semantik"` menghasilkan **0 baris** (kosong), padahal di dalam graf jelas-jelas terdapat data mata kuliah Web Semantik.

* **Penyebabnya:**
  Terjadi ketidakcocokan tipe data literal (*literal type mismatch*). Pola query mencari string polos (`plain literal`) tanpa tag bahasa (`"Web Semantik"`), sedangkan data yang tersimpan di dalam graf adalah *language-tagged literal* (`"Web Semantik"@id`). 
  
  Dalam spesifikasi RDF dan SPARQL, nilai literal dengan tag bahasa dianggap sebagai entitas yang berbeda secara ketat dari string biasa, sehingga pencocokan pola gagal total jika tag bahasanya tidak dimasukkan atau tidak difilter dengan fungsi seperti `STR()`.