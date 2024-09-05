import pandas as pd

# Use barras duplas invertidas
file_path = "C:\\Users\\lucas\\Music\\produtos.csv"

# Ler o arquivo CSV
df = pd.read_csv(file_path, sep=';')  # Ajuste o delimitador conforme o arquivo

# Converter a coluna 'Código' para string
df['Código'] = df['Código'].astype(str)

# Remover \t dos nomes das colunas
df.columns = df.columns.str.replace('\t', '', regex=False)

# Remover \t dentro dos dados, se presente
df = df.apply(lambda col: col.map(lambda x: x.replace('\t', '') if isinstance(x, str) else x))

# Exibir as primeiras linhas e os tipos de dados
print("Exibindo Algumas linhas:\n", df.head(5))

# sando shape para obter o número de linhas e colunas
print("\nNumero de Linhas:", df.shape[0])
print("Numero de Colunas:", df.shape[1])

# Salvar o DataFrame em um novo arquivo Excel (sem sobrescrever o arquivo original)
output_file = "C:\\Users\\lucas\\Music\\produtosBackup_corrigido.xlsx"
df.to_excel(output_file, index=False)
