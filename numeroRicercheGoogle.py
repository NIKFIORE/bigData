import csv
import requests
from bs4 import BeautifulSoup

# Nome del file CSV da leggere
filename = 'C:\\Users\\nazem\\OneDrive\\Desktop\\risultati_pagerank_caratteri.csv'

# Leggi il file CSV e crea un nuovo file CSV con la colonna aggiuntiva
with open(filename, mode='r', encoding='utf-8-sig', newline='') as input_file, \
     open('C:\\Users\\nazem\\OneDrive\\Desktop\\risultati_google.csv', mode='w', encoding='utf-8-sig', newline='') as output_file:
    reader = csv.reader(input_file, delimiter=',')
    writer = csv.writer(output_file, delimiter=',')

    # Leggi l'header del file CSV e aggiungi la nuova colonna
    header = next(reader)
    header.append('numero_risultati_google')
    writer.writerow(header)

    # Per ogni riga del file CSV, effettua la ricerca su Google e salva il numero di risultati
    for row in reader:
        nome_pagina = row[0] # il nome del personaggio è nella prima colonna

        # Effettua la ricerca su Google
        query = f'{nome_pagina} wikipedia'
        url = f'https://www.google.com/search?q={query}'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        response = requests.get(url, headers=headers)

        # Analizza il contenuto HTML della pagina di Google e estrai il numero di risultati
        soup = BeautifulSoup(response.text, 'html.parser')
        numero_risultati = soup.find('div', {'id': 'result-stats'})
        if numero_risultati is not None:
            numero_risultati = numero_risultati.text.split(' ')[1]
            row.append(numero_risultati)
        else:
            row.append('Errore')

        # Scrivi la riga aggiornata nel nuovo file CSV
        writer.writerow(row)
