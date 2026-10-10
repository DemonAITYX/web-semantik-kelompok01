from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD

g = Graph()

EX = Namespace("https://vshndrr-code.github.io/web-semantik/251402019/usu#")

g.bind("ex", EX)
g.bind("foaf", FOAF)

g.add((EX.ida, RDF.type, EX.Lecturer))
g.add((EX.ida, FOAF.name, Literal("Ida Adi", lang="id")))

g.add((EX.umay, RDF.type, EX.Lecturer))
g.add((EX.umay, FOAF.name, Literal("Umaya Nasution", lang="id")))

g.add((EX.dedy, RDF.type, EX.Lecturer))
g.add((EX.dedy, FOAF.name, Literal("Dedy Arisandi", lang="id")))


g.add((EX.web_semantik, RDF.type, EX.Course))
g.add((EX.web_semantik, FOAF.name, Literal("Web Semantik", lang="id")))

g.add((EX.pemrograman_web, RDF.type, EX.Course))
g.add((EX.pemrograman_web, FOAF.name, Literal("Pemrograman Web", lang="id")))

g.add((EX.manajemen_sistem_basis_data, RDF.type, EX.Course))
g.add((EX.manajemen_sistem_basis_data, FOAF.name, Literal("Manajemen Sistem Basis Data", lang="id")))


g.add((EX.vasha, RDF.type, EX.Student))
g.add((EX.vasha, FOAF.name, Literal("Vasha", lang="id")))

g.add((EX.bayu, RDF.type, EX.Student))
g.add((EX.bayu, FOAF.name, Literal("Bayu", lang="id")))


g.add((EX.ida, EX.mengajar, EX.web_semantik))
g.add((EX.umay, EX.mengajar, EX.pemrograman_web))
g.add((EX.dedy, EX.mengajar, EX.manajemen_sistem_basis_data))


g.add((EX.vasha, EX.mengambil, EX.web_semantik))
g.add((EX.vasha, EX.mengambil, EX.pemrograman_web))
g.add((EX.bayu, EX.mengambil, EX.manajemen_sistem_basis_data))


g.add((EX.web_semantik, EX.jumlahKredit,
       Literal(3, datatype=XSD.integer)))

g.add((EX.pemrograman_web, EX.jumlahKredit,
       Literal(3, datatype=XSD.integer)))

g.add((EX.manajemen_sistem_basis_data, EX.jumlahKredit,
       Literal(3, datatype=XSD.integer)))

g.add((EX.web_semantik, EX.hariKuliah,
       Literal("Senin", lang="id")))

g.add((EX.pemrograman_web, EX.hariKuliah,
       Literal("Rabu", lang="id")))

g.add((EX.manajemen_sistem_basis_data, EX.hariKuliah,
       Literal("Jumat", lang="id")))


print(g.serialize(format="turtle"))

g.serialize("pertemuan-06/kampus_usu.ttl", format="turtle")
g.serialize("pertemuan-06/kampus_usu.jsonld", format="json-ld", indent=2)

from rdflib.namespace import RDF

print("Daftar dosen:")
for subject, predicate, obj in g.triples((None, RDF.type, EX.Lecturer)):
    print(subject)