# Importa a biblioteca Pandas para manipulação de dados
import pandas as pd  

# Lê o arquivo CSV 'train.csv' e armazena os dados em um DataFrame chamado 'base'
base = pd.read_csv(r'train.csv')  

# Variável criada, mas não utilizada no código
Age = 0  

# Exporta o DataFrame 'base' para um novo arquivo CSV chamado 'train_exportado.csv'
base.to_csv(r'train_exportado.csv')  

# Exibe as primeiras 5 linhas do DataFrame para visualizar os dados iniciais
print(base.head())  

# Exibe todo o conteúdo do DataFrame (se for grande, pode demorar para carregar tudo)
print(base)  

# Retorna estatísticas descritivas das colunas numéricas do DataFrame
print(base.describe())  

# Conta a quantidade de valores não nulos em cada coluna
print(base.count())  

# Soma os valores de todas as colunas numéricas
print(base.sum(numeric_only=True))  

# Exibe os tipos de dados de cada coluna (exemplo: int64, float64, object)
print(base.dtypes)  

# Seleciona apenas as colunas numéricas e calcula a média de cada uma
print(base.select_dtypes(include=['number']).mean()) 

# Head - Visualizar primeiras linhas da tabela

print(base.head() )

print(base['PassengerId'])

print(base[['PassengerId','Survived','Age']].mean())

print(type(base['Ticket'][1]))


print('--------------------------Segmentação DataFrame---------------------------------------------------------')

# Não segue a regra geral : Primeiro número incluso e último número também está incluso
# Porque estamos chamando rótulos, e não números

print(base.loc[0:5,['PassengerId','Pclass']])

print(# Segue a regra geral: Primeiro número incluso, e último número não incluso
# Porque estamos chamando índices/números e não rótulos

print(base.iloc[-4:,-3:]))
print(base[0:5])
print(base[['PassengerId','Survived']])
print(base[base['Survived'] == 1])

# Criar uma coluna Nova

base['ColunaNova'] = pd.Series()
print(base)
base['ColunaNova2'] = base['PassengerId'] + base['Survived']

print(base)


base2 = base[['PassengerId','Survived','Name']]
base3 = base[['PassengerId','Sex','Age']]

print(base2)
print(base3)

base4 = pd.merge(base2,base3, on = 'PassengerId', how = 'left')

print(base4)

base4.to_excel(r'trainexcel.xlsx')