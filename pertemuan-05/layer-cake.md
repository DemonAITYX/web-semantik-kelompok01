# Pemetaan Semantic Web Layer Cake

Berdasarkan artefak dan file yang telah dikerjakan pada repositori kelompok, berikut adalah pemetaan untuk *Semantic Web Layer Cake*:

| Lapis | Peran | Contoh Anda (Artefak Repositori) |
| :--- | :--- | :--- |
| **URI dan Unicode** | Identitas global dan representasi karakter | Penggunaan URL namespace (seperti `xmlns:dc="http://purl.org/dc/elements/1.1/"`) pada `pertemuan-02/namespace.xml`[cite: 1] |
| **XML** | Sintaks pertukaran data | File `pertemuan-02/katalog_buku.xml` dan `pertemuan-02/buku.xsd`[cite: 1] |
| **RDF dan RDFS** | Pernyataan graph dan kosakata dasar | File `pertemuan-04/metadata-sumber.ttl` (penulisan data graf dengan format Turtle)[cite: 1] |
| **Ontology / OWL** | Makna domain dan penalaran lebih kaya | File `pertemuan-05/ontology-kampus.owl` (pendefinisian class dan hierarki kampus)[cite: 1] |
| **SPARQL** | Query graph RDF | *(Belum ada artefak file query khusus di pertemuan 1-4)*[cite: 1] |
| **Rules, Proof, Trust**| Aturan, pembuktian, dan kepercayaan | Proses validasi kebenaran *markup* menggunakan alat eksternal seperti pada `pertemuan-04/screenshots/schema-validator.png`[cite: 1] |

***

### Jawaban Singkat: 
**Mengapa ontology berada di atas RDF/RDFS dan di bawah SPARQL dalam arsitektur ini?**

*   **Berada di atas RDF/RDFS:** RDF dan RDFS mendasari web semantik dengan menyediakan struktur data berupa graph dasar (*triple*: Subject-Predicate-Object) dan hierarki klasifikasi yang sangat sederhana. Ontology (seperti OWL) berada di atasnya karena ia dibangun dari pondasi RDF tersebut untuk menambahkan semantik yang jauh lebih kaya, aturan logika yang kompleks, serta batasan-batasan (seperti *cardinality*, relasi *inverse*, dll) yang tidak bisa dilakukan oleh RDF biasa.
*   **Berada di bawah SPARQL:** SPARQL adalah bahasa *query* tingkat atas yang berfungsi untuk mencari, mengambil, dan mengekstrak data dari graf. Agar SPARQL dapat melakukan kueri secara cerdas (termasuk menarik kesimpulan logis atau inferensi), ia bergantung pada ketersediaan data (RDF) beserta makna struktural dan aturan domainnya (Ontology) yang harus sudah didefinisikan dan berada di lapisan bawahnya.
