# Pertemuan 12 - Inferensi dan Reasoning

## Langkah 1 - Closure dengan tangan
| # | Triple turunan | Aturan | Premis |
|---|----------------|--------|--------|
| [isi] | [isi] | [isi] | [isi] |
- Jumlah triple turunan bermakna: [isi]
- Triple yang baru ditemukan di putaran kedua: [isi]
- Triple asserted yang tidak menurunkan apa pun, dan alasannya: [isi]

## Langkah 2 - Tebak lalu cek
| Soal | Profil | Tebakan | Hasil mesin | Penjelasan bila meleset |
|------|--------|---------|-------------|-------------------------|
| A | RDFS | 3 baris | 3 baris | Tepat — `RDFS` mengenali `rdfs:subClassOf`, sehingga subkelas `ex:Mahasiswa` dan `ex:Dosen` ikut diturunkan menjadi `ex:Orang` bersama individu `ex:Orang` langsung. |
| B | OWL RL | 4 baris | 10 baris | Meleset 6 baris karena lupa menghitung seluruh pasangan transitif berantai; pada rantai 4 relasi `ex:beradaDi` berurutan, `OWL RL` menurunkan semua lompatan tidak langsung ($4 + 3 + 2 + 1 = 10$ pasangan). |
| C | RDFS | 1 baris | 0 baris | Meleset karena profil `RDFS` tidak mengenali aksioma `owl:inverseOf`, sehingga relasi `ex:membimbing` tidak dibalik menjadi `ex:dibimbing` dan diabaikan tanpa error. |
| C | OWL RL | 1 baris | 1 baris | Tepat — `OWL RL` memproses `owl:inverseOf` sehingga relasi `ex:membimbing` berhasil diturunkan menjadi `ex:dibimbing`. |
| D | OWL RL | False | False | Tepat — `False` berarti fakta `ex:medan a ex:Tempat` **tidak diketahui / tidak dapat dibuktikan** dari graf saat ini (prinsip dunia terbuka / *Open World Assumption*), bukan berarti Medan salah atau bukan tempat. |

## Langkah 3 - Reasoner pada graf kampus
- Berkas sumber dan IRI dasar graf: [isi]
- Asserted / closure / inferred / bermakna: [isi] / [isi] / [isi] / [isi]
- Triple di v4 yang tidak ada di asserted: [isi]
- Turunan yang muncul karena domain dan range ex:mengajar: [jawaban]
- Bila menambah dosen baru: [jawaban]

## Langkah 4 - Wikidata
- ?n Q8 / Q9: [isi] / [isi]
- Penyebab selisih: [isi]
- Satu subkelas yang menyumbang selisih: [isi]
- WDQS: materialisasi, saat query, atau tidak keduanya: [jawaban]

## Langkah 5 - Konsistensi
- Pesan galat RDFS / OWL RL: [isi] / [isi]
- Individu yang disebut pesan: [isi]
- Setelah baris terbalik dihapus: [isi]
- Isi laporan_kelas.csv sebelum dan sesudah: [isi]
- Dari mana dosen menjadi mata kuliah: [jawaban]

## Refleksi
1. Mengapa graf asserted disimpan terpisah dari graf inferred, dan apa akibatnya bila keduanya dicampur seperti kampus_usu_v4.ttl?
2. Pada Langkah 2, profil RDFS tidak memberi tahu bahwa aksioma OWL diabaikan. Bagaimana Anda akan memastikan profil yang dipakai sudah tepat untuk data Anda?
3. Kapan Anda memilih menulis jalur seperti wdt:P279* di query, dan kapan memilih menjalankan reasoner lalu menyimpan closure?