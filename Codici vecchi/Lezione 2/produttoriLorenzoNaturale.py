#from google.colab import files
#uploaded = files.upload()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io

#df = pd.read_csv(io.StringIO(uploaded['producerA.csv'].decode('utf-8')))
url1 = 'https://raw.githubusercontent.com/TheNoobRoxas/bigData/main/producerA.csv'
df1 = pd.read_csv(url1)
#print(df.dtypes) #utile per controllare data types "tabella" (file.csv)
 
meanBatteryA = df1.iloc[:,1].mean()
#Metodo alternativo per calcolare media sfruttando numpy ↓
#meanBatteryA = np.mean(df['BatteryLife'])
stdBatteryA = df1.iloc[:,1].std()
print('Mean Battery A: ' + str(meanBatteryA))
print(' Std Battery A: ' + str(stdBatteryA))
print()

url2 = 'https://raw.githubusercontent.com/TheNoobRoxas/bigData/main/producerB.csv'
df2 = pd.read_csv(url2)
meanBatteryB = df2.iloc[:,1].mean()
stdBatteryB = df2.iloc[:,1].std()
print('Mean Battery B: ' + str(meanBatteryB))
print(' Std Battery B: ' + str(stdBatteryB))
print()

choose = input('\nChoose a Statistic Analysis (1 OR 2): ')
choose = int(choose)
while choose != 1 and choose != 2:
  choose = input('!Not Available! - Choose Statistic Analysis (1 OR 2): ')
  choose = int(choose)

if choose == 1:
  print('\nSTATISTIC ANALYSIS 1 : Producer A ↓\n')
  plt.plot(df1['BatteryLife'])

if choose == 2:
  print('\nSTATISTIC ANALYSIS 2 : Producer B ↓\n')
  plt.plot(df2['BatteryLife'])

