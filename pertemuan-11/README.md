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
- Berkas sumber dan IRI dasar graf: [isi]
- Kelas dosen dan properti nama: [isi]
- Triple hasil pemetaan: [isi]
- foaf:Person sebelum / sesudah: [isi] / [isi]
- Triple asli vs triple turunan: [jawaban]
- Dosen baru setelah program selesai: [jawaban]

## Langkah 4 - Wikidata
- Jumlah triple Q6: [isi]
- Jumlah baris Q6 versi SELECT: [isi]
- Penjelasan perbedaan: [isi]
- Q7 dengan + vs *: [isi]
- Kelas yang mengejutkan dan alasannya: [isi]

## Langkah 5 - Graf dari Python
- Jumlah triple universitas.ttl: [isi]
- Jumlah baris universitas_per_kota.csv: [isi]
- setReturnFormat(TURTLE): [isi]
- Graph().parse(data=...): [isi]
- Mengapa q_kota tidak memanggil endpoint: [isi]

## Refleksi
1. Mengapa jumlah triple hasil CONSTRUCT bisa lebih kecil dari jumlah baris SELECT dengan WHERE yang sama?
    Query SELECT menghasilkan tabel yang dapat memuat baris berulang sesuai kombinasi variabel di klausa WHERE, sedangkan hasil CONSTRUCT membentuk graf RDF yang bersifat himpunan (set) sehingga triple yang identik otomatis digabung (deduplikasi). Selain itu, jika pola di CONSTRUCT hanya memakai sebagian variabel dari WHERE (seperti ?mk a ex:MataKuliahAktif tanpa ?d), variasi nilai variabel lain yang tidak ikut dicetak akan menghasilkan triple yang sama persis.

2. Bila taksonomi di graf kampus Anda berubah bulan depan, apa yang terjadi pada triple turunan di kampus_usu_v4.ttl?
    Triple turunan yang sudah tersimpan di file statis kampus_usu_v4.ttl tidak akan berubah secara otomatis sehingga isinya menjadi usang dan tidak sinkron dengan taksonomi terbaru. Untuk memperbaruinya, query CONSTRUCT (atau reasoner) harus dijalankan ulang pada graf sumber yang baru, lalu hasilnya disimpan kembali.

3. Kapan Anda menyimpan hasil query sebagai tabel (CSV), dan kapan sebagai graf (Turtle)?
    Tabel (CSV): Dipilih saat data akhir digunakan untuk pelaporan, rekapitulasi angka, tampilan antarmuka aplikasi, atau diolah di perangkat lunak spreadsheet dan basis data relasional.
    Graf (Turtle): Dipilih saat hasil query berupa fakta atau relasi baru yang ingin digabungkan kembali ke dalam knowledge graph, dibagikan sebagai Linked Data, atau di-query ulang menggunakan SPARQL dan reasoner. 