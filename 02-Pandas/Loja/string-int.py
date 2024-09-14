import pandas as pd

# Use barras duplas invertidas para o caminho do arquivo
file_path = "c:\\Users\\lucas\\Music\\relatorioSemMovimentacao-06-09.xlsx"

# Ler o arquivo Excel
df = pd.read_excel(file_path)

# Verificar se a coluna 'Código' existe antes de manipulá-la
if 'Estoque' in df.columns:
    # Converter a coluna 'Código' para int, substituindo valores inválidos por NaN
    df['Estoque'] = pd.to_numeric(df['Estoque'], errors='coerce').astype('Int64')
else:
    print("Coluna 'Estoque' não encontrada no arquivo.")

# Exibir as primeiras linhas e os tipos de dados
print(f"Exibindo algumas linhas:\n{df.head(5)}")

# Exibir o número de linhas e colunas usando shape
print(f"\nNúmero de Linhas: {df.shape[0]}")
print(f"Número de Colunas: {df.shape[1]}")

# Salvar o DataFrame em um novo arquivo Excel (sem sobrescrever o arquivo original)
# output_file = r"C:\Users\lucas\Music\ProdutosSemMovimentacao_limpo.xlsx"
# df.to_excel(output_file, index=False)
