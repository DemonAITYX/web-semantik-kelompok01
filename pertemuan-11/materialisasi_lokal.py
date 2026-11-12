from pathlib import Path
from rdflib import Graph

SUMBER = Path("../pertemuan-10/kampus_usu_v3.ttl")
if not SUMBER.exists():  # belum punya v3? pakai v2
    SUMBER = Path("../pertemuan-09/kampus_usu_v2.ttl")

g = Graph().parse(SUMBER, format="turtle")
print("Sumber:", SUMBER, "| triple awal:", len(g))

PREFIX = """
PREFIX ex: <https://vshndrr-code.github.io/web-semantik/251402019/usu#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
"""

# A. Pemetaan ke schema.org: graf baru, IRI tetap
q_peta = PREFIX + """
CONSTRUCT {
  ?d a schema:Person ;
     schema:name ?nama .
} WHERE {
  ?d a ex:Lecturer ;
     foaf:name ?nama .
}
"""
peta = Graph()
for t in g.query(q_peta):
    peta.add(t)
print("Triple hasil pemetaan:", len(peta))
peta.serialize("dosen_schema.ttl", format="turtle")

# B. Tambah hierarki kecil, lalu materialisasi
g.update(PREFIX + """
INSERT DATA {
  ex:Lecturer rdfs:subClassOf ex:Pegawai .
  ex:Pegawai rdfs:subClassOf foaf:Person .
}
""")
q_orang = PREFIX + "SELECT ?x WHERE { ?x a foaf:Person }"
print("foaf:Person sebelum:", len(g.query(q_orang)))

turunan = g.query(PREFIX + """
CONSTRUCT { ?x a ?super } WHERE { ?x a/rdfs:subClassOf+ ?super }
""")
baru = [t for t in turunan if t not in g]
for t in baru:
    g.add(t)
print("Triple turunan baru:", len(baru))
print("foaf:Person sesudah:", len(g.query(q_orang)))

g.serialize("kampus_usu_v4.ttl", format="turtle")
