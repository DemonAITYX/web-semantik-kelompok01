# Pertemuan 5 - Ontology dan Arsitektur Web Semantik

## LANGKAH 1 — Mengenali Anatomi Ontology

Domain yang digunakan dalam latihan ini adalah **kampus Universitas Sumatera Utara (USU)** dengan domain `usu.ac.id`.

| Komponen | Makna | Contoh Domain Kampus USU |
| --- | --- | --- |
| **Class** | Konsep atau kelompok abstrak | `Mahasiswa`, `Dosen`, `MataKuliah`, `ProgramStudi` |
| **Subclass** | Class yang lebih khusus dari suatu class | `MahasiswaTI` subclassOf `Mahasiswa`, `DosenTI` subclassOf `Dosen` |
| **Individual** | Instance konkret dari suatu class | `IsaDadi` bertipe `DosenTI`, `PemrogramanWeb` bertipe `MataKuliah` |
| **Property** | Hubungan atau nilai yang dimiliki suatu entitas | `mengambilMataKuliah`, `mengajarMataKuliah`, `memilikiNIM` |
| **Axiom** | Pernyataan yang memberikan makna atau aturan | `Mahasiswa` disjointWith `Dosen` |

## LANGKAH 3 — Eksplorasi Protégé

| Komponen | Isi yang dibuat |
| --- | --- |
| Class | `Pizza` |
| Subclass | `CheesyPizza` |
| Individual | `Italy` |
| Object property | `hasTopping` |
| Datatype property | `hasCaloricContent` |

## Ontology mini kampus
- IRI dasar: `https://ontology.usu.ac.id/semantik/kampus`
- Domain: ontology.usu.ac.id

## Komponen ontology
| Komponen | Isi yang dibuat |
| --- | --- |
| Class | `Person`, `Student`, `Lecturer`, `Course`, `Department` |
| Subclass | `Student` subclassOf `Person`, `Lecturer` subclassOf `Person` |
| Object property | `takesCourse`, `teachesCourse`, `registeredInDepartment` |
| Datatype property | `hasNIM`, `hasName` |
| Individual | `nabil`, `yosua`, `bayu`, `vasha`, `bariq`, `pak_isa_dadi`, `course_web_semantik`, `prodi_ti` |
| Axiom/disjointness | `Lecturer` disjointWith `Student`; `Student` memiliki restriction `takesCourse some Course` |

## Layer Cake
Jelaskan posisi ontology dalam Semantic Web Layer Cake: **Ontology/OWL berada di atas RDF/RDFS karena RDF/RDFS menyediakan dasar untuk merepresentasikan graph dan kosakata, sedangkan OWL menambahkan makna domain dan semantik yang lebih kaya. Ontology berada di bawah SPARQL karena SPARQL digunakan untuk melakukan query terhadap graph RDF yang memiliki struktur dan makna yang dapat didefinisikan oleh ontology.**

## Perbandingan serialisasi
- Turtle: Menggunakan `@prefix` untuk mempersingkat IRI dan memiliki sintaks yang ringkas, seperti penggunaan `a` sebagai singkatan `rdf:type` serta pengelompokan beberapa property dalam satu subject.
- RDF/XML: Menggunakan struktur tag XML seperti `<owl:Class>`, `<owl:ObjectProperty>`, dan `<owl:NamedIndividual>` serta atribut seperti `rdf:about` dan `rdf:resource`, sehingga sintaksnya lebih verbose dibandingkan Turtle.
- Kesamaan makna: Turtle dan RDF/XML merepresentasikan ontology yang sama, termasuk IRI dasar, class, subclass, property, individual, axiom/disjointness, dan restriction. Perbedaannya hanya pada bentuk sintaks atau serialisasinya.
