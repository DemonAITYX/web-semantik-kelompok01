# Pertemuan 7 - Serialisasi RDF


## 1. Membandingkan Serialisasi RDF

| Format | Kekuatan utama | Skenario tepat |
| :--- | :--- | :--- |
| **Turtle** | Ringkas dan mudah dibaca manusia | Saat menulis ontologi atau data RDF secara manual, keperluan pembelajaran, dan dokumentasi yang membutuhkan validasi manusia. |
| **JSON-LD** | Cocok web/API dan HTML | Saat menyematkan data terstruktur (seperti Schema.org) ke dalam halaman web untuk SEO atau bertukar data terstruktur melalui REST API modern. |
| **RDF/XML** | Kompatibilitas data lama | Saat berintegrasi dengan sistem (*legacy system*) atau pustaka lawas yang secara ketat hanya mendukung pemrosesan berbasis XML. |
| **N-Triples** | Satu triple per baris; stabil untuk diff | Saat memproses dataset skala besar (*bulk loading*) atau menyimpan data RDF dalam *version control* (seperti Git) agar perubahan mudah dilacak per baris. |
| **N-Quads** | Menambahkan konteks graf | Saat perlu mengekspor/mengimpor dataset yang berisi banyak graf bernama (*named graphs*) antar *triplestore* tanpa menghilangkan konteks asalnya. |

## Artefak
- Graf asal: 28 triple (sebelum ditambahkan reifikasi klasik) / 33 triple (setelah reifikasi klasik)
- Format ekspor: Turtle, JSON-LD, N-Triples
- Named graph: `https://vshndrr-code.github.io/web-semantik/251402019/graph/kampus` dan `https://vshndrr-code.github.io/web-semantik/251402019/graph/fakultas` (dari file `kampus_tergabung.trig`)

## Reifikasi dan provenance

- Triple yang dianotasi: `ex:ida ex:mengajar ex:web_semantik`
- Creator: `ex:ida`
- Date: `2026-10-01` (tipe: `xsd:date`)
- Source: `"Data akademik kampus"`

## Perbandingan

* **Format paling mudah dibaca manusia:** Turtle (TTL), karena sintaksnya sederhana, ringkas, dan mudah dipahami saat membaca hubungan antar-resource dalam bentuk triple RDF.
* **Format untuk HTML/API:** JSON-LD, karena menggunakan struktur JSON yang mudah diintegrasikan dengan aplikasi web, HTML, dan API.
* **Perbedaan reifikasi klasik dan RDF-star:** Reifikasi klasik menggunakan beberapa triple tambahan untuk menjelaskan suatu pernyataan RDF, sedangkan RDF-star memungkinkan triple dimasukkan langsung ke dalam triple lain sehingga informasi tambahan dapat ditulis dengan lebih ringkas.

## Refleksi

1. **Mengapa named graph berguna saat menggabungkan data dari sumber berbeda?**

   Named graph berguna untuk mengelompokkan triple berdasarkan sumber atau konteksnya. Dengan demikian, data dari berbagai sumber dapat digabungkan tanpa kehilangan informasi mengenai asal kelompok data tersebut.

2. **Mengapa provenance penting untuk sebuah triple?**

   Provenance penting untuk mengetahui asal-usul suatu triple, siapa yang menyatakannya, kapan informasi tersebut dicatat, dan sumber yang digunakan. Informasi ini membantu memeriksa keakuratan serta kepercayaan terhadap data.

3. **Format apa yang Anda pilih untuk git diff, dan mengapa?**

   Saya memilih format Turtle (TTL) karena sintaksnya ringkas dan mudah dibaca. Setiap triple ditulis dengan jelas sehingga perubahan berupa penambahan, penghapusan, atau pengeditan fakta lebih mudah diperiksa melalui `git diff`.
