import pandas as pd

# Carregar o Arquivo Excel de Backup com todas as colunas
file_path1 = "C:\\Users\\lucas\\Music\\produtosBackup_corrigido.xlsx"
df1 = pd.read_excel(file_path1)

# Carregar o Arquivo Excel Sem Movimentação
file_path2 = "c:\\Users\\lucas\\Music\\ProdutosSemMovimentacao_limpo.xlsx"
df2 = pd.read_excel(file_path2, usecols=['Código'])

# Fazer o merge entre as duas bases, mantendo todas as linhas de df2 e trazendo ID e Descrição de df1
# O 'left' merge garante que só os dados de df2 sejam mantidos
df_merged = pd.merge(df2, df1, on='Código', how='left')

# Exibir as primeiras linhas e os tipos de dados
print("Exibindo Algumas linhas:\n", df_merged.head(5))

# sando shape para obter o número de linhas e colunas
print("\nNumero de Linhas:", df_merged.shape[0])
print("Numero de Colunas:", df_merged.shape[1])

# Reorganizar as colunas na ordem fornecida
colunas_ordenadas = [
    'ID', 'Código', 'Descrição', 'Unidade', 'NCM', 'Origem', 'Preço', 'Valor IPI fixo', 
    'Observações', 'Situação', 'Estoque', 'Preço de custo', 'Cód no fornecedor', 
    'Fornecedor', 'Localização', 'Estoque maximo', 'Estoque minimo', 'Peso líquido (Kg)', 
    'Peso bruto (Kg)', 'GTIN/EAN', 'GTIN/EAN da embalagem', 'Largura do Produto', 
    'Altura do Produto', 'Profundidade do produto', 'Data Validade', 
    'Descrição do Produto no Fornecedor', 'Descrição Complementar', 'Unidade por Caixa', 
    'Produto Variação', 'Tipo Produção', 'Classe de enquadramento do IPI', 
    'Código da lista de serviços', 'Tipo do item', 'Grupo de Tags/Tags', 'Tributos', 
    'Código Pai', 'Código Integração', 'Grupo de produtos', 'Marca', 'CEST', 'Volumes', 
    'Descrição Curta', 'Cross-Docking', 'URL Imagens Externas', 'Link Externo', 
    'Meses Garantia no Fornecedor', 'Clonar dados do pai', 'Condição do produto', 
    'Frete Grátis', 'Número FCI', 'Vídeo', 'Departamento', 'Unidade de medida', 
    'Preço de compra', 'Valor base ICMS ST para retenção', 'Valor ICMS ST para retenção', 
    'Valor ICMS próprio do substituto', 'Categoria do produto', 'Informações Adicionais'
]

# Reorganizar o DataFrame com base na ordem das colunas
df_merged = df_merged[colunas_ordenadas]

# Remover as linhas que contêm valores NaN nas colunas'Código'
df_merged = df_merged.dropna(subset=['Código'])
print("\nRemovi os dados com NaN\n:", df_merged.head(5))

# sando shape para obter o número de linhas e colunas
print("\nNumero de Linhas:", df_merged.shape[0])
print("Numero de Colunas:", df_merged.shape[1])

# Salvar o resultado em um novo arquivo Excel
output_file = "c:\\Users\\lucas\\Music\\ComparacaoSomenteDf2.xlsx"
df_merged.to_excel(output_file, index=False)