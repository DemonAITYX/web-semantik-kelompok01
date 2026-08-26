# Pertemuan 1 - Pengenalan Web Semantik

## 1. Eksplorasi Wikidata
- Nama entitas: University of North Sumatra
- Identifier Wikidata: Q4200341
- Deskripsi: "national university in North Sumatera, Indonesia"
- Negara: Indonesia
- Lokasi: Medan Tuntungan
- Tahun berdiri: 4 July 1952
- Website: https://www.usu.ac.id
- Kode pos: 20155
- Alamat: Jalan Dr T Mansur No 9 Padang Bulan 

## 2. Entitas, Atribut, dan Relasi

| Informasi | Kategori | Alasan |
|---|---|---|
| University of North Sumatra (Q4200341) | Entitas | Objek utama yang dibahas |
| Medan Tuntungan (Q4250985) | Entitas | Wilayah yang terkait dengan USU |
| Indonesia (Q252) | Entitas | Negara tempat USU berada |
| Description | Atribut | Menjelaskan entitas |
| Postal Code | Atribut | Menunjukkan kode pos |
| Inception | Atribut | Menunjukkan tanggal pendirian |
| Official Website | Atribut | Menunjukkan situs resmi |
| Street Address | Atribut | Menunjukkan alamat entitas |
| University of North Sumatra → located in → Medan Tuntungan | Relasi | Menunjukkan lokasi USU |
| University of North Sumatra → country → Indonesia | Relasi | Menunjukkan negara USU |


## 3. Eksplorasi Schema.org
....


## 4. Pertanyaan Evaluasi

### 1. Apa perbedaan utama antara web tradisional dan Web Semantik?
**Web tradisional** dirancang untuk dibaca dan dipahami oleh manusia (*human-readable*), di mana dokumen atau halaman web dihubungkan melalui *hyperlink* (HTML) tanpa ada makna terstruktur yang dapat diolah otomatis oleh komputer. 

Sebaliknya, **Web Semantik** dirancang agar data dan informasi dapat dipahami serta diolah langsung oleh mesin/komputer (*machine-readable*). Data pada Web Semantik dihubungkan berdasarkan makna dan relasinya menggunakan standar seperti RDF dan URI/IRI.

### 2. Mengapa suatu entitas membutuhkan identifier unik?
Suatu entitas membutuhkan *identifier* unik (seperti URI atau IRI) untuk mencegah ambiguitas atau kekeliruan identitas data di internet. Dengan *identifier* unik, sistem dapat memastikan bahwa dua data merujuk pada objek/konsep nyata yang sama persis secara global, meskipun memiliki nama yang mirip atau digunakan oleh sistem yang berbeda-beda.

### 3. Jelaskan perbedaan subject, predicate, dan object menggunakan satu contoh buatan Anda sendiri.
Dalam konsep RDF triple, fakta direpresentasikan ke dalam 3 komponen utama:
* **Subject (Subjek):** Entitas atau sumber daya utama yang sedang dibahas.
* **Predicate (Predikat):** Sifat, hubungan, atau atribut yang menghubungkan subjek dengan objek.
* **Object (Objek):** Nilai dari atribut atau entitas lain yang menjadi tujuan hubungan dari subjek.

**Contoh buatan sendiri:**
`Samsung Galaxy S26 Ultra` → `manufacturedBy` → `Samsung Electronics`

* **Subject:** `Samsung Galaxy S26 Ultra` (perangkat/entitas yang dibicarakan)
* **Predicate:** `manufacturedBy` (relasi pembuat/produsen)
* **Object:** `Samsung Electronics` (perusahaan/entitas produsennya)

### 4. Apa keuntungan merepresentasikan informasi sebagai hubungan antarentitas dibandingkan hanya menyimpannya sebagai teks biasa?
Merepresentasikan informasi sebagai hubungan antarentitas (berbasis *graph* atau *triple*) memungkinkan mesin untuk melakukan analisis relasi, kueri data yang kompleks, dan penarikan kesimpulan (*inference*) secara otomatis. Teks biasa (*unstructured text*) sulit diindeks dan dipahami maknanya oleh komputer tanpa teknik NLP yang rumit, sedangkan data berelasi terstruktur (*structured data*) memudahkan integrasi data lintas platform dan pemrosesan yang presisi.

### 5. Menurut Anda, bagaimana Knowledge Graph dapat membantu sistem pencarian atau AI dalam memahami informasi?
Knowledge Graph membantu sistem pencarian dan AI dengan cara menyediakan konteks dan jaringan pengetahuan yang saling terhubung. Daripada sekadar mencocokkan kata kunci (*keyword matching*), AI dan mesin pencari dapat memahami *makna* di balik entitas, relasi antar konsep, serta fakta kontekstual. Hal ini memungkinkan AI memberikan jawaban yang akurat, relevan, dan mampu menyambungkan fakta fakta yang tersebar secara logis.

