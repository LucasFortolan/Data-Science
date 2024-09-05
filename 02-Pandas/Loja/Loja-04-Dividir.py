import pandas as pd

file_path1 = "c:\\Users\\lucas\\Music\\ComparacaoSomenteDf2.xlsx"
df = pd.read_excel(file_path1)

# Definir o número máximo de linhas por pedaço
tamanho_maximo = 1000

# Dividir o DataFrame em pedaços de no máximo 1000 linhas
def dividir_dataframe(df, tamanho_maximo):
    return [df[i:i + tamanho_maximo] for i in range(0, len(df), tamanho_maximo)]

# Dividir o DataFrame
pedaços = dividir_dataframe(df, tamanho_maximo)

# Salvar cada pedaço em arquivos Excel separados
for i, pedaço in enumerate(pedaços):
    output_file = f"c:\\Users\\lucas\\Music\\planilhaMergePedaco_{i+1}.xlsx"
    pedaço.to_excel(output_file, index=False)

# Exibir as primeiras linhas do primeiro pedaço como exemplo
print(pedaços[0].head())