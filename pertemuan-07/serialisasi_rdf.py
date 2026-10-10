from rdflib import Graph

g = Graph()
g.parse("pertemuan-07/kampus_usu.ttl", format="turtle")


g.serialize("pertemuan-07/kampus_usu.jsonld", format="json-ld", indent=2)
g.serialize("pertemuan-07/kampus_usu.nt", format="nt", encoding="utf-8")

print(f"Jumlah triple: {len(g)}")
print(g.serialize(format="turtle"))

from rdflib import URIRef, Literal, Namespace
from rdflib.namespace import RDF, DCTERMS, XSD

EX = Namespace("https://contoh.github.io/web-semantik/251402134/kampus#")
stmt = URIRef(EX + "stmt-01")

g.add((stmt, RDF.type, RDF.Statement))
g.add((stmt, RDF.subject, EX.ida))
g.add((stmt, RDF.predicate, EX.mengajar))
g.add((stmt, RDF.object, EX.web_semantik))
g.add((stmt, DCTERMS.creator, EX.ida))
g.add((stmt, DCTERMS.date, Literal("2026-10-01", datatype=XSD.date)))
g.add((stmt, DCTERMS.source, Literal("Data akademik kampus")))