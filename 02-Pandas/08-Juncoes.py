import pandas as pd
import numpy as np

# Criando um array com números de 1 a 9 e reformulando em uma matriz 3x3
dados = np.arange(1, 10).reshape(3, 3)
print("Matriz de dados:\n", dados)

# Convertendo o array para DataFrames separados para concatenação
df1 = pd.DataFrame(dados, columns=['A', 'B', 'C'])
df2 = pd.DataFrame(dados * 10, columns=['A', 'B', 'C'])  # Um DataFrame diferente para exemplo

# Concatenar 

# Concatenando os DataFrames, se não usar o ignore_index=True, copia o index da segunda, teria indices repetitidos
df_concatenado = pd.concat([df1, df2], ignore_index=True)
# Concatenando Verticalmente, aumentando as colunas
df_concatenado = pd.concat([df1, df2], axis=1)

print("\nDataFrames concatenados:\n", df_concatenado)


#Merge
