import pandas as pd  # Importa a biblioteca pandas, usada para manipulação de dados

# Dicionário contendo dados dos jogadores: nome, ano e pontuação
players_data = {
    'Player': ['Superman', 'Batman', 'Thanos', 'Batman', 'Thanos',
               'Superman', 'Batman', 'Thanos', 'Ironman', 'Batman', 'Thanos', 'Superman'],
    'Year': [2015, 2015, 2015, 2016, 2016, 2017, 2017, 2017, 2018, 2019, 2019, 2020],
    'Points': [23, 43, 45, 65, 76, 34, 23, 78, 89, 76, 92, 87]
}

# Cria um DataFrame a partir do dicionário de dados
df = pd.DataFrame(players_data)

# Exibe o DataFrame original
print("df Original:\n", df)

# Agrupa os dados pelo nome do jogador
groups_df = df.groupby('Player')

print("")  # Linha em branco para melhor formatação na saída

# Itera sobre cada grupo (um para cada jogador)
for player, group in groups_df:
    print("----- {} -----".format(player))  # Imprime o nome do jogador como cabeçalho
    print(group)  # Imprime o DataFrame correspondente ao grupo atual (jogador)
    print("")  # Linha em branco para separar os grupos na saída

# Filtra os jogadores que têm pontuação maior que 60
best_df = df.loc[df.Points > 60]
print("Best Players:\n", best_df)  # Exibe os jogadores que têm pontuação acima de 60

# Filtra os jogadores que têm pontuação maior que 60, excluindo o jogador 'Ironman'
best_df = df[(df.Points > 60) & (df.Player != 'Ironman')]
print("Best Players: (excluindo Ironman)\n", best_df)  # Exibe os melhores jogadores, sem incluir 'Ironman'
