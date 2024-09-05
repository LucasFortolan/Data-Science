# pip install lxml
# Utiliza para obter os dados da planilha pelo HTML
import pandas as pd

# Tentando ler o arquivo CSV
try:
    df = pd.read_csv('c:/Users/lucas/OneDrive/Documentos/Python/Data/02-Pandas/titanic-Dataset.csv',
                     usecols=['Name', 'Sex', 'Age'])
    print("CSV carregado com sucesso!")

    print(df.head(7))  # Exibe as primeiras 7 linhas
    print(df.describe())  # Exibe estatísticas descritivas
    print(df.shape)  # Exibe a forma do DataFrame (linhas, colunas)

except FileNotFoundError:
    print("Erro: O arquivo CSV não foi encontrado no caminho especificado.")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo CSV está vazio.")
except Exception as e:
    print(f"Um erro inesperado ocorreu ao carregar o CSV: {e}")

# Tentando ler uma tabela da página web
try:
    dfHTML = pd.read_html('https://fdic.gov/bank/individual/failed/banklist.html')
    print(f"Número de tabelas encontradas na página: {len(dfHTML)}")

except ValueError:
    print("Erro: Não foram encontradas tabelas na página especificada.")
except Exception as e:
    print(f"Um erro inesperado ocorreu ao carregar a tabela da web: {e}")




