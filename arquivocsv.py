import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Lendo o arquivo CSV
base = pd.read_csv('dados.csv', sep=None, engine='python')

# Salvando em um novo arquivo CSV (opcional)
base.to_csv('total.csv', index=False)




# Exibindo as primeiras linhas do DataFrame
print(base.head())

print(base.describe()) # variaveis numericas nao contam variaveis nan

print(base.count())


base['Coluna Nova Nome'] = pd.Series()

# Criando a nova coluna com a primeira e última letra da coluna 'Nome'
base['Coluna Nova Nome'] = base['Nome'].apply(lambda x: x[0] + x[-1] if isinstance(x, str) and len(x) > 1 and x[0] != 'M' else x)


# Exibindo o DataFrame com a nova coluna
print(base[['Nome', 'Coluna Nova Nome']])
print(base.index)
# Exibindo o cabeçalho (nomes das colunas)
print(base.columns)


#trazer apenas uma coluna especifica

print(base['Nome'])

#trazer duas colunas especifica

print(base[['Total das peças','Total de serviços']])

print(base.dtypes)  # tipo de saida de dados

print(base.iloc[-2:,2:])

print(base[base['Descrição']== 'Verificação de Equipamento'])
base2 = base[['Nome','Problema','Técnico']]
print(base2)



base3 =base[['Nome','Município','Equipamento']]
print(base3)



base_merged = pd.merge(base2, base3, on='Nome', how='inner')  # Apenas correspondências exatas
base_merged = base_merged.fillna('')  # Substitui NaN por string vazia



print(base_merged)



base.to_excel('total.xlsx', index=False, engine='openpyxl')