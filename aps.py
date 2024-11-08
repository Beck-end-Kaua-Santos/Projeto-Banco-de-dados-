import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '2021.xlsx'
df = pd.read_excel(file_path)

# Calcular o percentual de ocupação usando NumPy
df['PERCENTUAL_OCUPACAO'] = np.divide(df['OCUPADA'], df['APROVADA']) * 100  

# Top 5 órgãos com maior percentual de ocupação
df_sorted = df.sort_values(by='PERCENTUAL_OCUPACAO', ascending=False).head(5)
print("Top 5 Órgãos com Maior Percentual de Ocupação:")
print(df_sorted[['SIGLA_ORGAO', 'PERCENTUAL_OCUPACAO']])

plt.figure(figsize=(8, 5))
plt.barh(df_sorted['SIGLA_ORGAO'], df_sorted['PERCENTUAL_OCUPACAO'], color='teal')
plt.xlabel('Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Maior Percentual de Ocupação')
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()

# Agrupamento por órgão para cargos aprovados, ocupados e vagas
cargos_por_orgao = df.groupby('NOME_ORGAO')[['APROVADA', 'OCUPADA', 'VAGA']].sum().sort_values(by='APROVADA', ascending=False)

# Top 10 órgãos com maior quantidade de cargos aprovados
top_10_orgao = cargos_por_orgao.head(10)
print("\nTop 10 Órgãos com Maior Quantidade de Cargos Aprovados, Ocupados e Vagas:")
print(top_10_orgao[['APROVADA', 'OCUPADA', 'VAGA']])

top_10_orgao[['APROVADA', 'OCUPADA', 'VAGA']].plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('Top 10 Órgãos com Maior Quantidade de Cargos Aprovados, Ocupados e Vagas')
plt.xlabel('Órgão')
plt.ylabel('Quantidade de Cargos')
plt.xticks(rotation=75)
plt.grid(True)
plt.tight_layout()
plt.show()

# Calcular a média do percentual de ocupação com NumPy
percentual_ocupacao_mean = np.mean(df['PERCENTUAL_OCUPACAO'])
print(f'\nMédia do Percentual de Ocupação: {percentual_ocupacao_mean:.2f}%')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '2021.xlsx'
df = pd.read_excel(file_path)

# Calcular o percentual de ocupação usando NumPy
df['PERCENTUAL_OCUPACAO'] = np.divide(df['OCUPADA'], df['APROVADA']) * 100  

# Top 5 órgãos com menor percentual de ocupação
df_sorted_low_occup = df.sort_values(by='PERCENTUAL_OCUPACAO', ascending=True).head(5)
print("Top 5 Órgãos com Menor Percentual de Ocupação:")
print(df_sorted_low_occup[['SIGLA_ORGAO', 'PERCENTUAL_OCUPACAO']])

plt.figure(figsize=(8, 5))
plt.barh(df_sorted_low_occup['SIGLA_ORGAO'], df_sorted_low_occup['PERCENTUAL_OCUPACAO'], color='lightblue')
plt.xlabel('Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Menor Percentual de Ocupação')
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()

# Top 5 órgãos com menor número de vagas
df_sorted_low_vagas = df.sort_values(by='VAGA', ascending=True).head(5)
print("\nTop 5 Órgãos com Menor Número de Vagas Disponíveis:")
print(df_sorted_low_vagas[['SIGLA_ORGAO', 'VAGA']])

plt.figure(figsize=(8, 5))
plt.barh(df_sorted_low_vagas['SIGLA_ORGAO'], df_sorted_low_vagas['VAGA'], color='lightcoral')
plt.xlabel('Número de Vagas')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Menor Número de Vagas Disponíveis')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

########################################

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'tabela.xlsx'
df = pd.read_excel(file_path)

# Calcular o percentual de ocupação usando NumPy
df['PERCENTUAL_OCUPACAO'] = np.divide(df['OCUPADA'], df['APROVADA']) * 100  

# Top 5 órgãos com maior percentual de ocupação
df_sorted = df.sort_values(by='PERCENTUAL_OCUPACAO', ascending=False).head(5)
print("Top 5 Órgãos com Maior Percentual de Ocupação:")
print(df_sorted[['SIGLA_ORGAO', 'PERCENTUAL_OCUPACAO']])

plt.figure(figsize=(8, 5))
plt.barh(df_sorted['SIGLA_ORGAO'], df_sorted['PERCENTUAL_OCUPACAO'], color='teal')
plt.xlabel('Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Maior Percentual de Ocupação')
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()

# Agrupamento por órgão para cargos aprovados, ocupados e vagas
cargos_por_orgao = df.groupby('NOME_ORGAO')[['APROVADA', 'OCUPADA', 'VAGA']].sum().sort_values(by='APROVADA', ascending=False)

# Top 10 órgãos com maior quantidade de cargos aprovados
top_10_orgao = cargos_por_orgao.head(10)
print("\nTop 10 Órgãos com Maior Quantidade de Cargos Aprovados, Ocupados e Vagas:")
print(top_10_orgao[['APROVADA', 'OCUPADA', 'VAGA']])

top_10_orgao[['APROVADA', 'OCUPADA', 'VAGA']].plot(kind='bar', stacked=True, figsize=(10,6))
plt.title('Top 10 Órgãos com Maior Quantidade de Cargos Aprovados, Ocupados e Vagas')
plt.xlabel('Órgão')
plt.ylabel('Quantidade de Cargos')
plt.xticks(rotation=75)
plt.grid(True)
plt.tight_layout()
plt.show()

# Calcular a média do percentual de ocupação com NumPy
percentual_ocupacao_mean = np.mean(df['PERCENTUAL_OCUPACAO'])
print(f'\nMédia do Percentual de Ocupação: {percentual_ocupacao_mean:.2f}%')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = 'tabela.xlsx'
df = pd.read_excel(file_path)

# Calcular o percentual de ocupação usando NumPy
df['PERCENTUAL_OCUPACAO'] = np.divide(df['OCUPADA'], df['APROVADA']) * 100  

# Top 5 órgãos com menor percentual de ocupação
df_sorted_low_occup = df.sort_values(by='PERCENTUAL_OCUPACAO', ascending=True).head(5)
print("Top 5 Órgãos com Menor Percentual de Ocupação:")
print(df_sorted_low_occup[['SIGLA_ORGAO', 'PERCENTUAL_OCUPACAO']])

plt.figure(figsize=(8, 5))
plt.barh(df_sorted_low_occup['SIGLA_ORGAO'], df_sorted_low_occup['PERCENTUAL_OCUPACAO'], color='lightblue')
plt.xlabel('Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Menor Percentual de Ocupação')
plt.gca().invert_yaxis()  
plt.tight_layout()
plt.show()

# Top 5 órgãos com menor número de vagas
df_sorted_low_vagas = df.sort_values(by='VAGA', ascending=True).head(5)
print("\nTop 5 Órgãos com Menor Número de Vagas Disponíveis:")
print(df_sorted_low_vagas[['SIGLA_ORGAO', 'VAGA']])

plt.figure(figsize=(8, 5))
plt.barh(df_sorted_low_vagas['SIGLA_ORGAO'], df_sorted_low_vagas['VAGA'], color='lightcoral')
plt.xlabel('Número de Vagas')
plt.ylabel('Órgão')
plt.title('Top 5 Órgãos com Menor Número de Vagas Disponíveis')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados de cada ano
file_path_2021 = '2021.xlsx'
file_path_2022 = 'tabela.xlsx'  # Supondo que o outro arquivo é de 2022

df_2021 = pd.read_excel(file_path_2021)
df_2022 = pd.read_excel(file_path_2022)

# Calcular o percentual de ocupação em ambos os anos
df_2021['PERCENTUAL_OCUPACAO'] = np.divide(df_2021['OCUPADA'], df_2021['APROVADA']) * 100
df_2022['PERCENTUAL_OCUPACAO'] = np.divide(df_2022['OCUPADA'], df_2022['APROVADA']) * 100

# Selecionar colunas de interesse e renomear para o ano correspondente
df_2021 = df_2021[['SIGLA_ORGAO', 'NOME_ORGAO', 'APROVADA', 'OCUPADA', 'VAGA', 'PERCENTUAL_OCUPACAO']].copy()
df_2022 = df_2022[['SIGLA_ORGAO', 'NOME_ORGAO', 'APROVADA', 'OCUPADA', 'VAGA', 'PERCENTUAL_OCUPACAO']].copy()

df_2021.columns = [f"{col}_2021" for col in df_2021.columns]
df_2022.columns = [f"{col}_2022" for col in df_2022.columns]

# Juntar os dados por SIGLA_ORGAO e NOME_ORGAO
df_comparacao = pd.merge(df_2021, df_2022, left_on='SIGLA_ORGAO_2021', right_on='SIGLA_ORGAO_2022')

# Calcular variações
df_comparacao['VARIACAO_OCUPACAO'] = df_comparacao['PERCENTUAL_OCUPACAO_2022'] - df_comparacao['PERCENTUAL_OCUPACAO_2021']
df_comparacao['VARIACAO_VAGAS'] = df_comparacao['VAGA_2022'] - df_comparacao['VAGA_2021']

# Separar os Top 5 que mais aumentaram e diminuíram no percentual de ocupação
top_5_aumento_ocupacao = df_comparacao.nlargest(5, 'VARIACAO_OCUPACAO')
top_5_diminui_ocupacao = df_comparacao.nsmallest(5, 'VARIACAO_OCUPACAO')

# Separar os Top 5 que mais aumentaram e diminuíram no número de vagas
top_5_aumento_vagas = df_comparacao.nlargest(5, 'VARIACAO_VAGAS')
top_5_diminui_vagas = df_comparacao.nsmallest(5, 'VARIACAO_VAGAS')

# Exibir tabelas no console
print("Top 5 Órgãos com Maior Aumento no Percentual de Ocupação:")
print(top_5_aumento_ocupacao[['SIGLA_ORGAO_2021', 'PERCENTUAL_OCUPACAO_2021', 'PERCENTUAL_OCUPACAO_2022', 'VARIACAO_OCUPACAO']])

print("\nTop 5 Órgãos com Maior Diminuição no Percentual de Ocupação:")
print(top_5_diminui_ocupacao[['SIGLA_ORGAO_2021', 'PERCENTUAL_OCUPACAO_2021', 'PERCENTUAL_OCUPACAO_2022', 'VARIACAO_OCUPACAO']])

print("\nTop 5 Órgãos com Maior Aumento no Número de Vagas:")
print(top_5_aumento_vagas[['SIGLA_ORGAO_2021', 'VAGA_2021', 'VAGA_2022', 'VARIACAO_VAGAS']])

print("\nTop 5 Órgãos com Maior Diminuição no Número de Vagas:")
print(top_5_diminui_vagas[['SIGLA_ORGAO_2021', 'VAGA_2021', 'VAGA_2022', 'VARIACAO_VAGAS']])

# Gráfico comparativo para o percentual de ocupação
plt.figure(figsize=(12, 6))
plt.barh(top_5_aumento_ocupacao['SIGLA_ORGAO_2021'], top_5_aumento_ocupacao['VARIACAO_OCUPACAO'], color='teal', label='Aumento')
plt.barh(top_5_diminui_ocupacao['SIGLA_ORGAO_2021'], top_5_diminui_ocupacao['VARIACAO_OCUPACAO'], color='lightblue', label='Diminuição')
plt.xlabel('Variação no Percentual de Ocupação (%)')
plt.ylabel('Órgão')
plt.title('Top 5 Aumentos e Diminuições no Percentual de Ocupação (2021-2022)')
plt.legend()
plt.tight_layout()
plt.show()

# Gráfico comparativo para o número de vagas
plt.figure(figsize=(12, 6))
plt.barh(top_5_aumento_vagas['SIGLA_ORGAO_2021'], top_5_aumento_vagas['VARIACAO_VAGAS'], color='salmon', label='Aumento')
plt.barh(top_5_diminui_vagas['SIGLA_ORGAO_2021'], top_5_diminui_vagas['VARIACAO_VAGAS'], color='lightcoral', label='Diminuição')
plt.xlabel('Variação no Número de Vagas')
plt.ylabel('Órgão')
plt.title('Top 5 Aumentos e Diminuições no Número de Vagas (2021-2022)')
plt.legend()
plt.tight_layout()
plt.show()


