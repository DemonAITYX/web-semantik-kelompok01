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
