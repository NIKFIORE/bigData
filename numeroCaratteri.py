import csv
import requests

# URL dell'API di Wikimedia per ottenere il testo di una pagina di Wikipedia
url = 'https://en.wikipedia.org/w/api.php?action=query&titles={0}&prop=extracts&explaintext=1&format=json'

# Nome del file CSV da leggere
filename = 'C:\\Users\\nazem\\OneDrive\\Desktop\\risultati_pagerank.csv'

# Nome della colonna del personaggio
nome_colonna = 'personaggio'

# Leggi il file CSV e crea un nuovo file CSV con la colonna aggiuntiva
with open(filename, mode='r', encoding='utf-8-sig', newline='') as input_file, \
     open('C:\\Users\\nazem\\OneDrive\\Desktop\\risultati_pagerank_caratteri2.csv', mode='w', encoding='utf-8-sig', newline='') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')

    # Leggi l'header del file CSV e aggiungi la nuova colonna
    header = next(reader)
    header.append('numero_caratteri')
    writer.writerow(header)

    # Per ogni riga del file CSV, cerca il numero di caratteri sulla pagina di Wikipedia corrispondente
    for row in reader:
        nome_pagina = row[0] # il nome del personaggio è nella prima colonna

        # Codifica il nome della pagina per l'URL
        nome_pagina_encoded = requests.utils.quote(nome_pagina, safe='')

        # Effettua la richiesta GET all'API di Wikimedia
        response = requests.get(url.format(nome_pagina_encoded))

        # Se la richiesta ha avuto successo, estrai il numero di caratteri del testo della pagina
        if response.status_code == 200:
            try:
                soup = response.json()
                page = next(iter(soup['query']['pages'].values()))
                num_caratteri = len(page['extract'])
                row.append(str(num_caratteri))
            except (KeyError, StopIteration):
                row.append('Errore')
        else:
            row.append('Errore')

        # Scrivi la riga aggiornata nel nuovo file CSV
        writer.writerow(row)
