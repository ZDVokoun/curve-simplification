# curve-simplification
Kód ke konfeře z M&amp;M sousu v Hodoňovicích na zjednodušování křivek (přesněji lomených čar, neboli posloupností bodů spojených úsečkami). Protože bylo málo času (jen tři dny), soustředili jsme se jen na odstraňování bodů. Na této konfeře jsem pracoval spolu s Petrem Starým a Pavlou Šímovou a zajistila nám na sousu třetí místo.

Během konfery jsme implementovali čtyři různé algoritmy a porovnávali je. Mezi nima jsou:

- Vybírat ty body, jež jsou vrcholem největšího úhlu
- Vybírat ty body, jejichž součet vzdáleností od jejich sousedů je nejmenší
- Vybírat vždy k-tý bod
- Vybírat ty body, po jejichž odstranění se MSE zvětší nejméně (jako chyba se počítá vzdálenost původního bodu od zjednodušené křivky)

V kódu jsou příklady některých datasetů z OSM a některé ukázky.
