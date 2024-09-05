import numpy as np  # Importa a biblioteca NumPy para operações com arrays e geração de números aleatórios
import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados com Series e DataFrames

# Criação de uma Series a partir de um dicionário
d = {'Python': 10, 'JavaScript': 9, 'Matlab': 7}  # Dicionário de linguagens e suas pontuações
series = pd.Series(d)  # Converte o dicionário em uma Series
print(series)  # Exibe a Series resultante

# Indexação
# Criação de uma Series com dados aleatórios
# Gera 10 números inteiros aleatórios entre 1 e 5, e associa a um índice que vai de 'A' a 'J'
s = pd.Series(data=np.random.randint(1, 5, 10), index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
print(s[0])  # Acessa o primeiro elemento da Series usando indexação por posição
print(s['A'])  # Acessa o elemento com índice 'A'
print(s[0:2])  # Acessa os dois primeiros elementos usando fatiamento posicional
print(s['A':'B'])  # Acessa o intervalo de 'A' até 'B' (inclusivo) usando fatiamento por rótulos

# Indexação por fatiamento de uma Series criada a partir de um dicionário
print(series['Python':'JavaScript'])  # Acessa os dados de 'Python' até 'JavaScript' (inclusivo)

# Operações com Series
# Criação de duas Series, ambas com três valores inteiros aleatórios e índices específicos
s1 = pd.Series(data=np.random.randint(1, 100, 3), index=['Facebook', 'Instagram', 'Youtube'])
s2 = pd.Series(data=np.random.randint(1, 100, 3), index=['Zoom', 'Instagram', 'Youtube'])

# Exibe o conteúdo das duas Series
print("\ns1:\n", s1)
print("\ns2:\n", s2)

# Soma entre as duas Series
# A operação realiza a soma com base nos índices correspondentes. Se um índice não existe em uma Series, será substituído por NaN.
print("\ns1 + s2:\n", s1 + s2)  # Soma elementos com os mesmos índices ('Instagram' e 'Youtube') e resulta em NaN para índices que não correspondem
