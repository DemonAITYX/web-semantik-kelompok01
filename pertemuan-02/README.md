## 2. Analisis Kesalahan XML

| No | Bagian yang Salah | Alasan | Perbaikan |
|---|---|---|---|
| 1 | `<nama>Budi Santoso</Nama>` | XML bersifat *case-sensitive*. Tag pembuka menggunakan huruf kecil, sedangkan tag penutup diawali huruf kapital. | Ubah tag penutup menjadi huruf kecil: `</nama>` |
| 2 | `<angkatan>2024` | Elemen tidak memiliki tag penutup (*missing closing tag*). Setiap elemen XML wajib ditutup. | Tambahkan tag penutup di akhir nilai menjadi: `<angkatan>2024</angkatan>` |
| 3 | `<deskripsi>Saya suka AI & Web Semantik</deskripsi>` | Terdapat karakter khusus `&` yang dilarang ditulis langsung dalam XML (harus di-*escape*). | Ganti karakter `&` dengan entitas XML yang valid, yaitu `&amp;` |

### Kode XML Setelah Diperbaiki:
```xml
<mahasiswa>
    <nama>Budi Santoso</nama>
    <angkatan>2024</angkatan>
    <hobi>Programming</hobi>
    <hobi>Membaca</hobi>
    <deskripsi>Saya suka AI &amp; Web Semantik</deskripsi>
</mahasiswa>





## 5. Pertanyaan Evaluasi

#### 1. Apa perbedaan utama XML dan HTML?

| XML | HTML |
|---|---|
| Digunakan untuk menyimpan dan mengatur data | Digunakan untuk menampilkan dan menyusun halaman web |
| Fokus pada struktur dan isi data | Fokus pada tampilan dan penyajian data |
| Tag dapat dibuat sesuai kebutuhan | Tag menggunakan elemen yang sudah ditentukan |
| Data dapat dibaca dan diproses oleh berbagai aplikasi | Data ditampilkan dan diproses oleh browser |

#### 2. Apa yang dimaksud dokumen XML yang well-formed?

Dokumen XML yang **well-formed** adalah dokumen yang penulisannya sudah mengikuti aturan dasar XML. Misalnya, setiap tag yang dibuka harus ditutup, elemen tidak boleh saling tumpang tindih, hanya ada satu *root element*, dan nilai atribut harus berada di dalam tanda kutip.

#### 3. Jelaskan perbedaan well-formed dan valid.

| Well-formed | Valid |
|---|---|
| Mengikuti aturan dasar penulisan XML | Mengikuti aturan struktur yang sudah ditentukan |
| Tidak harus menggunakan DTD atau XSD | Biasanya diperiksa berdasarkan DTD atau XSD |
| Memastikan sintaks XML sudah benar | Memastikan isi dan struktur XML sesuai aturan yang ditentukan |
| XML bisa well-formed tetapi belum tentu valid | XML yang valid harus sudah well-formed |

#### 4. Mengapa XSD lebih kuat dibandingkan DTD?

**XSD** lebih kuat karena aturan yang dapat dibuat lebih lengkap dan detail dibandingkan DTD. XSD dapat menentukan tipe data seperti `string`, `integer`, dan `date`, serta dapat mengatur struktur dan jumlah elemen dengan lebih fleksibel. XSD juga mendukung *namespace* dan menggunakan sintaks XML.

#### 5. Mengapa namespace penting ketika data XML berasal dari beberapa kosakata berbeda?

**Namespace** digunakan untuk membedakan elemen yang memiliki nama sama tetapi berasal dari kosakata yang berbeda. Misalnya, ada dua elemen bernama `table` yang memiliki arti berbeda. Dengan namespace, XML dapat mengetahui bahwa kedua elemen tersebut berasal dari sumber atau kosakata yang berbeda sehingga tidak terjadi bentrokan nama.

#### 6. Apa kegunaan XPath dalam pengolahan dokumen XML?

**XPath** digunakan untuk **menentukan dan mengambil data tertentu dari dalam dokumen XML**. XPath membantu kita menelusuri struktur XML dan memilih elemen atau atribut yang ingin digunakan tanpa harus membaca seluruh isi dokumen.

Contohnya:

```xpath
/bookstore/book/title
