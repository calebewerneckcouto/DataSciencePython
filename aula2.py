import numpy as np

idades = [30,5,10,7]


# min = Mínimo

minimo = np.min(idades)


# max = Máximo

maximo = np.max(idades)


#mean = média

media = np.mean(idades)


#std = Desvio Padrão

dv= np.std(idades)

# sum = Soma

soma = np.sum(idades)

# isnan - Retorna True quando o valor é vazio
# nan - Retorna um valor vazio

isNan = idades[1]

np.nan

idade = idades.append(np.nan)

dados = np.isnan(idades[4])

idades.remove(np.nan)


quantil = np.quantile(idades,0.75)


print(minimo,maximo,media,dv)
print(isNan)
print(idades)
print(idade)
print(dados)
print(quantil)