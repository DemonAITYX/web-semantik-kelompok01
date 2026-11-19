# Pertemuan 12 - Inferensi dan Reasoning

## Langkah 1 - Closure dengan tangan
| # | Triple turunan | Aturan | Premis |
|---|----------------|--------|--------|
| 1 | `ex:budi a ex:Dosen` | rdfs2 (putaran 1) | domain `ex:membimbing` = `ex:Dosen` + `ex:budi ex:membimbing ex:andi` |
| 2 | `ex:andi a ex:Mahasiswa` | rdfs3 (putaran 1) | range `ex:membimbing` = `ex:Mahasiswa` + `ex:budi ex:membimbing ex:andi` |
| 3 | `ex:budi ex:mengenal ex:andi` | rdfs7 (putaran 1) | `ex:membimbing` ⊑ `ex:mengenal` + `ex:budi ex:membimbing ex:andi` |
| 4 | `ex:sari a ex:Dosen` | rdfs9 (putaran 1) | `ex:DosenTamu` ⊑ `ex:Dosen` + `ex:sari a ex:DosenTamu` |
| 5 | `ex:DosenTamu rdfs:subClassOf ex:Pegawai` | rdfs11 (putaran 1) | `ex:DosenTamu` ⊑ `ex:Dosen` + `ex:Dosen` ⊑ `ex:Pegawai` |
| 6 | `ex:Dosen rdfs:subClassOf ex:Orang` | rdfs11 (putaran 1) | `ex:Dosen` ⊑ `ex:Pegawai` + `ex:Pegawai` ⊑ `ex:Orang` |
| 7 | `ex:budi a ex:Pegawai` | rdfs9 (putaran 2) | `ex:Dosen` ⊑ `ex:Pegawai` + #1 `ex:budi a ex:Dosen` |
| 8 | `ex:sari a ex:Pegawai` | rdfs9 (putaran 2) | `ex:DosenTamu` ⊑ `ex:Pegawai` (#5) + `ex:sari a ex:DosenTamu` |
| 9 | `ex:budi a ex:Orang` | rdfs9 (putaran 2) | `ex:Dosen` ⊑ `ex:Orang` (#6) + #1 `ex:budi a ex:Dosen` |
| 10 | `ex:sari a ex:Orang` | rdfs9 (putaran 2) | `ex:Dosen` ⊑ `ex:Orang` (#6) + #4 `ex:sari a ex:Dosen` |
| 11 | `ex:andi a ex:Orang` | rdfs9 (putaran 2) | `ex:Mahasiswa` ⊑ `ex:Orang` + #2 `ex:andi a ex:Mahasiswa` |
| 12 | `ex:DosenTamu rdfs:subClassOf ex:Orang` | rdfs11 (putaran 2) | `ex:DosenTamu` ⊑ `ex:Pegawai` (#5) + `ex:Pegawai` ⊑ `ex:Orang` |
- **Jumlah triple turunan bermakna:** 12 (6 pada putaran pertama, 6 pada putaran kedua). Putaran ketiga tidak menghasilkan triple baru, sehingga closure sudah tercapai.
- **Triple yang baru ditemukan di putaran kedua:** #7–#12. Yang paling penting ialah `ex:budi a ex:Orang`, `ex:sari a ex:Orang`, dan `ex:andi a ex:Orang`, yang baru bisa dicapai setelah subkelas `ex:Dosen` dan `ex:DosenTamu` tersambung ke `ex:Orang` melalui `ex:Pegawai`.
- **Triple asserted yang tidak menurunkan apa pun:** `ex:andi a ex:MahasiswaBerprestasi`. Alasannya, tidak ada aksioma `rdfs:subClassOf` yang berawal dari `ex:MahasiswaBerprestasi`, sehingga rdfs9 tidak dapat diterapkan. Semua triple asserted RDFS lainnya ikut menurunkan minimal satu triple.
- **triple umum** seperti `x a rdfs:Resource` dan `ex:Dosen rdfs:subClassOf ex:Dosen` sengaja diabaikan sesuai instruksi.

## Langkah 2 - Tebak lalu cek
| Soal | Profil | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|--------|---------|-------------|-------------------------|
| A | RDFS | 3 baris | 3 baris | Tepat — `RDFS` mengenali `rdfs:subClassOf`, sehingga subkelas `ex:Mahasiswa` dan `ex:Dosen` ikut diturunkan menjadi `ex:Orang` bersama individu `ex:Orang` langsung. |
| B | OWL RL | 4 baris | 10 baris | Meleset 6 baris karena lupa menghitung seluruh pasangan transitif berantai; pada rantai 4 relasi `ex:beradaDi` berurutan, `OWL RL` menurunkan semua lompatan tidak langsung ($4 + 3 + 2 + 1 = 10$ pasangan). |
| C | RDFS | 1 baris | 0 baris | Meleset karena profil `RDFS` tidak mengenali aksioma `owl:inverseOf`, sehingga relasi `ex:membimbing` tidak dibalik menjadi `ex:dibimbing` dan diabaikan tanpa error. |
| C | OWL RL | 1 baris | 1 baris | Tepat — `OWL RL` memproses `owl:inverseOf` sehingga relasi `ex:membimbing` berhasil diturunkan menjadi `ex:dibimbing`. |
| D | OWL RL | False | False | Tepat — `False` berarti fakta `ex:medan a ex:Tempat` **tidak diketahui / tidak dapat dibuktikan** dari graf saat ini (prinsip dunia terbuka / *Open World Assumption*), bukan berarti Medan salah atau bukan tempat. |

## Langkah 3 - Reasoner pada graf kampus

- **Berkas sumber dan IRI dasar graf:** `pertemuan-09/kampus_usu_v2.ttl` dan `https://vshndrr-code.github.io/web-semantik/251402019/usu#`
- **Asserted / closure / inferred / bermakna:** 32 / 77 / 45 / 1
- **Triple di v4 yang tidak ada di asserted:** 8
- **Turunan yang muncul karena domain dan range `ex:mengajar`:** Domain `ex:mengajar` adalah `ex:Lecturer`, sedangkan range-nya adalah `ex:Course`. Domain menyimpulkan bahwa subjek yang menggunakan properti `ex:mengajar` merupakan dosen, sedangkan range menyimpulkan bahwa objeknya merupakan mata kuliah. Salah satu triple turunan yang muncul adalah `ex:kecerdasan_buatan rdf:type ex:Course`.
- **Bila menambah dosen baru:** Saya perlu menambahkan individu dosen baru ke dalam graf asserted, memberikan tipe `ex:Lecturer`, serta menambahkan relasi `ex:mengajar` jika dosen tersebut mengajar mata kuliah. Setelah itu, reasoner dijalankan kembali agar menghasilkan triple turunan terbaru.

**Screenshot output:** `screenshots/output-lokal.png`

## Langkah 4 - Wikidata
- ?n Q8 / Q9: 877 / 1343
- Penyebab selisih: Q9 lebih besar 466 karena jalur `wdt:P31/wdt:P279*` ikut menghitung universitas yang bertipe subkelas dari universitas, sedangkan Q8 (`wdt:P31 wd:Q3918`) hanya menghitung item yang tipenya langsung "universitas". Banyak institusi di Wikidata diberi tipe yang lebih spesifik, misalnya "universitas swasta" atau "politeknik", dan tidak pernah ditulis sebagai `P31 wd:Q3918`. Hierarki kelas yang disimpan sama untuk kedua query. Bedanya, Q8 tidak menelusurinya dan Q9 menelusurinya lewat jalur yang kita tulis sendiri.
- Satu subkelas yang menyumbang selisih: Universitas swasta (`wd:Q902104`), yang berstatus subkelas universitas (cocok dengan hasil Q7 Pertemuan 11) dan di Indonesia dipakai sebagai tipe langsung oleh 320 item. Subkelas lain: politeknik (`wd:Q845392`, 375 item) dan universitas negeri (`wd:Q875538`, 73 item). Angka ini dihitung per subkelas, jadi item yang punya beberapa tipe bisa terhitung lebih dari sekali.
- WDQS: materialisasi, saat query, atau tidak keduanya: Tidak keduanya. WDQS tidak menurunkan triple `P31` baru untuk subkelas (bukan materialisasi) dan tidak menalar otomatis saat query (bukan penalaran saat query). Ia hanya mencocokkan pola yang ada, sehingga Q8 tidak menemukan subkelas. Aturan rdfs9 (instance dari subkelas juga instance dari superkelas) di Q9 sebenarnya dijalankan oleh kita sendiri lewat jalur `wdt:P279*` yang kita tulis di query, bukan oleh WDQS.

## Langkah 5 - Konsistensi Graf

- **Pesan galat RDFS / OWL RL:** RDFS menghasilkan 0 pesan galat, sedangkan OWL RL menghasilkan minimal 1 pesan galat pada pengujian pertama.
- **Individu yang disebut pesan:** `ida` dan `web_semantik`. Keduanya terlibat dalam pelanggaran aturan disjoint class.
- **Setelah baris terbalik dihapus:** RDFS dan OWL RL sama-sama menghasilkan 0 pesan galat karena tidak ditemukan lagi individu yang termasuk ke dalam dua kelas yang saling bertentangan.

### Isi laporan_kelas.csv sebelum dan sesudah

Sebelum triple terbalik dihapus:

| Kelas | Asserted | RDFS | OWL RL |
|---|---:|---:|---:|
| Lecturer | 3 | 4 | 4 |
| Pegawai | 0 | 4 | 4 |
| Course | 3 | 4 | 4 |

Sesudah triple terbalik dihapus:

| Kelas | Asserted | RDFS | OWL RL |
|---|---:|---:|---:|
| Lecturer | 3 | 3 | 3 |
| Pegawai | 0 | 3 | 3 |
| Course | 3 | 3 | 3 |

### Dari mana dosen menjadi mata kuliah?

Reasoner mengetahui bahwa dosen juga menjadi mata kuliah melalui aturan domain dan range pada properti `ex:mengajar`. Ketika triple yang salah `ex:web_semantik ex:mengajar ex:ida` ditambahkan, aturan range menyimpulkan bahwa `ex:ida` merupakan anggota kelas `ex:Course`. Padahal, `ex:ida` sudah termasuk kelas `ex:Lecturer` yang merupakan subclass dari `ex:Pegawai`. Karena `ex:Pegawai` dinyatakan saling lepas dengan `ex:Course` menggunakan `owl:disjointWith`, kondisi tersebut dianggap sebagai inkonsistensi oleh OWL RL.

Profil RDFS tidak melaporkan kesalahan tersebut karena RDFS tidak memiliki mekanisme pemeriksaan konflik kelas melalui `owl:disjointWith`. Setelah triple yang sengaja dibalik dihapus, inkonsistensi tidak lagi ditemukan.
<br>

## Refleksi
1. Mengapa graf asserted disimpan terpisah dari graf inferred, dan apa akibatnya bila keduanya dicampur seperti kampus_usu_v4.ttl?
   - Jawaban: Graf asserted berisi fakta yang memang dicatat sumbernya dan menjadi acuan audit. Graf inferred hanya turunan yang bergantung pada profil dan aturan tertentu. Bila keduanya dicampur, kita tidak bisa lagi membedakan fakta yang dicatat dari fakta turunan. Akibatnya, menghapus triple asserted yang keliru tidak ikut menghapus turunannya sehingga data menjadi basi, dan konflik antar profil sulit ditelusuri. Pemisahan ini juga membuat closure bisa dihitung ulang kapan saja tanpa merusak sumber.

<br>

2. Pada Langkah 2, profil RDFS tidak memberi tahu bahwa aksioma OWL diabaikan. Bagaimana Anda akan memastikan profil yang dipakai sudah tepat untuk data Anda?
   - Jawaban: Pertama, periksa data dengan mencari predikat dan tipe dari namespace `owl:` (misalnya `owl:inverseOf`, `owl:TransitiveProperty`, `owl:disjointWith`). Bila ada, profil harus minimal OWL RL. Bila hanya RDFS, profil RDFS sudah cukup. Kedua, jangan menganggap "tidak ada error" sebagai bukti bahwa semua aksioma diproses, karena reasoner bisa diam. Ketiga, uji dengan contoh kecil seperti pada Langkah 2: buat tebakan dulu, lalu bandingkan dengan hasil mesin. Bila selisihnya muncul, berarti profil belum sesuai.

<br>

3. Kapan Anda memilih menulis jalur seperti wdt:P279* di query, dan kapan memilih menjalankan reasoner lalu menyimpan closure?
   - Jawaban: Saya memilih jalur `wdt:P279*` bila data sumber besar, sering berubah, atau tidak boleh disalin, misalnya pada WDQS yang tidak menyimpan closure dan menghitung relasi saat query. Saya memilih menjalankan reasoner lalu menyimpan closure bila data lokal relatif stabil, banyak query membutuhkan hasil turunan, dan kita perlu query yang sederhana serta cepat. Trade-off-nya: closure bisa basi bila data sumber berubah dan harus dihitung ulang, sedangkan jalur properti bisa lambat pada data besar.
