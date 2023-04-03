from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler



df = pd.read_csv(r'C:\Users\nazem\PycharmProjects\pythonProject\Big Data\Produttori\file\risultati_google.csv')
df['numero_caratteri'] = df['numero_caratteri'].astype(int)
df['numero_risultati_google'] = df['numero_risultati_google'].str.replace('.', '').astype(int)


cols_to_use = ['PageRank','numero_caratteri']

X = df[cols_to_use]
y = df.numero_risultati_google

scaler = StandardScaler()
X = scaler.fit_transform(X)


X_train, X_valid, y_train, y_valid = train_test_split(X,y)

my_model = XGBRegressor(n_estimators=1000, learning_rate=0.05)
my_model.fit(X_train, y_train,
             early_stopping_rounds=5,
             eval_set=[(X_valid, y_valid)],
             verbose=False)

predictions = my_model.predict(X_valid)
print("Mean Absolute Error: " + str(mean_absolute_error(predictions, y_valid)))