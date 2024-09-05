import pandas as pd

# Use barras duplas invertidas
file_path = "C:\\Users\\lucas\\Music\\ProdutosSemMovimentacao.xlsx"

# Ler o arquivo Excel e selecionar as colunas 'Código' e 'Produto'
df = pd.read_excel(file_path, usecols=['Código', 'Produto'])

# Renomear a coluna 'Produto' para 'Descrição'
df = df.rename(columns={'Produto': 'Descrição'})

# Converter a coluna 'Código' para string
df['Código'] = df['Código'].astype(str)

# Adicionar "Apagar " no início de cada valor na coluna 'Descrição'
df['Descrição'] = "Apagar " + df['Descrição']

# Exibir as primeiras linhas e os tipos de dados
print("Exibindo Algumas linhas:\n", df.head(5))

# sando shape para obter o número de linhas e colunas
print("\nNumero de Linhas:", df.shape[0])
print("Numero de Colunas:", df.shape[1])

# Salvar o DataFrame em um novo arquivo Excel (sem sobrescrever o arquivo original)
output_file = "c:\\Users\\lucas\\Music\\ProdutosSemMovimentacao_limpo.xlsx"
df.to_excel(output_file, index=False)
