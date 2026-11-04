# Pertemuan 9 - SPARQL Dasar: Tell & Ask dan Endpoint
## Langkah 1 – Tabel Binding

| Tahap | ?dosen | ?mk | ?namaMK |
|---|---|---|---|
| Pola 1, baris 1 | ex:budi | ex:tif2305 | – |
| Pola 1, baris lain | ex:sari | ex:tif2410 | – |
| Pola 1, baris lain | ex:sari | ex:tif2305 | – |
| Pola 2 | – | ex:tif2305 | "Web Semantik" |
| Pola 2 | – | ex:tif2410 | "Data Mining" |
| Hasil akhir | ex:budi | ex:tif2305 | "Web Semantik" |
| Hasil akhir | ex:sari | ex:tif2410 | "Data Mining" |
| Hasil akhir | ex:sari | ex:tif2305 | "Web Semantik" |

Jumlah baris hasil akhir : 3 baris

Peran `?mk` : berfungsi sebagai penghubung (join variable) antara Pola 1 dan Pola 2. Kedua pola digabungkan berdasarkan nilai `?mk` yang sama. Meskipun `?mk` tidak ditampilkan karena tidak dicantumkan dalam bagian `SELECT`, variabel tersebut tetap digunakan untuk mencocokkan data pada kedua pola di bagian `WHERE`.


## Langkah 2 – ASK dan Asumsi Dunia Terbuka

