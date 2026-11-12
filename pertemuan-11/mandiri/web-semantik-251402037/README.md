# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 / 10
- Mengapa tidak (atau mengapa tepat) 30 triple: Hasilnya tepat mencapai 30 triple karena `LIMIT 10` membatasi blok `WHERE` pada 10 baris solusi (`solution`), dan pada eksekusi ini ke-10 baris solusi tersebut berasal dari 10 kota yang semuanya berbeda. Karena setiap kota memiliki 1 label bahasa Indonesia dan 1 nilai populasi yang terambil, seluruh 3 pola dalam template `CONSTRUCT` (`?kota a ex:Kota`, `?kota rdfs:label ?namaKota`, dan `?kota ex:populasi ?populasi`) menghasilkan triple yang unik tanpa ada duplikat yang tergabung (10 solusi × 3 pola = 30 triple).

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia
- Triple yang tetap tercetak untuk film tanpa tanggal: Tiga triple tetap tercetak, yaitu `?film a schema:Movie`, `?film schema:name ?judul`, dan `?film schema:director dbr:Christopher_Nolan`, sedangkan pola `?film schema:datePublished ?rilis` tidak tercetak. Tidak muncul pesan error karena `dbo:releaseDate` dibungkus dalam klausa `OPTIONAL`; ketika tanggal rilis kosong, variabel `?rilis` berstatus tak terikat (*unbound*), dan SPARQL `CONSTRUCT` secara otomatis melewatkan pola template yang memiliki variabel tak terikat.
- Query lokal tanpa internet: Menjalankan `Q_TANPA_TANGGAL` pada `film_nolan.ttl` tetap berhasil tanpa internet karena graf hasil `CONSTRUCT` sudah tersimpan di disk lokal dan diproses sepenuhnya di memori oleh `rdflib`. Sebaliknya, jika menjalankan ulang seluruh skrip `demo_c.py` tanpa internet, program akan gagal dengan error jaringan (`URLError` / gagal resolusi host `dbpedia.org`) pada baris `sp.queryAndConvert()` karena `SPARQLWrapper` mencoba menghubungi endpoint jarak jauh DBpedia.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: Karena query `CONSTRUCT` pada `q_demo_b.rq` melakukan pemetaan skema dari kosakata DBpedia (`dbo:Film`) ke kosakata Schema.org (`schema:Movie`). Dengan demikian, setiap entitas film di dalam `film_nolan.ttl` hanya memiliki tipe `schema:Movie` dan tidak memiliki triple `rdf:type dbo:Film`, sehingga pencarian `?f a dbo:Film` bernilai 0.

## Bagian C - Materialisasi
- Output demo_d.py:
  ```text
  Sebelum: 0
  Sesudah: 3
  Ada Rina: 3
- Mengapa Ada Rina bernilai 3: Karena materialisasi menggunakan CONSTRUCT bersifat statis dan hanya berjalan satu kali saat dieksekusi, bukan mekanisme penalaran otomatis (live reasoning) yang terus memantau perubahan graf. Triple ex:rina a ex:DosenTetap baru ditambahkan ke graf g setelah blok CONSTRUCT selesai dijalankan, sehingga triple turunan ex:rina a ex:Dosen dan ex:rina a foaf:Person belum pernah dibentuk di dalam graf.
- Output materialisasi_ulang.py:
    ```text
    Putaran 1: 4 triple baru | Person: 3
    Rina masuk | Person: 3
    Putaran 2 | Person: 4
    Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: Tiga triple yang sudah ada di kampus.ttl sehingga tidak dihitung sebagai triple baru adalah ex:budi a ex:DosenTetap, ex:sari a ex:Dosen, dan ex:andi a ex:Mahasiswa. Ketiganya tercetak oleh bagian operator * (nol atau lebih langkah) pada jalur a/rdfs:subClassOf* saat menempuh 0 langkah (refleksif terhadap kelas asal masing-masing individu).
-Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: Berkas terpisah kampus_turunan.ttl memisahkan fakta dasar (kampus.ttl) dari fakta hasil inferensi, sehingga jika suatu hari ex:Dosen tidak lagi menjadi subkelas foaf:Person, fakta dasar tetap bersih dan kesimpulan lama yang tidak valid tidak tercampur permanen seperti pada kampus_v4.ttl. Langkah manual yang tetap harus dilakukan adalah menghapus berkas kampus_turunan.ttl yang lama, memperbarui struktur rdfs:subClassOf pada skema, lalu menjalankan ulang skrip materialisasi dari fakta dasar untuk membangkitkan kampus_turunan.ttl yang baru.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong, tanpa error | Baris `CONSTRUCT { ?film ex:judul ?j . }` memakai variabel `?film` yang tidak terikat karena tidak cocok dengan variabel `?f` pada baris `?f dbo:director dbr:Christopher_Nolan ;` di blok `WHERE`. | 3 triple (`Following`, `Insomnia`, `Memento` masing-masing memiliki satu `ex:judul`) |
| rusak_b | 4 triple | Dua nilai yang tampak sama | Baris `?o foaf:name\|rdfs:label\|schema:name ?n .` mengambil literal dari predikat berbeda tanpa menyeragamkan tag bahasa, sehingga `"Christopher Nolan"` dan `"Christopher Nolan"@en` pada `dbr:Christopher_Nolan` dianggap dua nilai berbeda. | 3 triple (tepat satu `ex:nama` untuk `Christopher_Nolan`, `Joko_Anwar`, dan `Mira_Lesmana` dengan `STR(?n)`) |
| rusak_c | 0 triple | Superkelas tidak ditemukan | Baris `?x a ex:Permukiman .` di blok `WHERE` hanya mencocokkan keanggotaan kelas langsung tanpa menelusuri hierarki subkelas melalui jalur `rdfs:subClassOf*`. | 3 triple (`ex:Medan`, `ex:Surabaya`, dan `ex:Tomok` sebagai `ex:Permukiman`) |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak relevan di berkas `.rq` karena query dijalankan manual lewat antarmuka browser (`query.wikidata.org`), sehingga `User-Agent` dikirim otomatis oleh browser. | Memenuhi pada baris `UA = "KelasWebSemantik/1.0 (email@kampus.ac.id)"` (diisi email pribadi) dan diteruskan ke `SPARQLWrapper(..., agent=UA)`. |
| 2 LIMIT | Memenuhi pada baris terakhir `LIMIT 10` untuk membatasi jumlah baris solusi saat eksplorasi. | Tidak memakai `LIMIT` eksplisit karena pola `dbo:director dbr:Christopher_Nolan` di `q_demo_b.rq` sudah sangat sempit (hanya 16 film). |
| 3 Simpan, jangan ulangi | Tidak relevan di dalam sintaks berkas `.rq` karena hasil disimpan dan dicatat manual dari tampilan browser. | Memenuhi pada baris `g.serialize("film_nolan.ttl", format="turtle")` dan pembacaan lokal `Graph().parse("film_nolan.ttl")` tanpa mengulang request ke endpoint. |
| 4 Jangkar jalur | Memenuhi pada baris `?kota wdt:P31/wdt:P279* wd:Q515 ;` yang menjangkarkan ujung jalur `*` pada IRI spesifik `wd:Q515`. | Tidak relevan karena query `q_demo_b.rq` tidak menggunakan operator jalur `*` maupun `+`. |

- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:
  ```sparql
  PREFIX ex: [http://contoh.id/](http://contoh.id/)
  CONSTRUCT {
    ?kota a ex:Kota ;
          rdfs:label ?namaKota ;
          ex:populasi ?populasi .
  }
  WHERE {
    ?kota wdt:P31/wdt:P279* ?kelas ;
          wdt:P17 wd:Q252 ;
          wdt:P1082 ?populasi ;
          rdfs:label ?namaKota .
    FILTER ( LANG(?namaKota) = "id" )
  }
  LIMIT 10

alasannya : Menghapus jangkar IRI wd:Q515 menjadi variabel bebas ?kelas membuat jalur transitif wdt:P279* tidak memiliki titik henti tertentu, sehingga mesin endpoint harus menelusuri seluruh rantai superkelas hingga puncak taksonomi Wikidata untuk setiap entitas di Indonesia dan memicu beban komputasi besar atau timeout.

### Diskusi 1 - Taksonomi berubah
Jika taksonomi pada Demo D berubah sehingga ex:Dosen tidak lagi menjadi subkelas foaf:Person, maka tiga triple hasil materialisasi menjadi salah, yaitu ex:budi a foaf:Person, ex:sari a foaf:Person, dan ex:rina a foaf:Person yang terbentuk pada Putaran 2 di C2. Sementara itu, ex:andi a foaf:Person tetap valid karena diturunkan melalui ex:Mahasiswa. Untuk menemukan triple yang usang tersebut, kita menjalankan ulang query CONSTRUCT dari fakta dasar (kampus.ttl ditambah data Rina) menggunakan taksonomi terbaru, lalu membandingkan selisih himpunan triple antara graf produksi lama dan graf hasil inferensi baru.

Perbandingan antara kampus_v4.ttl dari C1 dan kampus_turunan.ttl dari C2 menunjukkan perbedaan krusial dalam pemeliharaan graf. Berkas kampus_v4.ttl mencampur fakta dasar dan triple turunan dalam satu file tanpa penanda asal-usul, sehingga sistem tidak dapat membedakan mana keanggotaan foaf:Person yang berasal dari fakta eksplisit dan mana yang merupakan kesimpulan lama. Sebaliknya, kampus_turunan.ttl menyimpan khusus 6 triple hasil inferensi secara terpisah dari fakta dasar. Pemisahan ini memudahkan tim untuk langsung menghapus berkas kampus_turunan.ttl yang lama dan membangkitkannya ulang dari data dasar yang tetap bersih tanpa merusak integritas graf produksi.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk membangun dashboard populasi kota, saya memilih SELECT karena antarmuka dashboard memerlukan data tabular yang siap diolah menjadi tabel atau grafik serta mendukung fungsi agregasi seperti MAX dan GROUP BY. Pada Bagian A, terlihat bahwa LIMIT 10 menghasilkan 10 baris solusi (30 triple karena setiap solusi memetakan 3 pola), dan pada skala data yang lebih luas seperti ex:Medan di kota.ttl, satu kota dapat memiliki lebih dari satu nilai populasi (wdt:P1082). Jika memakai CONSTRUCT, seluruh triple populasi kembar tersebut tetap tersimpan dalam graf tanpa memilih satu angka tunggal untuk ditampilkan di dashboard.

Sebaliknya, untuk menggabungkan data kota dari tiga sumber berbeda, saya memilih CONSTRUCT karena tujuannya adalah menyelaraskan beragam kosakata ke dalam satu skema graf RDF terpadu. Namun, CONSTRUCT hanya melebur triple yang identik secara persis. Temuan pada rusak_b.rq membuktikan bahwa query menghasilkan 4 triple alih-alih 3 karena dbr:Christopher_Nolan memiliki literal "Christopher Nolan" tanpa tag bahasa dan "Christopher Nolan"@en yang dianggap berbeda oleh RDF. Oleh karena itu, integrasi lintas sumber dengan CONSTRUCT wajib menormalisasi literal di blok WHERE memakai fungsi seperti STR() agar tidak memicu duplikasi data.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | **Bagian A** (`LIMIT 10` dengan 10 solusi kota berbeda mencetak 3 pola per solusi menjadi `30` triple, dan `LIMIT 30` menjadi `90` triple) serta **Bagian D** (`perbaikan_b.rq` melebur 2 literal nama Christopher Nolan yang sudah dinormalisasi menjadi `3 triple` unik, bukan 4). |
| 2 | **Bagian B** (`demo_c.py` menghasilkan `48 triple` dari `16` film tanpa tanggal rilis karena pola `schema:datePublished ?rilis` dilewati tanpa error) serta **Bagian D** (`rusak_a.rq` menghasilkan `0 triple` tanpa error akibat variabel `?film` tak terikat). |
| 3 | **Bagian D** pada `rusak_b.rq` (`4 triple`) dan `perbaikan_b.rq` (`3 triple`) yang memakai `VALUES ?o { ... }` serta jalur alternatif `foaf:name\|rdfs:label\|schema:name` untuk menyatukan tiga predikat nama berbeda. |
| 4 | **Bagian A** (`wdt:P31/wdt:P279* wd:Q515` menghasilkan `30` triple), **Bagian C** (`?x a/rdfs:subClassOf* ?super` menghasilkan `Sesudah: 3` Person dari `ex:budi` tanpa menyebut kelas perantara `ex:Dosen`), dan **Bagian D** (`perbaikan_c.rq` menghasilkan `3 triple` permukiman). |
| 5 | **Bagian C1** (`demo_d.py` menyimpan kesimpulan ke `kampus_v4.ttl` sehingga `Sesudah: 3`, tetapi tetap `Ada Rina: 3` setelah data baru masuk) dan **Bagian C2** (`materialisasi_ulang.py` baru menaikkan `Person: 4` dan `6` triple turunan pada Putaran 2 setelah dihitung ulang). |