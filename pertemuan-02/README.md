## 2. Analisis Kesalahan XML

| No | Bagian yang Salah | Alasan | Perbaikan |
|---|---|---|---|
| 1 | `<nama>Budi Santoso</Nama>` | XML bersifat *case-sensitive*. Tag pembuka menggunakan huruf kecil, sedangkan tag penutup diawali huruf kapital. | Ubah tag penutup menjadi huruf kecil: `</nama>` |
| 2 | `<angkatan>2024` | Elemen tidak memiliki tag penutup (*missing closing tag*). Setiap elemen XML wajib ditutup. | Tambahkan tag penutup di akhir nilai menjadi: `<angkatan>2024</angkatan>` |
| 3 | `<deskripsi>Saya suka AI & Web Semantik</deskripsi>` | Terdapat karakter khusus `&` yang dilarang ditulis langsung dalam XML (harus di-*escape*). | Ganti karakter `&` dengan entitas XML yang valid, yaitu `&amp;` |

## 3. Analisis XML Schema

1. **Root element:** `buku`. Di dalam `buku.xsd` hanya ada satu `<xs:element>` yang berada langsung di bawah `<xs:schema>`, yaitu `name="buku"`. Elemen yang dideklarasikan di level atas (global) inilah yang boleh menjadi root, sehingga dokumen XML yang divalidasi dengan skema ini harus berakar pada `<buku>`. Elemen `katalog` tidak dideklarasikan di skema ini, jadi `katalog_buku.xml` belum bisa divalidasi langsung dengan `buku.xsd`.

2. **Tipe data `judul`:** `xs:string`, yaitu teks bebas (boleh huruf, angka, spasi, dan tanda baca). Contoh nilai valid: `Pengantar Web Semantik`.

3. **Tipe data `tahun`:** `xs:gYear`, yaitu tipe tanggal Gregorian yang hanya memuat komponen tahun dengan format `CCYY` (empat digit), misalnya `2024`. Karena tipenya spesifik, nilai seperti `24`, `2024/2025`, atau `tahun 2024` akan dianggap tidak valid.

4. **Tipe data `harga`:** `xs:decimal`, yaitu bilangan desimal yang boleh memiliki bagian pecahan dan tanda minus, tetapi tanpa pemisah ribuan dan tanpa simbol mata uang. Nilai `125000` dan `125000.50` valid, sedangkan `Rp125.000` tidak valid.

5. **Atribut `isbn`:** **Tidak boleh dihilangkan.** Pada skema tertulis `use="required"`, yang berarti setiap elemen `<buku>` wajib mencantumkan atribut `isbn`. Jika atribut tersebut tidak dituliskan, dokumen tetap *well-formed* (sintaks XML-nya benar), tetapi menjadi **tidak valid** karena melanggar aturan skema. Jika ingin bersifat opsional, nilainya harus diubah menjadi `use="optional"` (nilai default apabila atribut `use` tidak ditulis sama sekali).

## 4. Analisis Namespace

1. **Mengapa kedua elemen `title` tidak sama?** Karena identitas sebuah elemen dalam XML ditentukan oleh pasangan **(URI namespace, nama lokal)**, bukan oleh nama lokalnya saja. Elemen `<buku:title>` sebenarnya bernama `{https://example.org/buku}title`, sedangkan `<web:title>` bernama `{https://example.org/web}title`. Nama lokalnya memang sama-sama `title`, tetapi karena berasal dari namespace yang berbeda, keduanya dianggap dua elemen yang berbeda. Secara makna pun berbeda: yang satu adalah judul buku, yang lain adalah judul situs/portal. Inilah cara XML menghindari tabrakan nama (*name collision*) ketika satu dokumen memuat data dari beberapa kosakata.

2. **Fungsi prefix `buku:` dan `web:`:** Prefix adalah alias atau singkatan bagi URI namespace yang panjang, sehingga penulisan elemen menjadi ringkas sekaligus menunjukkan dari kosakata mana elemen itu berasal. Prefix hanya berlaku lokal di dalam dokumen dan bukan bagian dari identitas elemen; yang mengikat adalah URI-nya. Artinya, mengganti `buku:` menjadi `b:` (selama `xmlns` tetap menunjuk URI yang sama) sama sekali tidak mengubah arti dokumen.

3. **Fungsi atribut `xmlns`:** Atribut `xmlns` berfungsi mendeklarasikan namespace. Dalam bentuk `xmlns:prefix="URI"` ia mengikat sebuah prefix ke URI namespace tertentu, sedangkan dalam bentuk `xmlns="URI"` ia menetapkan *default namespace* bagi semua elemen tanpa prefix. Deklarasi ini berlaku pada elemen tempat ia dituliskan beserta seluruh elemen turunannya, sehingga cukup dideklarasikan sekali di elemen `<data>` untuk dipakai anak-anaknya.

4. **Apakah URI namespace harus dapat dibuka sebagai halaman web?** **Tidak harus.** URI namespace hanya berperan sebagai **pengenal unik (identifier)**, bukan sebagai alamat yang isinya akan diunduh. Parser XML tidak pernah mengakses URI tersebut ketika memproses dokumen, sehingga `https://example.org/buku` tetap sah meskipun halamannya tidak ada. Penggunaan URI berbasis domain (http/https) hanya konvensi agar identifier dijamin unik dan jelas kepemilikannya. Meski begitu, pada praktik Linked Data/RDF sangat dianjurkan (*best practice*) agar URI tersebut dapat dibuka (*dereferenceable*) dan menampilkan dokumentasi atau ontologinya, tetapi hal itu bersifat anjuran, bukan kewajiban XML.

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
