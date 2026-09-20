# Pertemuan 5 — Ontology dan Arsitektur Web Semantik

## LANGKAH 1 — Mengenali Anatomi Ontology

Domain yang digunakan dalam latihan ini adalah **kampus Universitas Sumatera Utara (USU)** dengan domain `usu.ac.id`.

| Komponen       | Makna                                           | Contoh Domain Kampus USU                                                   |
| -------------- | ----------------------------------------------- | -------------------------------------------------------------------------- |
| **Class**      | Konsep atau kelompok abstrak                    | `Mahasiswa`, `Dosen`, `MataKuliah`, `ProgramStudi`                         |
| **Subclass**   | Class yang lebih khusus dari suatu class        | `MahasiswaTI` subclassOf `Mahasiswa`, `DosenTI` subclassOf `Dosen`         |
| **Individual** | Instance konkret dari suatu class               | `IsaDadi` bertipe `DosenTI`, `PemrogramanWeb` bertipe `MataKuliah` |
| **Property**   | Hubungan atau nilai yang dimiliki suatu entitas | `mengambilMataKuliah`, `mengajarMataKuliah`, `memilikiNIM`                 |
| **Axiom**      | Pernyataan yang memberikan makna atau aturan    | `Mahasiswa` disjointWith `Dosen`                                           |