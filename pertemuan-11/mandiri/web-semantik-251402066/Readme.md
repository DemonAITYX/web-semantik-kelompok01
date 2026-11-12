# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 / 10
- Mengapa tidak (atau mengapa tepat) 30 triple: Hasil CONSTRUCT LIMIT 10 mencapai tepat 30 triple[cite: 1] karena masing-masing dari 10 solution yang dikembalikan berasal dari entitas kota berbeda (Jakarta, Kota Manokwari, Singaraja, Atambua, Sintang, Indramayu, Meulaboh, Kota Mamuju, Tual, dan Soreang) dengan masing-masing hanya satu nilai populasi dan satu label bahasa Indonesia[cite: 4]. Karena tidak ada solution ganda yang mencetak triple identik, seluruh 30 triple tetap unik dan tidak ada yang tergabung.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia / data contoh film.ttl
- Triple yang tetap tercetak untuk film tanpa tanggal: Tiga triple lain dari template tetap tercetak untuk setiap film, yaitu `?film a schema:Movie`, `?film schema:name ?judul`, dan `?film schema:director dbr:Christopher_Nolan`, sedangkan pola `?film schema:datePublished ?rilis` tidak dicetak. Tidak muncul pesan error karena klausa `OPTIONAL` membiarkan variabel `?rilis` tetap tidak terikat (unbound) saat `dbo:releaseDate` tidak ada, dan aturan SPARQL `CONSTRUCT` otomatis mengabaikan pola triple yang mengandung variabel unbound.
- Query lokal tanpa internet: Menjalankan hanya query `Q_TANPA_TANGGAL` pada `film_nolan.ttl` tetap berhasil dan mengembalikan angka `16` karena `rdflib` memproses berkas lokal di penyimpanan komputer tanpa akses jaringan. Namun, jika seluruh skrip `demo_c.py` dijalankan ulang tanpa internet, eksekusi akan gagal dengan error koneksi jaringan (`URLError`) pada pemanggilan `sp.queryAndConvert()` karena `SPARQLWrapper` tidak dapat menghubungi endpoint `https://dbpedia.org/sparql`.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: Pada tahap `CONSTRUCT` di `q_demo_b.rq`, kosakata sumber dari DBpedia (`dbo:Film`) telah dipetakan menjadi kosakata `schema.org` (`schema:Movie`). Karena berkas `film_nolan.ttl` hanya menyimpan hasil graf `CONSTRUCT` tersebut dan tidak lagi memuat triple bertipe `dbo:Film`, query lokal dengan pola `dbo:Film` menghasilkan 0.

## Bagian C - Materialisasi
- Output demo_d.py: Sebelum: 0 | Sesudah: 3 | Ada Rina: 3
- Mengapa Ada Rina bernilai 3: Karena materialisasi dengan `CONSTRUCT` hanya berjalan satu kali saat dipanggil dan tidak otomatis melakukan penalaran saat fakta baru masuk. Ketika `ex:rina a ex:DosenTetap` ditambahkan belakangan, RDFLib hanya menyimpan fakta eksplisit tersebut tanpa menurunkan triple `ex:rina a foaf:Person`, sehingga jumlah `foaf:Person` tetap 3 (Budi, Sari, dan Andi).
- Output materialisasi_ulang.py: Putaran 1: 4 triple baru | Person: 3 | Rina masuk | Person: 3 | Putaran 2 | Person: 4 | Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: Tiga triple tersebut adalah fakta kelas asal yang sudah ada di `kampus.ttl`, yaitu `ex:budi a ex:DosenTetap`, `ex:sari a ex:Dosen`, dan `ex:andi a ex:Mahasiswa`. Ketiganya tercetak oleh bagian `rdfs:subClassOf*` pada jalur `a/rdfs:subClassOf*` karena operator `*` mencakup nol langkah (menghasilkan kelas itu sendiri), lalu disaring oleh pengecekan `if t not in g:`.
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: Memisahkan triple hasil inferensi ke `kampus_turunan.ttl` mencegah fakta turunan tercampur permanen dengan fakta eksplisit di graf utama, sehingga triple turunan lama mudah dilacak atau dibuang saat taksonomi berubah. Namun, secara manual kita tetap harus menghapus/menarik kembali triple turunan yang usang dari graf produksi (atau memulai ulang dari graf sumber bersih) dan menjalankan kembali skrip materialisasi agar kesimpulan baru diperbarui.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong, tanpa error | Baris `CONSTRUCT { ?film ex:judul ?j . }` memakai variabel `?film` yang tidak terikat karena di blok `WHERE` variabel subjek yang dipakai adalah `?f`. | 3 triple (`dbr:Following`, `dbr:Insomnia`, `dbr:Memento` dengan `ex:judul`) |
| rusak_b | 4 triple (nama Christopher Nolan muncul dua kali: `"Christopher Nolan"` dan `"Christopher Nolan"@en`) | Dua nilai yang tampak sama | Baris `?o foaf:name\|rdfs:label\|schema:name ?n .` mencocokkan nilai tanpa tag bahasa dan bertag `@en` secara terpisah sehingga tidak dianggap kembar oleh graf RDF. | 3 triple (tepat satu `ex:nama` tanpa tag bahasa per orang) |
| rusak_c | 0 triple | Superkelas tidak ditemukan | Baris `?x a ex:Permukiman .` di blok `WHERE` tidak menelusuri hierarki subkelas (`ex:KotaMetropolitan`, `ex:KotaDiIndonesia`, `ex:Desa`) yang ada di `kota.ttl`. | 3 triple (`ex:Medan`, `ex:Surabaya`, `ex:Tomok` bertipe `ex:Permukiman`) |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak relevan (query dijalankan langsung di antarmuka web Wikidata Query Service sehingga identitas klien diatur oleh browser). | Terpenuhi pada baris `UA = "KelasWebSemantik/1.0 (...)"` dan `SPARQLWrapper("https://dbpedia.org/sparql", agent=UA)` yang mencantumkan nama aplikasi dan email kontak. |
| 2 LIMIT | Terpenuhi pada baris terakhir `LIMIT 10` yang membatasi jumlah solution saat eksplorasi data kota di Wikidata. | Tidak relevan untuk eksplorasi terbuka karena memanggil `q_demo_b.rq` yang sudah terfokus pada satu entitas spesifik (`dbo:director dbr:Christopher_Nolan`) dengan hasil terbatas (16 film). |
| 3 Simpan, jangan ulangi | Tidak relevan (berkas `.rq` hanya berisi teks query SPARQL tanpa mekanisme penyimpanan berkas lokal). | Terpenuhi pada baris `g.serialize("film_nolan.ttl", format="turtle")` untuk menyimpan hasil ke lokal dan `Graph().parse("film_nolan.ttl")` untuk query offline berikutnya. |
| 4 Jangkar jalur | Terpenuhi pada baris `?kota wdt:P31/wdt:P279* wd:Q515 ;` karena jalur transitif `*` dijangkarkan langsung ke IRI `wd:Q515`, bukan di antara dua variabel bebas. | Tidak relevan karena query yang dijalankan (`q_demo_b.rq`) hanya memakai pola triple langsung tanpa operator property path `*` atau `+`. |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:
  ```sparql
  PREFIX ex: [http://contoh.id/](http://contoh.id/)
  CONSTRUCT {
    ?kota a ex:Kota ;
          rdfs:label ?namaKota ;
          ex:populasi ?populasi .
  }
  WHERE {
    ?kota wdt:P31 ?kelas .
    ?kelas wdt:P279* ?induk .
    ?kota wdt:P17 wd:Q252 ;
          wdt:P1082 ?populasi ;
          rdfs:label ?namaKota .
    FILTER ( LANG(?namaKota) = "id" )
  }
  LIMIT 10

### Diskusi 1 - Taksonomi berubah
Ketika hasil materialisasi disimpan langsung ke graf produksi seperti pada kampus_v4.ttl di Bagian C1, triple hasil inferensi (seperti ex:budi a foaf:Person dan ex:sari a foaf:Person) tercampur menyatu dengan fakta eksplisit asli di dalam satu berkas. Jika setahun kemudian taksonomi berubah—misalnya ex:Dosen tidak lagi menjadi subkelas foaf:Person—maka seluruh triple yang menyimpulkan keanggotaan foaf:Person bagi individu dosen (ex:budi, ex:sari, dan ex:rina) otomatis menjadi salah secara semantik. Masalahnya, pada kampus_v4.ttl kita tidak bisa membedakan apakah ex:sari a foaf:Person dulunya ditulis manual oleh admin atau hasil turunan aturan CONSTRUCT, sehingga penghapusannya harus diaudit satu per satu dengan membandingkannya kembali ke berkas sumber kampus.ttl. Sebaliknya, pendekatan pada kampus_turunan.ttl di Bagian C2 memisahkan 6 triple hasil inferensi ke berkas tersendiri. Untuk menemukan dan membersihkan triple yang salah, kita cukup menghapus atau mengabaikan kampus_turunan.ttl lama, memperbarui definisi rdfs:subClassOf pada graf sumber, lalu menjalankan ulang skrip materialisasi dari awal. Pemisahan berkas ini membuat proses pembaruan kesimpulan jauh lebih aman dan terisolasi tanpa risiko merusak fakta asli produksi.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk kebutuhan dashboard populasi kota, saya akan memilih SELECT karena dashboard umumnya membutuhkan data tabular datar (kolom nama kota dan angka populasi) yang siap langsung ditampilkan ke tabel atau grafik antarmuka pengguna tanpa perlu membentuk struktur graf RDF baru. Namun, jika data sumber memiliki beberapa nilai populasi untuk satu kota—seperti kasus ex:Medan di kota.ttl yang tercatat memiliki dua nilai populasi (2435252 dan 2097610) atau entitas Wikidata di Bagian A—query SELECT harus disertai agregasi seperti MAX(?populasi) atau SAMPLE agar satu kota tidak muncul sebagai dua baris kembar di dashboard. Sebaliknya, untuk menggabungkan data kota dari tiga sumber berbeda dengan kosakata yang tidak seragam, CONSTRUCT jauh lebih tepat karena mampu menyelaraskan skema dari masing-masing sumber ke satu kosakata target yang seragam sebelum digabung ke graf lokal, sebagaimana terbukti pada q_demo_b.rq yang memetakan dbo:Film menjadi schema:Movie. Selain itu, saat menggabungkan atribut teks seperti nama kota dari tiga sumber, perlu dilakukan normalisasi seperti BIND(STR(?n) AS ?nama) pada perbaikan_b.rq; tanpa normalisasi tersebut, literal identik dengan tag bahasa berbeda seperti "Christopher Nolan" dan "Christopher Nolan"@en akan dianggap dua triple terpisah dan memicu duplikasi data.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Pada Bagian A (LIMIT 10), template CONSTRUCT dengan 3 pola mencetak tepat 30 triple dari 10 kota berbeda (10 × 3 = 30), sedangkan pada perbaikan_b.rq (Bagian D), 4 baris solusi yang dinormalisasi dengan STR() digabung otomatis menjadi 3 triple karena dua triple untuk dbr:Christopher_Nolan menjadi kembar identik. |
| 2 | Pada Bagian B (demo_c.py), ke-16 film Christopher Nolan dari DBpedia tidak memiliki properti dbo:releaseDate sehingga variabel ?rilis di blok OPTIONAL tidak terikat; hasilnya pola schema:datePublished tidak dicetak (hanya 48 triple dari 3 pola lainnya) dan program berjalan tanpa error. |
| 3 | Pada Bagian D (perbaikan_b.rq), penggunaan VALUES untuk 3 tokoh dan jalur alternatif foaf:name|rdfs:label|schema:name berhasil menyatukan tiga predikat nama berbeda dari masing-masing tokoh menjadi satu predikat seragam ex:nama dalam 3 triple. |
| 4 | Pada Bagian D (perbaikan_c.rq), jalur ?x a/rdfs:subClassOf* ex:Permukiman berhasil menemukan ex:Medan, ex:Surabaya, dan ex:Tomok (3 triple) tanpa perlu menyebut kelas perantara ex:Kota, ex:KotaMetropolitan, ex:KotaDiIndonesia, maupun ex:Desa. |
| 5 | Pada Bagian C (demo_d.py dan materialisasi_ulang.py), materialisasi putaran pertama menyimpan 4 triple turunan baru sehingga foaf:Person menjadi 3, namun saat ex:rina masuk jumlah foaf:Person tetap 3 sampai fungsi materialisasi(g) dijalankan ulang pada putaran kedua hingga menghasilkan 4 foaf:Person dan 6 triple turunan terpisah. |