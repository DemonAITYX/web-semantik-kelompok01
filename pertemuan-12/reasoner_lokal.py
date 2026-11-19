from pathlib import Path
from rdflib import Graph, Namespace, RDF, RDFS
from owlrl import DeductiveClosure, RDFS_Semantics

BASE = "https://vshndrr-code.github.io/web-semantik/251402019/usu#"

FOLDER = Path(__file__).resolve().parent

SUMBER = FOLDER.parent / "pertemuan-09" / "kampus_usu_v2.ttl"
V4 = FOLDER.parent / "pertemuan-11" / "kampus_usu_v4.ttl"

EX = Namespace(BASE)

# 1. Graf asserted + skema
asserted = Graph()
asserted.parse(SUMBER, format="turtle")

asserted.bind("ex", EX)
asserted.bind("rdfs", RDFS)

# Domain dan range properti mengajar
asserted.add((EX.mengajar, RDFS.domain, EX.Lecturer))
asserted.add((EX.mengajar, RDFS.range, EX.Course))

print("Sumber:", SUMBER)
print("Triple asserted:", len(asserted))

# 2. Closure dan inferensi
closure = Graph()
closure += asserted

DeductiveClosure(RDFS_Semantics).expand(closure)

inferred = closure - asserted

# 3. Simpan hanya turunan yang bermakna
TRIVIAL = {RDFS.Resource, RDF.Property}

bermakna = Graph()

for s, p, o in inferred:
    if str(s).startswith(BASE) and o not in TRIVIAL and s != o:
        bermakna.add((s, p, o))

print("Closure:", len(closure))
print("Inferred:", len(inferred))
print("Bermakna:", len(bermakna))

# 4. Simpan hasil
asserted.serialize(
    destination=FOLDER / "kampus_usu_v5.ttl",
    format="turtle"
)

bermakna.serialize(
    destination=FOLDER / "kampus_usu_inferred.ttl",
    format="turtle"
)

# 5. Bandingkan dengan v4 Pertemuan 11
if V4.exists():
    v4 = Graph()
    v4.parse(V4, format="turtle")

    tercampur = [t for t in v4 if t not in asserted]

    print("Triple di v4 yang tidak ada di asserted:",
            len(tercampur))

    print("Triple turunan baru:", len(bermakna))

    print("\nTriple di v4 yang tidak ada di asserted:")
    for triple in tercampur:
        print(triple)
else:
    print("File v4 tidak ditemukan:", V4)