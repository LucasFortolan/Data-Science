import pandas as pd
import numpy as np

dados = np.array([[1, 2, np.nan],
                  [4, np.nan, np.nan],
                  [7, 8, 9]])

df = pd.DataFrame(dados, columns='A B C'.split())

print(df.isnull()) # Para verificar os valores nulos.

df.dropna()  # Remove linhas com valores nulos
df.dropna(axis=1)  # Remove colunas com valores nulos

df.fillna(0)  # Substitui valores NaN por 0
df.fillna(method='ffill')  # Preenche NaN com o valor anterior
