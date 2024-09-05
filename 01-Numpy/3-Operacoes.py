import numpy as np  # Importa a biblioteca NumPy para operações com arrays e cálculos matemáticos
# Definindo uma semente para o gerador de números aleatórios, garantindo que os mesmos números sejam gerados a cada execução
np.random.seed(32)

# Geração de um array de inteiros aleatórios entre 1 e 20, com 8 elementos
a1 = np.random.randint(1, 20, 8)
print(a1)  # Exibe o array gerado
print(a1**2)  # Exibe o array com os valores elevados ao quadrado

# Gerando outro array com 8 inteiros aleatórios entre 1 e 100
a2 = np.random.randint(1, 100, 8)
print(a2)  # Exibe o segundo array

# Operações aritméticas entre os dois arrays
# Soma dos elementos correspondentes de a1 e a2
print("Soma:\n", a1 + a2)

# Subtração dos elementos correspondentes de a2 de a1
print("Subtração:\n", a1 - a2)

# Multiplicação dos elementos correspondentes de a1 e a2
print("Multiplicação:\n", a1 * a2)

# Divisão dos elementos correspondentes de a1 pelos de a2
print("Divisão:\n", a1 / a2)  # Pode gerar números decimais

# Comparações entre os dois arrays
print(a1 == a2)  # Compara os elementos de a1 e a2, resultando em um array de valores booleanos (True ou False)

# Verifica se os arrays são idênticos (considera tamanho e valores)
np.array_equal(a1, a2)  # Retorna True se a1 e a2 forem iguais, caso contrário, retorna False
