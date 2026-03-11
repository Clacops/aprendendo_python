# %%
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregar os dados (O Seaborn baixa automaticamente para você)
titanic = sns.load_dataset('titanic')

# 2. Configurar o "look" do gráfico (estilo fundo branco com linhas)
sns.set_theme(style="whitegrid")

# 3. Criar o gráfico de barras
# Queremos ver a classe (1ª, 2ª, 3ª) no eixo X
# A sobrevivência (0 ou 1) no eixo Y
# E separar as barras por sexo (homem/mulher)
sns.barplot(x="class", y="survived", hue="sex", data=titanic)

# 4. Adicionar um título bonito
plt.title("Quem sobreviveu ao Titanic? (Por Classe e Gênero)")

# 5. Mostrar o gráfico na tela
#plt.show()

import seaborn as sns
import pandas as pd

# 1. Carregar os dados
titanic = sns.load_dataset('titanic')

# 2. Ver as primeiras 5 linhas (O "Cartão de Visitas")
print("--- Primeiras 5 linhas do Titanic ---")
print(titanic.head())

# 3. Ver o "Raio-X" dos dados (Quantas colunas, tipos de dados, etc.)
print("\n--- Informações Gerais do Dataset ---")
print(titanic.info())

# 4. Ver as estatísticas (Média de idade, preço da passagem, etc.)
print("\n--- Resumo Estatístico ---")
print(titanic.describe())

import seaborn as sns
import pandas as pd

# 1. Carregamos os dados do navio
titanic = sns.load_dataset('titanic')

# 2. O comando mágico para criar o arquivo
# O nome entre aspas é como o arquivo vai se chamar na sua pasta
titanic.to_csv('meus_dados_titanic.csv', index=False, encoding='utf-8-sig')

print("Arquivo CSV criado com sucesso! Olhe na sua pasta à esquerda. 😉")

# %%
