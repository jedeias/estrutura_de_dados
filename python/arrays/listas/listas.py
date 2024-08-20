#Criando uma lista

lista = ['a', 'b', 'c', 'd', 'e']

lista.append('f') # append adciona o elemnto a lista

lista2 = lista.copy() #duplicando uma lista

lista2.clear() # limpando a lista

print(lista2) # lista2 completamente limpa

lista2.append("a") # adicionando (a) a lista2

print(lista2)

lista.extend(lista2) # junta as duas listas

print(lista)

print(lista.count('a')) # mostra quantos elementos(a) tem na lista

print(lista.index('b')) # mostra a posição do elemento (b) na lista

lista.insert(3, "element") # novo elemento adicionado a posição 3 da lista

lista.pop() # remove o ultimo elemento da lista, nesse caso o elemento (a)

lista.pop(3) # remove o 3º elemento da lista no caso o "elemente"

lista.reverse() # invertendo a lista

print(lista)

lista.sort() # re ordenando a lista em ordem alfabetica

print(lista)

# também é possivel manipular a lista de forma similar a uma array convencional por meio dos index:

lista[0] = "A" # altera o index 0 para "A"
