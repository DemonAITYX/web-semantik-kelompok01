# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

> Catatan: `film.ttl`, `kota.ttl`, dan `kampus.ttl` dari LMS tidak tersedia saat pengerjaan, jadi saya membuat data contoh sendiri yang mengikuti deskripsi tugas (12 triple untuk `q_demo_b.rq`, output demo D sesuai soal). Bagian A dan B2 (DBpedia) memakai data langsung dari endpoint.

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: 30
- Triple dengan LIMIT 30: 90
- Baris SELECT LIMIT 10 / kota berbeda: 10 / 10
- Mengapa tidak (atau mengapa tepat) 30 triple: Pada eksekusi saya hasilnya tepat 30, yaitu batas atas 10 solution x 3 pola template. Sepuluh kota yang muncul (Jakarta, Tubei, Turikale, Bondowoso, Tanah Merah, Kepanjen, Tanjung Selor, Sidoarjo, Karang Tinggi, Kaur Selatan) masing-masing hanya punya satu populasi dan satu label `@id`, jadi tidak ada solution yang berbagi kota. Triple kembar akan muncul bila sebuah kota punya dua nilai `P1082` (misalnya populasi dari dua tahun): kota itu menghasilkan dua solution, dan pola `?kota a ex:Kota` serta `rdfs:label ?namaKota` tercetak dua kali dengan isi identik, lalu digabung menjadi satu. Dalam kasus itu total triple bisa kurang dari 30 walau LIMIT tetap 10 solution. Pada eksekusi saya hal ini tidak terjadi.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: 48 triple, film tanpa tanggal: 16
- Sumber data: DBpedia (langsung dari endpoint `https://dbpedia.org/sparql`)
- Triple yang tetap tercetak untuk film tanpa tanggal: Tiga triple tetap tercetak, yaitu `?film a schema:Movie`, `schema:name ?judul`, dan `schema:director dbr:Christopher_Nolan`. Triple `schema:datePublished ?rilis` tidak tercetak karena `?rilis` tidak terikat (OPTIONAL kosong), dan template CONSTRUCT melewati triple dengan variabel tak terikat tanpa pesan error. Hasil saya: 16 film x 3 triple = 48, dan semuanya tidak punya tanggal, sehingga `COUNT` film tanpa tanggal juga 16.
- Query lokal tanpa internet: Query `Q_TANPA_TANGGAL` hanya membaca `film_nolan.ttl` yang sudah tersimpan di disk lewat `Graph().parse("film_nolan.ttl")`, tidak ada permintaan jaringan, jadi berhasil. Bila seluruh `demo_c.py` dijalankan ulang tanpa internet, `sp.queryAndConvert()` gagal (galat koneksi) sebelum `serialize`, sehingga program berhenti dan berkas tidak diperbarui.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl: Graf hasil CONSTRUCT hanya berisi triple dari template, yaitu `a schema:Movie`. Tipe `dbo:Film` dipakai di WHERE untuk mencari data tetapi tidak dicetak ke graf hasil, jadi query `?f a dbo:Film` pada `film_nolan.ttl` tidak menemukan apa pun.

## Bagian C - Materialisasi
- Output demo_d.py: `Sebelum: 0`, `Sesudah: 3`, `Ada Rina: 3`
- Mengapa Ada Rina bernilai 3: Materialisasi hanya dijalankan satu kali sebelum Rina ada. Triple `ex:rina a ex:DosenTetap` masuk sesudahnya, dan tidak ada yang menurunkan `ex:rina a foaf:Person`. Query `?x a foaf:Person` hanya melihat triple yang benar-benar tersimpan, bukan kesimpulan yang bisa ditarik dari hierarki.
- Output materialisasi_ulang.py: `Putaran 1: 4 triple baru | Person: 3`, `Rina masuk | Person: 3`, `Putaran 2 | Person: 4`, `Triple turunan disimpan terpisah: 6`
- Tiga triple yang bukan baru: Itu triple asli `ex:budi a ex:DosenTetap`, `ex:sari a ex:Dosen`, dan `ex:rudi a ex:Tendik`. Triple ini dicetak oleh jalur `a/rdfs:subClassOf*` pada bagian `*` dengan nol langkah (kelas yang ditulis langsung diambil apa adanya), jadi 7 hasil = 3 asli + 4 baru (`budi a Dosen`, `budi a foaf:Person`, `sari a foaf:Person`, `rudi a foaf:Person`).
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: Berkas ini berisi hanya 6 triple hasil kesimpulan, terpisah dari 7 triple data asli (6 di `kampus.ttl` ditambah Rina; `kampus_v4.ttl` berisi 13 campuran). Bila `ex:Dosen` tidak lagi menjadi subkelas `foaf:Person`, berkas turunan lama bisa dibuang atau dihitung ulang seluruhnya tanpa menyentuh data asli. Langkah manual yang tetap perlu: mengubah taksonomi di sumber, menjalankan ulang `materialisasi_ulang.py` dari `kampus.ttl`, lalu mengganti berkas turunan lama dengan yang baru.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 0 triple | Graf kosong, tanpa error | `CONSTRUCT { ?film ex:judul ?j . }`: template memakai `?film`, padahal WHERE mengikat `?f`, jadi variabel tak terikat | 3 triple (Inception, Interstellar, Dunkirk) setelah `?film` diganti `?f` |
| rusak_b | 5 triple (Nolan dan Joko Anwar masing-masing 2 nama) | Dua nilai yang tampak sama | `?o foaf:name\|rdfs:label\|schema:name ?n .`: label berbeda tag bahasa (`@en` dan `@fr`/`@id`) terambil semua | 3 triple setelah ditambah `FILTER ( LANG(?n) = "en" )` |
| rusak_c | 0 triple | Superkelas tidak ditemukan | `WHERE { ?x a ex:Permukiman . }`: tidak ada jalur subClassOf, padahal Medan/Surabaya bertipe `ex:Kota` dan Tomok `ex:Desa` | 3 triple (Medan, Surabaya, Tomok) setelah `?x a/rdfs:subClassOf* ex:Permukiman` |

Hasil perbaikan ada di `perbaikan_a.rq`, `perbaikan_b.rq`, `perbaikan_c.rq`.

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Dijalankan di browser WDQS (UA dari browser). Saat saya jalankan lewat Python, saya memakai UA `KelasWebSemantik/1.0 (guloyosua@gmail.com)`. | Baris `UA = "KelasWebSemantik/1.0 (guloyosua@gmail.com)"` dan `agent=UA`. |
| 2 LIMIT | Baris terakhir `LIMIT 10`. | `q_demo_b.rq` tidak memakai LIMIT, tetapi dibatasi jangkar `dbr:Christopher_Nolan` (hanya 16 film). |
| 3 Simpan, jangan ulangi | Tidak relevan: dijalankan hanya untuk melihat angka. Hasil bisa disimpan sebagai `.ttl` bila dipakai lagi. | `g.serialize("film_nolan.ttl")`, lalu query kedua dari berkas lokal. |
| 4 Jangkar jalur | `wdt:P31/wdt:P279* wd:Q515` berjangkar pada `wd:Q515` (kota). | Tidak ada jalur di query. |

- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:
  ```sparql
  CONSTRUCT { ?kota a ex:Kota . }
  WHERE { ?kota wdt:P31/wdt:P279* ?jenis . ?jenis wdt:P279* ?induk . }
  LIMIT 10
  ```
  Kedua ujung jalur `*` berupa variabel, tanpa IRI jangkar. Mesin harus menelusuri seluruh hierarki `subclass of` Wikidata dari jutaan item sebagai titik awal, sehingga ruang pencarian membengkak dan sangat mungkin timeout. Versi aslinya hanya menelusuri turunan satu kelas (`wd:Q515`).

### Diskusi 1 - Taksonomi berubah
Hasil materialisasi yang disimpan di graf produksi adalah salinan statis kesimpulan, bukan aturan hidup. Di Bagian C, `kampus_v4.ttl` berisi 13 triple campuran: 7 triple asli (6 dari `kampus.ttl` plus Rina) dan 6 triple turunan. Dari berkas itu saja saya tidak bisa melihat mana yang asli dan mana yang turunan. Bila setahun kemudian `ex:Dosen` bukan lagi subkelas `foaf:Person`, triple yang kini salah adalah `ex:budi a foaf:Person`, `ex:sari a foaf:Person`, dan `ex:rina a foaf:Person` (dan `a ex:Dosen` bila `DosenTetap` dilepas dari `Dosen`), sedangkan `ex:rudi a foaf:Person` masih benar karena lewat `ex:Tendik`. Dengan `kampus_turunan.ttl` (6 triple) dari C2, saya cukup menjalankan ulang `ATURAN` pada taksonomi baru, lalu membandingkan hasilnya dengan berkas lama (selisih himpunan): triple yang ada di berkas lama tetapi tidak di hasil baru adalah triple yang kini salah. Karena turunan sudah terpisah, saya bisa menghapusnya tanpa menyentuh data asli. Pada `kampus_v4.ttl` saya harus menebak mana yang boleh dihapus. Pelajarannya: simpan turunan terpisah atau pakai reasoner (Pertemuan 12).

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk dashboard populasi kota saya memakai SELECT, karena dashboard butuh tabel angka per kota. Pada Demo A, SELECT LIMIT 10 memberi 10 baris untuk 10 kota, mudah dihitung dan digambar. Kalau kota punya dua nilai populasi, SELECT menampilkannya sebagai dua baris yang tetap bisa dipilih (misalnya yang terbaru), sedangkan CONSTRUCT menggabung pola kembar sehingga jumlah triple tidak lagi sebanding dengan jumlah baris (30 triple untuk 10 baris hanya bila tidak ada kembar). Untuk menggabungkan data kota dari tiga sumber saya memakai CONSTRUCT, karena hasilnya graf dengan kosakata seragam (`ex:Kota`, `ex:populasi`) yang bisa disatukan dan di-query ulang. Namun `rusak_b.rq` menunjukkan risikonya: satu orang punya dua `ex:nama` (`@en` dan `@fr`/`@id`) yang tampak sama tetapi berbeda sebagai literal, sehingga 3 orang menjadi 5 triple. Jadi saat menggabungkan sumber, saya harus memilih satu bahasa lewat `FILTER ( LANG(?n) = "en" )` atau `STR()`, serta memakai `|` atau `VALUES` untuk menyatukan predikat berbeda antar sumber. Singkatnya: SELECT untuk membaca dan menampilkan, CONSTRUCT untuk membentuk dan menyatukan graf.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1 | Bagian A: LIMIT 10 menghasilkan 30 triple (10 solution x 3 pola) dan LIMIT 30 menghasilkan 90. Template dicetak sekali per solution; triple kembar akan digabung (bagian C: 7 hasil, 4 baru). |
| 2 | Bagian B2: 16 film tanpa `releaseDate` mencetak 3 triple masing-masing (48 total) tanpa error; `rusak_a.rq` menghasilkan 0 triple karena `?film` tak terikat, tanpa error. |
| 3 | `rusak_b.rq` memakai `foaf:name\|rdfs:label\|schema:name` dan `VALUES` untuk tiga orang; hasilnya 5 triple dari 3 orang, menjadi 3 setelah `FILTER LANG`. |
| 4 | `rusak_c.rq` memberi 0, sedangkan `perbaikan_c.rq` dengan `a/rdfs:subClassOf*` memberi 3 (Medan, Surabaya, Tomok) tanpa menyebut `ex:Kota` atau `ex:Desa`; `kampus.ttl` memberi `foaf:Person` 0 menjadi 3. |
| 5 | Bagian C: `demo_d.py` menyimpan kesimpulan (Person 0 menjadi 3), tetapi Rina tetap 3; setelah `materialisasi_ulang.py` dijalankan ulang menjadi 4 (Putaran 2). |
