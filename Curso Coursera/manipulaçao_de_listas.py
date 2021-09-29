lista1 = ['vermelho','verde','azul']
print(lista1)
lista2 = lista1[:]
lista2[0] = 'rosa'
print(lista1)
print(lista2)

# não é necessário usar essa formula

#def clone(lista1)
   # clone=[]
   # for cor in lista1
     #   clone.append(cor)
   # return

# fatiamento cria uma nova lista - basta criar

#lista1[:] - devolve um clone na lista

'rosa'in lista1
print (lista1)

'rosa' in lista2
print (lista2)

if 'vermelho' in lista1:
    print ('está!!!')
else:
    print('falhou!!!')

# Então a linha clonada fica lista2 = lista1[:]

print([1,2]+[3,4])

a=[1,2,3]

b=[4,5,6]

print(a+b)

a.append('gato')
print(a)

b = a +[5]
print(b)

a_triplicado = a *3
print(a_triplicado)

b_quintuplicado = b*5
print(b_quintuplicado)

del a[1]
print(a)
lista = ['a','b','c','d','e','f']
del lista[2:5]
print(lista)