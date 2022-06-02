from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from sklearn.preprocessing import MinMaxScaler
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Determinar a quantidade de dias para previsão
Qtd_dias_previsao = 90

base = pd.read_csv('N_seaice_extent_daily_v3.0.csv')
base = base.iloc[1:, :]

# Utilizar dados a partir de 1988, já que os dados foram atualizados de forma diária
# apenas a partir de 1988.

base = base.drop(base[base['Year'].astype(int) < 1988].index)
base = base.dropna()

base_teste = base.iloc[-Qtd_dias_previsao:, :]
base_teste = base_teste.iloc[:, 3:4].values

base_treinamento = base.iloc[:-Qtd_dias_previsao, :]
base_treinamento = base_treinamento.iloc[:, 3:4].values

normalizador = MinMaxScaler(feature_range=(0,1))
base_treinamento_normalizada = normalizador.fit_transform(base_treinamento)

previsores = []
extensao_real = []
for i in range(Qtd_dias_previsao, len(base_treinamento)):
    previsores.append(base_treinamento_normalizada[i-Qtd_dias_previsao:i, 0])
    extensao_real.append(base_treinamento_normalizada[i, 0])
previsores, extensao_real = np.array(previsores), np.array(extensao_real)
previsores = np.reshape(previsores, (previsores.shape[0], previsores.shape[1], 1))

regressor = Sequential()
regressor.add(LSTM(units = 100, return_sequences = True, input_shape = (previsores.shape[1], 1)))
regressor.add(Dropout(0.3))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.3))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.3))

regressor.add(LSTM(units = 50))
regressor.add(Dropout(0.3))

regressor.add(Dense(units = 1, activation = 'sigmoid'))

regressor.compile(optimizer = 'adam', loss = 'mean_squared_error',
                  metrics = ['mean_absolute_error'])

es = EarlyStopping(monitor = 'loss', min_delta = 1e-10, patience = 7, verbose = 1)
rlr = ReduceLROnPlateau(monitor = 'loss', factor = 0.2, patience = 5, verbose = 1)

regressor.fit(previsores, extensao_real, epochs = 70, batch_size = 25,
              callbacks = [es, rlr])


base_completa = base.iloc[:, 3:4]
entradas = base_completa[len(base_completa) - len(base_teste) - Qtd_dias_previsao:]
entradas = entradas.to_numpy().reshape(-1, 1)
entradas = normalizador.transform(entradas)


X_teste = []
for i in range(Qtd_dias_previsao, len(entradas)):
    X_teste.append(entradas[i-Qtd_dias_previsao:i, 0])
X_teste = np.array(X_teste)
X_teste = np.reshape(X_teste, (X_teste.shape[0], X_teste.shape[1], 1))
previsoes = regressor.predict(X_teste)
previsoes = normalizador.inverse_transform(previsoes)

print(previsoes.mean())
print(base_teste.astype(float).mean())

#valor médio da previsão: 13.9089155
#valor médio medido: 13.867099999999997

plt.plot(np.float64(base_teste), color = 'red', label = 'Extensão de gelo do oceano')
plt.plot(previsoes, color = 'blue', label = 'Previsões')
plt.title('Previsão Extensão de gelo')
plt.xlabel('Tempo (Dias)')
plt.ylabel('Valor medido pelo satélite (10^6 sq km)')
plt.legend()
plt.show()


























