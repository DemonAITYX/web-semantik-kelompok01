# Langkah 7 - Menuliskan XPath

| No. | Kebutuhan | XPath |
|---|---|---|
| 1 | Memilih semua elemen buku | `/katalog/buku` |
| 2 | Memilih semua judul buku | `/katalog/buku/judul` |
| 3 | Memilih buku pertama | `/katalog/buku[1]` |
| 4 | Memilih semua buku yang mempunyai atribut ISBN | `/katalog/buku[@isbn]` |
| 5 | Memilih buku dengan harga lebih dari 100000 | `/katalog/buku[harga > 100000]` |
| 6 | Mengambil nilai teks dari seluruh elemen pengarang | `/katalog/buku/pengarang/text()` |