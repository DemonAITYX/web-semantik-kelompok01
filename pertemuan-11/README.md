# Pertemuan 11 - CONSTRUCT dan Hierarki Data

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

## Langkah 2 - Tebak lalu cek
| Soal | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|---------|-------------|-------------------------|
| A    | 3 baris | 3 baris | Operator `*` (*zero-or-more*) menyertakan panjang jalur 0 langkah (`ex:Dosen` itu sendiri) serta 1 langkah (`ex:DosenTetap` dan `ex:DosenTamu`). |
| B    | 4 baris (duplikat: `ex:sari`) | 4 baris | `ex:sari` memiliki dua kelas (`ex:DosenTetap` dan `ex:DosenTamu`) yang masing-masing punya jalur ke `ex:Pegawai`, sehingga `SELECT` mencetak `ex:sari` sebanyak 2 kali bersama `ex:budi` dan `ex:rudi`. |
| C    | 3 triple | 3 triple | Hasil `CONSTRUCT` berupa graf RDF (himpunan), sehingga triple duplikat `ex:sari a ex:Pegawai` otomatis digabung menjadi satu. |
| D    | 0 triple (tanpa error) | 0 triple | Karena `ex:rudi` tidak memiliki `ex:nama`, variabel `?n` menjadi *unbound* (tidak terikat), sehingga triple pada template `CONSTRUCT` diabaikan tanpa pesan error. |

## Langkah 3 - Graf kampus lokal
- Berkas sumber dan IRI dasar graf: `../pertemuan-09/kampus_usu_v2.ttl` (v3 belum ada), 30 triple awal; IRI dasar `https://vshndrr-code.github.io/web-semantik/251402019/usu#`
- Kelas dosen dan properti nama: `ex:Lecturer` dan `foaf:name`
- Triple hasil pemetaan: 6 (3 dosen x 2 triple: `a schema:Person` dan `schema:name`)
- foaf:Person sebelum / sesudah: 0 / 3 (sama dengan jumlah dosen)
- Triple asli vs triple turunan: Bisa. Triple asli adalah 30 triple dari `kampus_usu_v2.ttl` ditambah 2 triple hierarki hasil `INSERT DATA` (`ex:Lecturer rdfs:subClassOf ex:Pegawai` dan `ex:Pegawai rdfs:subClassOf foaf:Person`) yang kita tulis sendiri. Triple turunan ada 6, yaitu `a ex:Pegawai` dan `a foaf:Person` untuk tiap dosen (`ex:dedy`, `ex:ida`, `ex:umay`), hasil CONSTRUCT lalu ditambahkan ke graf. Di berkas Turtle keduanya tampak sama, tidak ada penanda mana yang turunan.
- Dosen baru setelah program selesai: Dosen baru tidak otomatis menjadi `foaf:Person` atau `ex:Pegawai`. Materialisasi adalah salinan statis yang dihitung sekali, jadi program harus dijalankan ulang agar triple turunan untuk dosen baru dibuat.

## Langkah 4 - Wikidata
- Jumlah triple Q6: 118
- Jumlah baris Q6 versi SELECT: 50
- Penjelasan perbedaan: Jumlah triple CONSTRUCT adalah 118, sedangkan SELECT menghasilkan 50 baris. Secara teori, 50 baris menghasilkan 150 triple karena setiap universitas memiliki tiga informasi, yaitu tipe, nama, dan lokasi. Namun, hasil CONSTRUCT hanya menghasilkan 118 triple karena RDF Graph menghilangkan triple duplikat. Artinya, beberapa triple yang sama hanya dihitung satu kali.
Kesimpulan: Jumlah triple tidak sama dengan 3 × jumlah baris karena CONSTRUCT menghasilkan graf RDF yang hanya menyimpan triple unik.

- Q7 dengan + vs *: P279+ mencari kelas yang memiliki satu atau lebih hubungan subclass (subkelas) menuju Universitas. Sedangkan, P279* mencari kelas dengan nol atau lebih hubungan subclass. Artinya, kelas Universitas itu sendiri juga dapat ikut muncul dalam hasil.
Meskipun keduanya menghasilkan 30 results, cara penelusuran hierarkinya berbeda.

- Kelas yang mengejutkan dan alasannya: Salah satu kelas yang mengejutkan adalah _'Coast Guard Academy'_ karena merupakan institusi pendidikan khusus yang melatih calon personel penjaga pantai. Kelas ini bisa menjadi subkelas universitas karena memiliki fungsi sebagai lembaga pendidikan tinggi yang memberikan pendidikan dan pelatihan profesional. Hal ini menunjukkan bahwa hierarki Wikidata tidak hanya mencakup universitas umum, tetapi juga institusi pendidikan khusus.

## Langkah 5 - Graf dari Python
- Jumlah triple universitas.ttl: 114 (sesuai keluaran `Triple dari Wikidata:` saat program dijalankan). Jumlah ini berbeda dari Q6 pada Langkah 4 (118) karena Q6 dijalankan di browser pada waktu yang berbeda; data Wikidata terus berubah dan query memakai `LIMIT 50` tanpa `ORDER BY`, sehingga 50 solution yang terambil bisa berbeda di tiap eksekusi
- Jumlah baris universitas_per_kota.csv: 47 (tanpa baris header)
- setReturnFormat(TURTLE): Meminta endpoint Wikidata mengembalikan hasil query CONSTRUCT dalam format Turtle (graf RDF), bukan JSON atau XML, sehingga hasilnya dapat langsung dibaca sebagai graf.
- Graph().parse(data=...): Membaca teks Turtle yang dikembalikan endpoint menjadi graf rdflib di memori, sehingga graf dapat disimpan ke `universitas.ttl` dan di-query secara lokal.
- Mengapa q_kota tidak memanggil endpoint: Karena `q_kota` dijalankan dengan `g.query(...)` pada graf lokal yang sudah dimuat di memori (dan disimpan di `universitas.ttl`), bukan dikirim ke endpoint Wikidata. Endpoint hanya dipanggil satu kali, yaitu saat Q6 dikirim; `universitas.ttl` berfungsi sebagai cache.

## Refleksi
1. Mengapa jumlah triple hasil CONSTRUCT bisa lebih kecil dari jumlah baris SELECT dengan WHERE yang sama?
    Query SELECT menghasilkan tabel yang dapat memuat baris berulang sesuai kombinasi variabel di klausa WHERE, sedangkan hasil CONSTRUCT membentuk graf RDF yang bersifat himpunan (set) sehingga triple yang identik otomatis digabung (deduplikasi). Selain itu, jika pola di CONSTRUCT hanya memakai sebagian variabel dari WHERE (seperti ?mk a ex:MataKuliahAktif tanpa ?d), variasi nilai variabel lain yang tidak ikut dicetak akan menghasilkan triple yang sama persis.

2. Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di kampus_usu_v4.ttl?
    Triple turunan yang sudah tersimpan di file statis kampus_usu_v4.ttl tidak akan berubah secara otomatis sehingga isinya menjadi usang dan tidak sinkron dengan taksonomi terbaru. Untuk memperbaruinya, query CONSTRUCT (atau reasoner) harus dijalankan ulang pada graf sumber yang baru, lalu hasilnya disimpan kembali.

3. Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?
    Tabel (CSV): Dipilih saat data akhir digunakan untuk pelaporan, rekapitulasi angka, tampilan antarmuka aplikasi, atau diolah di perangkat lunak spreadsheet dan basis data relasional.
    Graf (Turtle): Dipilih saat hasil query berupa fakta atau relasi baru yang ingin digabungkan kembali ke dalam knowledge graph, dibagikan sebagai Linked Data, atau di-query ulang menggunakan SPARQL dan reasoner. 
