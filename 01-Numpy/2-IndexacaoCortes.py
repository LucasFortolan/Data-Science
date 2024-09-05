import numpy as np  # Importa a biblioteca NumPy para operações com arrays e cálculos numéricos

# Criação de arrays comuns
e = np.ones(10)  # Cria um array de tamanho 10 preenchido com o valor 1
print(e)  # Exibe o array 'e'

ee = np.zeros((2, 2))  # Cria uma matriz 2x2 preenchida com zeros
print(ee)  # Exibe a matriz 'ee'

f = np.random.rand(10)  # Gera um array de 10 números aleatórios entre 0 e 1 (distribuição uniforme)
print(f)  # Exibe o array 'f'

# Indexação e fatiamento (slices) de arrays
# Array unidimensional
g = np.arange(10, 21)  # Cria um array com valores inteiros de 10 a 20
print(g)  # Exibe o array 'g'

print(g[0])  # Exibe o primeiro elemento (na posição 0)
print(g[-1])  # Exibe o último elemento do array (indexação negativa)
print(g[2:5])  # Exibe os elementos de posição 2 a 4 (5 não é incluído)
print(g[2:])  # Exibe os elementos a partir da posição 2 até o final
print(g[2:9:2])  # Exibe elementos de 2 até 8 (não inclui 9) com passo de 2: [inicio,fim, passo]
print(g[8:2:-1])  # Exibe os elementos de 8 a 3 (decrescente)

# Array bidimensional
h = np.random.rand(5, 5)  # Gera uma matriz 5x5 com valores aleatórios entre 0 e 1
print(h)  # Exibe a matriz 'h'

print(h[0][1])  # Acessa o elemento da primeira linha (índice 0) e segunda coluna (índice 1)
# Alternativa para o acesso de elemento em array multidimensional:
print(h[0, 1])  # Acessa o mesmo elemento usando uma notação simplificada

print(h[0:2, 2])  # Exibe os elementos da 3ª coluna (índice 2) nas duas primeiras linhas (índice 0 e 1)
