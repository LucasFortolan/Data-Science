import numpy as np  # Importa a biblioteca NumPy para realizar operações matemáticas
import pandas as pd  # Importa a biblioteca Pandas para manipulação de dados com Series e DataFrames

# Series: Estrutura de dados de uma dimensão, semelhante a uma coluna em uma tabela

# Criação de uma Series simples, sem índices nomeados
steps = pd.Series([4216, 3867, 7934, 4180, 5344])  # Passos diários registrados durante a semana
print(steps)  # Exibe a Series contendo o número de passos diários
print(type(steps))  # Exibe o tipo da variável (Series)
print(steps.values)  # Exibe os valores da Series
print(steps.index)  # Exibe o índice da Series (posições dos elementos, de 0 a 4)

# Criação de uma Series com índices nomeados (dias da semana)
stepsIndex = pd.Series(data=[4216, 3867, 7934, 4180, 5344], index=['seg', 'ter', 'qua', 'qui', 'sex'])
print(stepsIndex)  # Exibe a Series com os índices (dias) e os valores (passos)
print(stepsIndex.index)  # Exibe os índices da Series (neste caso, dias da semana)
print(stepsIndex.values)  # Exibe os valores da Series (número de passos por dia)

# Realizando operações estatísticas básicas
print("\n\nOperações\n")
print("Mínimo: ", stepsIndex.min())  # Exibe o menor número de passos registrados
print("Máximo: ", stepsIndex.max())  # Exibe o maior número de passos registrados
print("Média: ", stepsIndex.mean())  # Exibe a média dos passos diários
print("Soma: ", stepsIndex.sum())  # Exibe a soma total dos passos registrados na semana

# Exibe uma descrição estatística dos dados, como contagem, média, desvio padrão, etc.
print("\nDescrição:\n ", stepsIndex.describe())

# Operações matemáticas com a Series
print("\n2x: \n", stepsIndex * 2)  # Multiplica os valores por 2 (operações vetoriais são automáticas com Series)
print("\nRaiz Quadrada\n", np.sqrt(stepsIndex * 2))  # Calcula a raiz quadrada de cada valor multiplicado por 2
