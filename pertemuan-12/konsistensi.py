
import csv
from rdflib import Graph, Namespace, RDF, URIRef
from owlrl import DeductiveClosure, RDFS_Semantics, OWLRL_Semantics

BASE = "https://vshndrr-code.github.io/web-semantik/251402019/usu#"
ERR = Namespace("http://www.daml.org/2002/03/agents/agent-ont#")

# Memuat graf kampus
asserted = Graph().parse("kampus_usu_v5.ttl", format="turtle")

# Menambahkan aksioma dan triple yang sengaja dibalik
asserted.update(f"""
PREFIX ex: <{BASE}>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
INSERT DATA {{
    ex:Pegawai owl:disjointWith ex:Course .

}}
""")

# Kelas yang akan dihitung
KELAS = ["Lecturer", "Pegawai", "Course"]

def anggota(g, kelas):
    return len(set(
        g.subjects(RDF.type, URIRef(BASE + kelas))
    ))

hasil = {}

# Menjalankan dua profil reasoner
for nama, semantik in [
    ("RDFS", RDFS_Semantics),
    ("OWL RL", OWLRL_Semantics)
]:
    g = Graph() + asserted
    DeductiveClosure(semantik).expand(g)

    pesan = [
        str(e)
        for m in g.subjects(RDF.type, ERR.ErrorMessage)
        for e in g.objects(m, ERR.error)
    ]

    hasil[nama] = {
        k: anggota(g, k) for k in KELAS
    }

    print("\nProfil:", nama)
    print("Jumlah triple:", len(g))
    print("Jumlah pesan galat:", len(pesan))

    for p in pesan:
        print("  ", p)

# Membuat laporan CSV
with open(
    "laporan_kelas.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:
    w = csv.writer(f)

    w.writerow(["kelas", "asserted", "rdfs", "owl_rl"])

    for k in KELAS:
        w.writerow([
            k,
            anggota(asserted, k),
            hasil["RDFS"][k],
            hasil["OWL RL"][k]
        ])

print("\nCSV tersimpan: laporan_kelas.csv")
