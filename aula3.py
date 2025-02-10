import pandas as pd
import numpy as np

base = pd.read_csv(r'train.csv')

print(base)

texto = 'Pedro Alves'

print(texto[0]+texto[-1]+' - Final')

def funcaopedro(texto):
    
    print(texto[0]+texto[-1]+ ' - Final')
    

funcaopedro('João Batista')    
funcaopedro('Rodrigo Santana')

def funcaopedro(texto = 'Pedro Alves'):
    """ Retorna a Primeira e a Última Letra do texto passado + a string - teste"""
    
    print(texto[0]+texto[-1]+ ' - Final')
    
funcaopedro = lambda x: x[0]+x[-1] + ' - Final'    
funcaopedro('Pedro Alves')

base['ColunaNova'] = pd.Series()
print(base)
print(base.index)
print(base)

# Fazendo a operação repetida para a coluna inteira

for i in base.index:
    base['ColunaNova'][i] = funcaopedro(base['Name'][i])

print(base)    

# Dica - Função Apply

base['ColunaNova2'] = base['Name'].apply(lambda x: funcaopedro(x))

print(base)

base['ColunaNova3'] = pd.Series()
print(base)


for i in base.index:
    if base['Name'][i][0] == 'B':
        base['ColunaNova3'][i] = funcaopedro(base['Name'][i])
    elif base['Name'][i][0] == 'C':
        base['ColunaNova3'][i] = funcaopedro(base['Name'][i])
    else:
        pass
    
print(base) 


base['ColunaNova4'] = pd.Series()

contador = 0
while contador <5:
    base['ColunaNova4'][contador] = funcaopedro(base['Name'][contador])
    contador = contador + 1
    
print(base.head(6))    

# Usamos o operador Try quando queremos rodar um código com tolerância a erros

# Definindo novamente a função Pedro

def funcaopedro(texto):
    
    return(texto[0]+texto[-1]+ ' - Final')


# Fazendo a operação repetida para a coluna inteira

for i in base.index:
    base['ColunaNova5'][i] = funcaopedro(base['Cabin'][i])   
    
# Fazendo a operação repetida para a coluna inteira
base['ColunaNova5'] = pd.Series()

for i in base.index:
    try:
        base['ColunaNova5'][i] = funcaopedro(base['Cabin'][i])
    except:
        #print('Erro no índice ' + str(i))
        base['ColunaNova5'][i] = funcaopedro('Pedro Alves')  
        
print(base)          