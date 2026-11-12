## Langkah 1 - Solution menjadi triple
| Solution | ?d | ?mk | Triple yang dicetak |
|----------|----|-----|---------------------|
| 1        | ex:budi | ex:tif2108 | ex:tif2108 a ex:MataKuliahAktif <br> ex:tif2108 ex:diampuOleh ex:budi |
| 2        | ex:budi | ex:tif2104 | ex:tif2104 a ex:MataKuliahAktif <br> ex:tif2104 ex:diampuOleh ex:budi |
| 3        | ex:sari | ex:tif2108 | ex:tif2108 a ex:MataKuliahAktif <br> ex:tif2108 ex:diampuOleh ex:sari |
| 4        | ex:ida  | ex:tif2104 | ex:tif2104 a ex:MataKuliahAktif <br> ex:tif2104 ex:diampuOleh ex:ida  |

- Jumlah solution: 4
- Jumlah cetakan triple: 8
- Jumlah triple di graf hasil: 6
- Triple yang tercetak lebih dari sekali: `ex:tif2108 a ex:MataKuliahAktif` dan `ex:tif2104 a ex:MataKuliahAktif`

## Refleksi
1. **Mengapa jumlah triple hasil `CONSTRUCT` bisa lebih kecil dari jumlah baris `SELECT` dengan `WHERE` yang sama?**
   Query `SELECT` menghasilkan tabel yang dapat memuat baris berulang sesuai kombinasi variabel di klausa `WHERE`, sedangkan hasil `CONSTRUCT` membentuk graf RDF yang bersifat **himpunan (*set*)** sehingga triple yang identik otomatis digabung (deduplikasi). Selain itu, jika pola di `CONSTRUCT` hanya memakai sebagian variabel dari `WHERE` (seperti `?mk a ex:MataKuliahAktif` tanpa `?d`), variasi nilai variabel lain yang tidak ikut dicetak akan menghasilkan triple yang sama persis.

2. **Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di `kampus_usu_v4.ttl`?**
   Triple turunan yang sudah tersimpan di file statis `kampus_usu_v4.ttl` **tidak akan berubah secara otomatis** sehingga isinya menjadi usang dan tidak sinkron dengan taksonomi terbaru. Untuk memperbaruinya, query `CONSTRUCT` (atau *reasoner*) harus dijalankan ulang pada graf sumber yang baru, lalu hasilnya disimpan kembali.

3. **Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?**
   - **Tabel (CSV):** Dipilih saat data akhir digunakan untuk pelaporan, rekapitulasi angka, tampilan antarmuka aplikasi, atau diolah di perangkat lunak *spreadsheet* dan basis data relasional.
   - **Graf (Turtle):** Dipilih saat hasil query berupa fakta atau relasi baru yang ingin digabungkan kembali ke dalam *knowledge graph*, dibagikan sebagai *Linked Data*, atau di-query ulang menggunakan SPARQL dan *reasoner*.

---

# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30 triple
- Triple dengan LIMIT 30: 90 triple
- Baris SELECT LIMIT 10 / kota berbeda: 10 baris / 10 kota berbeda
- Mengapa tidak (atau mengapa tepat) 30 triple:
  Hasil saya mencapai **tepat 30 triple**, yaitu batas atas maksimal dari `LIMIT 10` dengan 3 pola template ($10 \times 3 = 30$). Berdasarkan tabel `SELECT`, ke-10 baris (*solution*) pertama yang dikembalikan oleh klausa `WHERE` seluruhnya merupakan **10 kota yang berbeda** (Jakarta, Tubei, Turikale, Bondowoso, Tanah Merah, Kepanjen, Tanjung Selor, Sidoarjo, Purwokerto, dan Tual). Karena tidak ada kota yang muncul berulang dalam 10 baris tersebut, ketiga pola template (`?kota a ex:Kota`, `rdfs:label ?namaKota`, dan `ex:populasi ?populasi`) mencetak 30 triple yang semuanya unik sehingga tidak ada triple kembar yang digabung oleh graf RDF.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia
- Triple yang tetap tercetak untuk film tanpa tanggal:
  Tiga triple tetap tercetak untuk setiap film tanpa `dbo:releaseDate`, yaitu `?film a schema:Movie`, `?film schema:name ?judul`, dan `?film schema:director dbr:Christopher_Nolan`. Satu-satunya pola yang tidak tercetak adalah `?film schema:datePublished ?rilis`. Tidak muncul pesan error karena menurut aturan `CONSTRUCT` pada SPARQL, pola triple yang mengandung variabel tak terikat (*unbound* akibat blok `OPTIONAL` tidak menemukan kecocokan) akan dilewati (*skip*) secara diam-diam.
- Query lokal tanpa internet:
  Menjalankan query `Q_TANPA_TANGGAL` pada `film_nolan.ttl` tetap berhasil tanpa internet karena graf hasil konversi sudah tersimpan lokal dan diproses langsung di memori oleh `rdflib`. Namun, jika seluruh skrip `demo_c.py` dijalankan ulang tanpa internet, program akan mengalami error jaringan (`URLError`) pada baris `sp.queryAndConvert()` karena mencoba mengirim permintaan HTTP ke endpoint publik DBpedia.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl:
  Karena query `CONSTRUCT` pada Demo B melakukan pemetaan kosakata dari ontologi DBpedia (`dbo:Film`) ke Schema.org (`schema:Movie`). Di dalam berkas `film_nolan.ttl` hanya tersimpan triple hasil cetakan template (`?film a schema:Movie`), sedangkan triple sumber `dbo:Film` tidak ikut disimpan sehingga pencariannya menghasilkan 0.

## Bagian C - Materialisasi
- Output demo_d.py:
  `Sebelum: 0`, `Sesudah: 3`, `Ada Rina: 3`
- Mengapa Ada Rina bernilai 3:
  Karena `CONSTRUCT` melakukan materialisasi satu kali (statis), bukan inferensi otomatis yang terus aktif. Fakta `ex:rina a ex:DosenTetap` ditambahkan ke dalam graf `g` **setelah** proses `CONSTRUCT` selesai dijalankan, sehingga triple turunan eksplisit `ex:rina a foaf:Person` belum pernah dihitung dan ditambahkan ke graf.
- Output materialisasi_ulang.py:
  `Putaran 1: 4 triple baru | Person: 3`, `Rina masuk | Person: 3`, `Putaran 2 | Person: 4`, `Triple turunan disimpan terpisah: 6`
- Tiga triple yang bukan baru:
  Tiga triple yang bukan baru adalah triple tipe kelas langsung (*direct type*) yang sudah ada sejak awal di `kampus.ttl` untuk 3 individu awal (`ex:budi a ex:DosenTetap`, `ex:sari a ex:Dosen`, dan `ex:andi a ex:Mahasiswa`). Triple tersebut ikut tercetak oleh operator `*` (*zero-or-more*) pada jalur `a/rdfs:subClassOf*` untuk kasus 0 langkah (`?super` sama dengan kelas asalnya), lalu disaring oleh pengecekan `if t not in g`.
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa:
  Menyimpan triple turunan secara terpisah di `kampus_turunan.ttl` menjaga berkas sumber `kampus.ttl` tetap bersih dari fakta turunan yang bisa menjadi salah saat struktur taksonomi berubah. Jika `ex:Dosen` tidak lagi menjadi subkelas `foaf:Person`, langkah manual yang tetap harus dilakukan adalah menghapus atau mengosongkan `kampus_turunan.ttl` lama, memperbarui taksonomi di `kampus.ttl`, lalu menjalankan ulang `materialisasi_ulang.py` agar isi `kampus_turunan.ttl` dihitung ulang.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Tidak ada pesan error, tetapi hasil kosong (0 triple) | Pada baris `CONSTRUCT { ?film ex:judul ?j . }` dan `WHERE { ?f dbo:director ... }`, nama variabel subjek tidak sama (`?film` vs `?f`) sehingga `?film` tidak terikat nilai apa pun. | 3 triple (satu judul per film Nolan) |
| rusak_b | 6 triple | Jumlah triple melebihi target 3 triple (muncul nama ganda per orang) | Pada baris `?o foaf:name\|rdfs:label\|schema:name ?n .`, tidak ada `FILTER` bahasa sehingga semua literal dengan tag bahasa berbeda (`@en` dan `@id`) ikut tercetak. | 3 triple (tepat satu `ex:nama` per orang) |
| rusak_c | 0 triple | Tidak ada pesan error, tetapi individu subkelas tidak ditemukan | Pada baris `?x a ex:Permukiman .`, pola hanya mencocokkan tipe kelas langsung tanpa menelusuri subkelas menggunakan `rdfs:subClassOf*`. | 3 triple (`Medan`, `Surabaya`, `Tomok`) |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak relevan (berkas `.rq` hanya berisi teks query yang dijalankan lewat browser) | Terpenuhi pada baris `UA = "KelasWebSemantik/1.0 (...)"` dan `SPARQLWrapper(..., agent=UA)` |
| 2 LIMIT | Terpenuhi pada baris terakhir `LIMIT 10` | Tidak dipakai karena query `q_demo_b.rq` sudah terfilter spesifik pada satu sutradara (`dbr:Christopher_Nolan`) |
| 3 Simpan, jangan ulangi | Tidak relevan (query SPARQL murni tidak menyimpan berkas lokal) | Terpenuhi pada baris `g.serialize("film_nolan.ttl", ...)` dan pembacaan offline `Graph().parse("film_nolan.ttl")` |
| 4 Jangkar jalur | Terpenuhi pada baris `?kota wdt:P31/wdt:P279* wd:Q515 ;` karena jalur `*` dijangkarkan ke IRI `wd:Q515` | Tidak relevan (tidak ada operator jalur `*` atau `+` pada query yang dikirim) |

- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:
  ```sparql
  PREFIX ex: [http://contoh.id/](http://contoh.id/)
  CONSTRUCT {
    ?kota a ex:Kota ;
          rdfs:label ?namaKota ;
          ex:populasi ?populasi .
  }
  WHERE {
    ?kota wdt:P31/wdt:P279* ?kelas .
    ?kota wdt:P17 wd:Q252 ;
          wdt:P1082 ?populasi ;
          rdfs:label ?namaKota .
    FILTER ( LANG(?namaKota) = "id" )
  }
  LIMIT 10
  ```
  **Alasan:** Pada pola `?kota wdt:P31/wdt:P279* ?kelas`, jalur transitif `wdt:P279*` menghubungkan dua variabel bebas (`?kota` dan `?kelas`) tanpa jangkar IRI tertentu (`wd:Q515`). Hal ini memaksa endpoint Wikidata menelusuri seluruh rantai subkelas ke atas untuk setiap entitas di seluruh graf, sehingga beban komputasi melonjak drastis dan berisiko menyebabkan *timeout*.

### Diskusi 1 - Taksonomi berubah
Jika setahun kemudian taksonomi kampus berubah—misalnya `ex:Dosen` tidak lagi menjadi subkelas dari `foaf:Person`—maka triple hasil inferensi keanggotaan kelas lama seperti `ex:budi a foaf:Person` atau `ex:sari a foaf:Person` yang berasal dari jalur `ex:Dosen` kini menjadi salah. Triple yang keliru tersebut dapat ditemukan dengan cara menjalankan ulang query aturan `CONSTRUCT { ?x a ?super } WHERE { ?x a/rdfs:subClassOf* ?super }` pada graf sumber `kampus.ttl` yang sudah diperbarui taksonominya, lalu membandingkan selisih (*graph difference*) antara himpunan triple baru dengan triple yang tersimpan sebelumnya.

Perbandingan antara `kampus_v4.ttl` (C1) dan `kampus_turunan.ttl` (C2) menunjukkan perbedaan arsitektur pengelolaan data yang krusial. Pada `kampus_v4.ttl` dari C1, seluruh triple sumber asli dan 3 triple turunan `foaf:Person` digabung menjadi satu berkas tunggal, sehingga membersihkan triple yang salah saat taksonomi berubah menjadi sulit karena fakta asli dan hasil materialisasi bercampur. Sebaliknya, pada C2, 6 triple turunan disimpan terpisah di `kampus_turunan.ttl`, sementara fakta mentah tetap bersih di `kampus.ttl`. Dengan pemisahan ini, kita cukup menghapus `kampus_turunan.ttl` lama dan menjalankan ulang `materialisasi_ulang.py` untuk membangun ulang graf turunan yang akurat tanpa merusak data sumber.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk menampilkan grafik atau tabel pada *dashboard* populasi kota secara langsung, saya memilih **SELECT** karena hasilnya sudah berbentuk tabel baris dan kolom yang siap diolah oleh antarmuka aplikasi maupun pustaka visualisasi tanpa perlu mengurai struktur graf kembali. Namun, apabila tugasnya adalah **menggabungkan data kota dari tiga sumber berbeda** sebelum ditampilkan, saya menggunakan **CONSTRUCT** terlebih dahulu untuk menyeragamkan kosakata (seperti memetakan properti sumber menjadi `ex:Kota` dan `ex:populasi`), lalu menjalankan `SELECT` di atas graf gabungan lokal tersebut.

Pemilihan ini didukung oleh temuan pada Bagian A dan Bagian D (`rusak_b.rq`). Pada Bagian A dengan `LIMIT 10`, kebetulan seluruh 10 baris merupakan kota berbeda (Jakarta, Tubei, Turikale, Bondowoso, Tanah Merah, Kepanjen, Tanjung Selor, Sidoarjo, Purwokerto, Tual) sehingga menghasilkan tepat 30 triple, namun ketika batas diperbesar atau suatu kota memiliki lebih dari satu nilai populasi `wdt:P1082` dari tahun sensus berbeda, `SELECT` akan menghasilkan baris kota berulang sedangkan `CONSTRUCT` otomatis menggabungkan triple identik seperti `?kota a ex:Kota` karena graf RDF bersifat himpunan. Sementara itu, pada `rusak_b.rq`, penggabungan predikat `foaf:name|rdfs:label|schema:name` tanpa penyaring bahasa memunculkan nama ganda akibat tag bahasa berbeda (`@en` dan `@id`). Dengan `CONSTRUCT` yang dilengkapi `FILTER` bahasa dan agregasi di `SELECT`, integrasi dari tiga sumber menjadi konsisten dan bebas duplikasi.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian A: dengan `LIMIT 10` dan 3 pola template menghasilkan batas atas 30 triple karena ke-10 solution-nya unik semua; sedangkan pada Langkah 1, 4 solution × 2 pola menghasilkan 8 cetakan triple tetapi digabung menjadi 6 triple unik karena 2 triple tipe kelas tercetak kembar. |
| 2 | Bagian B2 (`q_demo_b.rq`) untuk 16 film Nolan tanpa `dbo:releaseDate` tidak mencetak `schema:datePublished` tanpa error, serta Bagian D (`rusak_a.rq`) di mana `?film` tak terikat menghasilkan 0 triple tanpa error. |
| 3 | Bagian D (`rusak_b.rq` / `perbaikan_b.rq`) yang memakai `VALUES ?o { ... }` dan jalur `foaf:name\|rdfs:label\|schema:name` untuk menyatukan tiga predikat nama berbeda. |
| 4 | Bagian A (`wdt:P31/wdt:P279* wd:Q515`), Bagian C (`a/rdfs:subClassOf*` menghasilkan 7 triple di putaran 1), dan Bagian D (`perbaikan_c.rq` menghasilkan 3 triple: Medan, Surabaya, Tomok). |
| 5 | Bagian C1 dan C2 (`demo_d.py` dan `materialisasi_ulang.py`), di mana setelah Rina masuk hitungan `Person` tetap `3` dan baru menjadi `4` setelah aturan dijalankan ulang pada Putaran 2. |