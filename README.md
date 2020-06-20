# TEST---PYTHON-SUMMER-INTERN
*poslední commit z 20. června opravuje bug s mongoDB, vše je teď funkční*
Pokud nebudete vědět jak něco 'rozběhnout' nebo nepochopíte proč jsem něco udělal tak, jak jsem to udělal, je velká šance, že to bude někde tady napsané, pokud ne, zeptejte se mě.
Jsou tu totiž dvě možnosti, jak tuto aplikaci 'rozběhnout'.
Jo a nezapomeňte na requirements.
# 1A) Aplikace s Flask frameworkem
Na tuto možnost je vše připravené.
Nejdříve vysvětlím, porč jsou některé věci tak, jak jsou. 
Ze všeho nejdřív si asi budete říkat: 'Proč používá Pymongo a Flask odděleně a nepoužívá přímo flask-pymongo?'
No.. Je to proto, protože jsem do 3/4 projektu nevěděl, že něco takového existuje.
Dále si asi řekenete: 'Proč nepoužívá mongo databázi přímo jako output pro stránku, ale používá seznamy, z kterých pak udělá JSON.'
Na stránce se zobrazuje vše z posledních 50ti otázek, které se následně smažou a pak se při dalším načtení stránky udělají nové, v databázi se nic nemaže.
# 1B) Jak rozběhnout mongo databázi a Flask server?
Začneme se 'setupem' mongo databáze. V kódu je databáze nastavená na localhost na portu 27017. Pokud máte jiný server mongodb nebo cokoliv v kódu jsou komentáře, které ukazují, kde můžete změnit mongodb server(přesněji v 'app.py' a v 'stack/stack/pipelines.py')
Pokud nemáte mongodb a potřebujete nějak pomoc, napište.
Teď stačí pouze spustit server (napsat 'python app.py' ve složce, kde je app.py)
# 2A) Aplikace BEZ Flask frameworku
Najděte soubor pipelines.py, tam je ale komentářů, že? Pokud chcete aplikaci rozběhnout, řiďte se podle nich.(zde není ani nejmenší chyba)
