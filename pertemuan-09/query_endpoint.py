import csv
from SPARQLWrapper import SPARQLWrapper, JSON

UA = "KelasWebSemantik/1.0 (guloyosua@gmail.com)"
sparql = SPARQLWrapper("https://query.wikidata.org/sparql", agent=UA)
sparql.setReturnFormat(JSON)
sparql.setQuery("""
SELECT ?univLabel ?kotaLabel WHERE {
  ?univ wdt:P31 wd:Q3918 ;
        wdt:P17 wd:Q252 ;
        wdt:P131 ?kota .
  SERVICE wikibase:label { bd:serviceParam wikibase:language "id,en". }
}
LIMIT 20
""")

hasil = sparql.queryAndConvert()
baris = hasil["results"]["bindings"]
print("Jumlah baris:", len(baris))

with open("hasil_universitas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["universitas", "kota"])
    for b in baris:
        w.writerow([b["univLabel"]["value"], b.get("kotaLabel", {}).get("value", "")])
