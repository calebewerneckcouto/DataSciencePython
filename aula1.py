import pandas as pd
import numpy as np

texto = 'testando'

textoModificado =texto.replace('t','T')

print(texto)
print(textoModificado)
print(texto[0:3])
print(texto[3:])
print(texto[-3:])


print('---------------------')


print(3==5)

verdadeiro = True
falso = False  

print(verdadeiro + falso)
print(verdadeiro * 2)
print(falso *2)


print('-------------------------')

lista = [1,2,4,'teste',3.5]

print(lista)

print('-------------------------')

dic = {'um':1,'dois':2,'tres':3}

print(dic)

print('-------------------------')

print(type(lista))
print(type(verdadeiro))
print(type(dic))
print(type(float))

print('-------------------------')


tres = '3'

print(type(tres))

print('-------------------------')
texto1 = 'palavra1'
texto2 = 'palavra2'

print(texto1+texto2)
print(texto1*2)


print(texto1 + 'textodomeio' + '   ' + '/' + ':' + texto2)

print('-------------------------')

lista1 = [1,2,4,'teste',3.5]
lista2 = [1,3,5,7]

lista3 = lista1 + lista2

print(lista3)

print('-------------------------')


texto = 'Mundo'

print(texto.replace('o','ão'))

print(texto.upper())

print(texto.count(texto))

print('-------------------------')
idades = [30,27,31,45,50,22,18,26,30,45]
idades.append(15)
total =sum(idades)

idades.remove(15)

print(total)
print(idades)

print(type(idades))

idades.sort()
print(idades)

idades.sort(reverse=True)
print(idades)

index =idades.index(45)
print(index)

idades30=idades.count(30)
print(idades30)

print(len(idades))

print(idades[3])


print('-------------------------------------------------------')

nomes = ['Pedro', 'Carlos','Maria','Alice','Marina','Marcos','Antonio','José','Renata']
dict_idades = {'Pedro':30,'Carlos':27,'Maria':31,'Alice':45,'Marina':50,'Marcos':22,'Antonio':18,'José':26,'Renata':30}
print(dict_idades.get('Pedro'))



dict_idades = dict(zip(nomes,idades))

print(dict_idades)

print(dict_idades.keys())
print(dict_idades.values())

dict_idades['Henrique'] = 45

print(dict_idades)

dict_idades.pop('Henrique')

print(dict_idades)


dict_idades['Pedro'] = 31

print(dict_idades)
