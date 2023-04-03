import networkx as nx
import wikipediaapi
import pandas as pd

# Creiamo un wikipedia api wrapper
wiki = wikipediaapi.Wikipedia(
        language='it',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

# Leggiamo il file "SkineaTop100.csv" e otteniamo la lista delle persone
dati = pd.read_csv(r'C:\Users\nazem\PycharmProjects\pythonProject\Big Data\Produttori\file\SkineaTop100.csv')

# Aggiungiamo la colonna "posizioneInClassifica" al DataFrame
dati['posizioneInClassifica'] = dati.index + 1

persone = dati['personaggio'].tolist()

# Creiamo un grafo vuoto
G = nx.DiGraph()

# Aggiungiamo i nodi per ciascuna persona
for persona in persone:
    page = wiki.page(persona)
    G.add_nodes_from([page.title])

# Aggiungiamo gli archi tra le pagine Wikipedia
for persona in persone:
    page = wiki.page(persona)
    for link in page.links.items():
        if link[0] in persone:
            G.add_edge(page.title, link[0])

# Calcoliamo il PageRank
pr = nx.pagerank(G)

# Ordiniamo il dizionario in base al valore del PageRank
pr_ordinato = dict(sorted(pr.items(), key=lambda item: item[1], reverse=True))

# Creiamo un DataFrame a partire dal dizionario dei PageRank
df = pd.DataFrame({'personaggio': list(pr_ordinato.keys()), 'PageRank': list(pr_ordinato.values())})

# Uniamo il DataFrame del PageRank con il DataFrame delle posizioni in classifica
df = pd.merge(df, dati, on='personaggio')

# Salviamo il DataFrame come file CSV
df.to_csv('risultati_pagerank2.csv', index=False)
