from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF

g = Graph()

EX = Namespace("https://vshndrr-code.github.io/web-semantik/251402019/usu#")

g.bind("ex", EX)
g.bind("foaf", FOAF)

g.add((EX.ida, RDF.type, EX.Lecturer))
g.add((EX.ida, FOAF.name, Literal("Ida Adi", lang="id")))
g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))
g.add((EX.ida, EX.mengajar, EX.web_semantik))

print(g.serialize(format="turtle"))

g.serialize("kampus_usu.ttl", format="turtle")
g.serialize("kampus_usu.jsonld", format="json-ld", indent=2)
