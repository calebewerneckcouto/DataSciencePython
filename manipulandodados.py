import numpy as np

idades =[30,5,10,7]

print(np.min(idades))
print(np.max(idades))
print(np.mean(idades)) #media
print(np.std(idades))#desvio padrao
print(np.sum(idades))#soma
print(idades[1])#indice
print(idades.append(np.nan))
print(np.isnan(idades[4]))#ver se e vazio
idades.remove(np.nan) #remove o nan
print(np.quantile(idades,0.75)) # retonra o quantile
print(idades)