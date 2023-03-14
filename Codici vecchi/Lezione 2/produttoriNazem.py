
#@title Testo del titolo predefinito
import pandas as pd
from statsmodels.stats.weightstats import DescrStatsW
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/TheNoobRoxas/bigData/main/produttori.csv'
df = pd.read_csv(url)
print("Seleziona il produttore di cui vuoi ottenere i dati")
print("1 - Produttore A")
print("2 - Produttore B")
inputUtente = input()

if int(inputUtente) == 1:
        df2 = df.loc[df['produttore'] == 'produttoreA']
        media = DescrStatsW(df2['vitaMesi'], df2['numeroDevice'], ddof=1).mean
        deviazioneStandard = DescrStatsW(df2['vitaMesi'], df2['numeroDevice'], ddof=1).std
        print("La media è: " + str(media))
        print("La standard deviazione è : " + str(deviazioneStandard))
        plt.plot(df2['vitaMesi'], df2['distribuzione'])
        plt.xlim([0, 100])
        plt.show()
if int(inputUtente) == 2:
        df2 = df.loc[df['produttore'] == 'produttoreB']
        media = DescrStatsW(df2['vitaMesi'], df2['numeroDevice'], ddof=1).mean
        deviazioneStandard = DescrStatsW(df2['vitaMesi'], df2['numeroDevice'], ddof=1).std
        print("La media è: " + str(media))
        print("La standard deviazione è :" + str(deviazioneStandard))
        plt.plot(df2['vitaMesi'], df2['distribuzione'])
        plt.xlim([0, 100])
        plt.show()
