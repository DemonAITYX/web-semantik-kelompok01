from pathlib import Path
from rdflib import Graph

g = Graph()
g.parse(Path("../pertemuan-06/kampus_usu.ttl"), format="turtle")
print("Jumlah triple awal:", len(g))

PREFIX = """
PREFIX ex:   <https://vshndrr-code.github.io/web-semantik/251402019/usu#>
PREFIX foaf: <http://xmlns.com/foaf/0.1/>
"""

# 1. SELECT: siapa mengajar apa
q_select = PREFIX + """
SELECT ?namaDosen ?namaMK WHERE {
  ?dosen ex:mengajar ?mk ;
         foaf:name   ?namaDosen .
  ?mk    foaf:name   ?namaMK .
}
ORDER BY ?namaDosen
"""
for row in g.query(q_select):
    print(row.namaDosen, "-", row.namaMK)

# 2. ASK: fakta yang belum tercatat
q_ask = PREFIX + "ASK { ex:ida ex:mengajar ex:kecerdasan_buatan }"
print("Sebelum INSERT:", g.query(q_ask).askAnswer)

# 3. TELL lewat SPARQL Update
g.update(PREFIX + """
INSERT DATA {
  ex:ida ex:mengajar ex:kecerdasan_buatan .
  ex:kecerdasan_buatan foaf:name "Kecerdasan Buatan"@id .
}
""")
print("Sesudah INSERT:", g.query(q_ask).askAnswer)
print("Jumlah triple akhir:", len(g))

g.serialize("kampus_usu_v2.ttl", format="turtle")