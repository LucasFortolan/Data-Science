import pandas as pd
import numpy as np

# Carregando o arquivo CSV
df = pd.read_csv('c:/Users/lucas/OneDrive/Documentos/Python/Data/02-Pandas/titanic-Dataset.csv')

# Agrupando o DataFrame pela coluna 'Survived'
df_Survived = df.groupby('Survived')

# Selecionando apenas as colunas numéricas
df_numeric = df.select_dtypes(include=[np.number])

# Exibindo a média dos grupos apenas para as colunas numéricas
print("\nMédia dos grupos por 'Survived' (somente colunas numéricas):")
print(df_Survived[df_numeric.columns].mean())

# Para visualizar os dados agrupados, você pode aplicar uma função de agregação, como a média, contagem, etc.
df_sex = df.groupby('Sex')
print("\nMédia dos grupos por 'Sexo' (somente colunas numéricas):")
print(df_sex[df_numeric.columns].mean())




