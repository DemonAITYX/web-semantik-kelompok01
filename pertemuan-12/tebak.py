from pathlib import Path
from rdflib import Graph
from owlrl import DeductiveClosure, RDFS_Semantics, OWLRL_Semantics

file_ttl = Path(__file__).parent / "latihan12.ttl"
asserted = Graph().parse(file_ttl, format="turtle")

def tutup(semantik):
    g = Graph() + asserted      # salinan; asserted tidak diubah
    DeductiveClosure(semantik).expand(g)
    return g

G = {"RDFS": tutup(RDFS_Semantics), "OWL RL": tutup(OWLRL_Semantics)}
P = "PREFIX ex: <http://contoh.id/latihan12/>\n"

soal = [
    ("A", "RDFS",   "SELECT ?x WHERE { ?x a ex:Orang }"),
    ("B", "OWL RL", "SELECT ?a ?b WHERE { ?a ex:beradaDi ?b }"),
    ("C", "RDFS",   "SELECT ?m ?d WHERE { ?m ex:dibimbing ?d }"),
    ("C", "OWL RL", "SELECT ?m ?d WHERE { ?m ex:dibimbing ?d }"),
    ("D", "OWL RL", "ASK { ex:medan a ex:Tempat }"),
]

for kode, profil, q in soal:
    hasil = G[profil].query(P + q)
    jawab = hasil.askAnswer if hasil.type == "ASK" else f"{len(hasil)} baris"
    print(kode, "|", profil, "|", jawab)