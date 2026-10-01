## Langkah 1: Membaca Triple RDF

| Kalimat | Subject | Predicate | Object |
| --- | --- | --- | --- |
| Ida Adi adalah dosen. | `ex:ida` | `rdf:type` | `ex:Lecturer` |
| Ida Adi mengajar Web Semantik. | `ex:ida` | `ex:mengajar` | `ex:web_semantik` |
| Mata kuliah itu memiliki nama "Web Semantik". | `ex:web_semantik` | `foaf:name` | `"Web Semantik"` |


## Langkah 2: IRI, Literal, Blank Node, dan Prefix

Berikut adalah jawaban untuk pertanyaan pada Langkah 2:

***1. Identifikasi jenis node:***
* `ex:ida`: *IRI (Internationalized Resource Identifier)*. Ini adalah node yang merepresentasikan suatu sumber daya (resource) unik.
* `"Ida Adi"@id`: *Literal*. Ini adalah *language-tagged literal* yang merepresentasikan nilai teks string beserta informasi bahasanya (bahasa Indonesia).
* `[ ex:kota "Medan" ]`: *Blank Node*. Ini merepresentasikan sumber daya anonim yang tidak memiliki IRI spesifik namun menyimpan properti/relasi di dalamnya.

***2. Mengapa literal tidak boleh menjadi subject RDF?***

  Dalam model data RDF (yang berbentuk graf), *Subject* adalah sumber daya (resource) yang sedang dideskripsikan, sehingga harus memiliki *identifier* berupa IRI atau Blank Node. Literal hanya merepresentasikan nilai akhir (seperti teks, angka, atau tanggal) dan bertindak sebagai daun (*leaf node*) pada graf. Oleh karena itu, literal tidak bisa menjadi *Subject* karena tidak bisa memiliki properti cabang atau relasi turunan lainnya.

***3. IRI dasar untuk graf:***
`https://vshndrr-code.github.io/web-semantik/251402019/usu#`

***4. Kepanjangan namespace:***
* *`rdf`*: Resource Description Framework
* *`rdfs`*: Resource Description Framework Schema (atau RDF Schema)
* *`xsd`*: XML Schema Definition
* *`foaf`*: Friend of a Friend

## Ringkasan graf

* Jumlah triple: 28
* Namespace yang digunakan: `ex`, `foaf`, `rdf`, dan `xsd`
* Entitas: 3 dosen (`ex:ida`, `ex:umay`, `ex:dedy`), 3 mata kuliah (`ex:web_semantik`, `ex:pemrograman_web`, `ex:manajemen_sistem_basis_data`), dan 2 mahasiswa (`ex:vasha`, `ex:bayu`)

## Contoh triple

1. `ex:ida` - `rdf:type` - `ex:Lecturer`

2. `ex:ida` - `foaf:name` - `"Ida Adi"@id`

3. `ex:umay` - `rdf:type` - `ex:Lecturer`

4. `ex:umay` - `foaf:name` - `"Umaya Nasution"@id`

5. `ex:dedy` - `rdf:type` - `ex:Lecturer`

6. `ex:dedy` - `foaf:name` - `"Dedy Arisandi"@id`

7. `ex:web_semantik` - `rdf:type` - `ex:Course`

8. `ex:web_semantik` - `foaf:name` - `"Web Semantik"@id`

9. `ex:pemrograman_web` - `rdf:type` - `ex:Course`

10. `ex:pemrograman_web` - `foaf:name` - `"Pemrograman Web"@id`

11. `ex:manajemen_sistem_basis_data` - `rdf:type` - `ex:Course`

12. `ex:manajemen_sistem_basis_data` - `foaf:name` - `"Manajemen Sistem Basis Data"@id`

13. `ex:vasha` - `rdf:type` - `ex:Student`

14. `ex:vasha` - `foaf:name` - `"Vasha"@id`

15. `ex:bayu` - `rdf:type` - `ex:Student`

16. `ex:bayu` - `foaf:name` - `"Bayu"@id`

17. `ex:ida` - `ex:mengajar` - `ex:web_semantik`

18. `ex:umay` - `ex:mengajar` - `ex:pemrograman_web`

19. `ex:dedy` - `ex:mengajar` - `ex:manajemen_sistem_basis_data`

20. `ex:vasha` - `ex:mengambil` - `ex:web_semantik`

21. `ex:vasha` - `ex:mengambil` - `ex:pemrograman_web`

22. `ex:bayu` - `ex:mengambil` - `ex:manajemen_sistem_basis_data`

23. `ex:web_semantik` - `ex:jumlahKredit` - `3^^xsd:integer`

24. `ex:pemrograman_web` - `ex:jumlahKredit` - `3^^xsd:integer`

25. `ex:manajemen_sistem_basis_data` - `ex:jumlahKredit` - `3^^xsd:integer`

26. `ex:web_semantik` - `ex:hariKuliah` - `"Senin"@id`

27. `ex:pemrograman_web` - `ex:hariKuliah` - `"Rabu"@id`

28. `ex:manajemen_sistem_basis_data` - `ex:hariKuliah` - `"Jumat"@id`