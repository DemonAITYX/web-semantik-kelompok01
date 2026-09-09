# Latihan Pertemuan 3 - JSON-LD dan Structured Data

## Identitas
- Nama: Albariqi Deanda Tarigan
- NIM: 251402037

## Struktur Hasil
- `profil_saya.jsonld`
- `profil_perbaikan.jsonld`
- `seminar.html`
- folder `screenshots`


## 1. JSON Biasa dan JSON-LD
1. Perbedaan fungsi kunci: Pasangan `nama`/`pekerjaan` bersifat lokal dan hanya dikenali oleh internal aplikasi, sedangkan `name`/`jobTitle` merupakan kunci standar global Schema.org yang dapat dipahami secara universal oleh mesin pencari dan sistem lain.
2. Fungsi `@context`, `@type`, dan `@id`: `@context` mendefinisikan acuan kosa kata standar global (seperti Schema.org), `@type` menentukan tipe atau kategori entitas data (misalnya `Person`), dan `@id` menyediakan identitas unik berupa IRI/URL agar entitas dapat dirujuk di *Web of Data*.
3. Node tanpa `@id`: Node tersebut akan dianggap sebagai *Blank Node* (node anonim); datanya tetap valid secara sintaksis, namun tidak memiliki URI unik yang dapat ditautkan atau dihubungkan oleh dokumen luar.
