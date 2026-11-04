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





## Langkah 2 – ASK dan Asumsi Dunia Terbuka

Berikut adalah jawaban dan penjelasan untuk setiap pertanyaan pada Langkah 2 berdasarkan data dari Langkah 1.

---

### 1. Apa hasil `ASK { ex:budi ex:mengajar ex:tif2410 }`? Bagaimana tafsir yang tepat menurut asumsi dunia terbuka?

* **Hasil:** `false` (salah) karena tripel tersebut tidak ditemukan di dalam grafik RDF yang ada. Berdasarkan data Langkah 1, `ex:budi` hanya mengajar `ex:tif2305`, sedangkan `ex:tif2410` diajar oleh `ex:sari`.
* **Tafsir Menurut Asumsi Dunia Terbuka (Open World Assumption - OWA):** 
  Dalam OWA, ketiadaan informasi di dalam basis pengetahuan **tidak berarti** bahwa informasi tersebut salah atau tidak pernah terjadi di dunia nyata. Hasil `false` hanya menunjukkan bahwa *di dalam graf saat ini*, fakta tersebut belum dinyatakan atau belum tercatat. Bisa jadi di dunia nyata Budi memang mengajar mata kuliah tersebut, tetapi data itu belum dimasukkan ke dalam sistem.

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

