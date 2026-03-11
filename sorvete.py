import pandas as pd

# 1. Carregar a base de dados
# Certifique-se de que o nome do arquivo abaixo é exatamente igual ao que você baixou
df_sorvete = pd.read_csv('ice_cream_sales_temperatures.csv') 

# 2. Mostrar as primeiras linhas para conferir os nomes das colunas
print("--- Dados Originais ---")
print(df_sorvete.head())

# 3. Ordenar os valores pela coluna 'Temperature'
#ascendending=True deixa do mais frio para o mais quente
df_ordenado = df_sorvete.sort_values(by='Temperature', ascending=True)

# 4. Mostrar o resultado na tela
print("\n--- Valores Ordenados por Temperatura (do menor para o maior) ---")
#print(df_ordenado)

#df_ordenado = df_sorvete.sort_values(by='Temperature').reset_index(drop=True)
#print(df_ordenado.head())

# 1. Criar o grupo (filtro)
# Lógica: Temperatura maior ou igual a 39 E temperatura menor ou igual a 41
filtro_calor = df_sorvete[(df_sorvete['Temperature'] >= 39) & (df_sorvete['Temperature'] <= 41)]

# 2. Ordenar esse grupo para facilitar a leitura
filtro_calor = filtro_calor.sort_values(by='Temperature')

# 3. Mostrar o resultado
print(f"--- Dias com temperatura entre 39°C e 41°C ---")
if filtro_calor.empty:
    print("Nenhum registro encontrado nessa faixa de temperatura.")
else:
    print(filtro_calor)

# 4. Quantos dias foram encontrados?
print(f"\nTotal de dias encontrados: {len(filtro_calor)}")
# Estudo realizado em Março de 2026.