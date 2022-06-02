import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Script apenas para plotar a média anual da extensão de gelo do oceano artico.

base = pd.read_csv('N_seaice_extent_daily_v3.0.csv')
base = base.dropna()

enso = pd.read_csv('ENSO.csv')
enso_1978 = enso.loc[enso['Year'] >= 1978]
enso_1978 = enso_1978.loc[enso_1978['Year'] < 2022]


base_extensao = base.iloc[:, 3:4].values

dados_dic = {i: base.loc[base['Year'] == ('' ''.join(str(i)))].iloc[:, 3:4].values.astype(np.float64) for i in range(1978,2023)}
medias_dic = {ano: np.mean(dados_dic[ano]) for ano in range(1978, 2022)}

plt.plot(medias_dic.keys(), medias_dic.values(), color = 'black')
plt.show()

