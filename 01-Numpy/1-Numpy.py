import numpy as np  # Importa a biblioteca NumPy e a associa ao alias 'np'

# Criação de um array unidimensional
a = np.array([0, 1, 2, 3])  # Cria um array NumPy com os elementos 0, 1, 2 e 3
print(a)  # Imprime o array 'a'

# Criação de um array bidimensional
# Cria um array 2D (matriz) com duas linhas
b = np.array([[0, 1, 2], [3, 4, 5]])
print(type(b))  # Exibe o tipo da variável 'b' (deve ser <class 'numpy.ndarray'>)
print(b.ndim)  # Exibe o número de dimensões do array (neste caso, 2)
# Exibe as dimensões do array (número de linhas e colunas, neste caso (2, 3))
print(b.shape)
print(len(b))  # Exibe o número de linhas do array (neste caso, 2)

# Criação de arrays utilizando funções
# np.arange(start, stop, step) - gera um array com valores de 'start' até 'stop' (não inclusivo) com um intervalo 'step'
c = np.arange(0, 10, 2)  # Cria um array com valores de 0 a 10, com passo 2
print(c)  # Exibe o array 'c'

cc = np.arange(10)  # Cria um array com inteiros de 0 a 9 (passo 1 é padrão)
print(cc)  # Exibe o array 'cc'

# np.linspace(start, stop, num) - gera 'num' valores igualmente espaçados entre 'start' e 'stop'
# Cria um array com 10 valores igualmente espaçados entre 1 e 10
d = np.linspace(1, 10, 10)
print(d)  # Exibe o array 'd'

# Exemplo de linspace com endpoint=False, que exclui o valor final
# Gera 10 valores igualmente espaçados entre 1 e 10, excluindo o 10
dd = np.linspace(1, 10, 10, endpoint=False)
print(dd)  # Exibe o array 'dd'
