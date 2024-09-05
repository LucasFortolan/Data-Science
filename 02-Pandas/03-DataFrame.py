import numpy as np  # Importa a biblioteca NumPy, usada para criar arrays e realizar operações matemáticas.
import pandas as pd  # Importa a biblioteca Pandas, usada para manipulação de dados com DataFrames e Series.

# DataFrame: É uma estrutura de dados bidimensional, semelhante a uma tabela com linhas e colunas.
# DataFrame é uma coleção de Series, onde cada coluna é uma Series.

# Criando um array NumPy de 3 linhas e 3 colunas, contendo dados de 'Peso', 'Altura' e 'Idade'.
dados = np.array([[72, 180, 26], [80, 170, 19], [26, 19, 15]])

# Imprime o array de dados criado.
print(dados)

# Converte o array NumPy em um DataFrame Pandas, onde:
# 'data=dados' define os dados do DataFrame e
# 'columns=['Peso', 'Altura', 'Idade']' define os nomes das colunas.
df = pd.DataFrame(data=dados, columns=['Peso', 'Altura', 'Idade'])

# Imprime o DataFrame criado. Ele será exibido como uma tabela com as colunas 'Peso', 'Altura' e 'Idade'.
print(df)

# Indexação: Acessando dados específicos no DataFrame.

# Retorna a coluna 'Altura' do DataFrame como uma Series.
print('\n\n', df['Altura'])

# Imprime o tipo do objeto retornado. No caso, será 'pandas.core.series.Series', que é uma coluna individual de um DataFrame.
print(type(df['Altura']))

# Retorna a linha com índice 1 (segunda linha), mostrando os valores de 'Peso', 'Altura' e 'Idade' para essa linha.
print(df.loc[1])

# O correto seria acessar a linha e depois a coluna.
df.loc[1, 'Altura']

# Usando 'iloc', que faz indexação posicional, para acessar o valor na linha 2 (índice 2) e na coluna 1 (índice 1).
# Neste caso, será a altura da terceira pessoa.
print(df.iloc[2][1])  # Imprime o valor correspondente à Altura da terceira linha.


