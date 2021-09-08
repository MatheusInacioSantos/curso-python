conjunto = {1, 2, 3, 4, 6}
conjunto2 = {6, 7, 8, 9, 10}
print(conjunto)

conjunto.add(5) # adicionar um novo valor
conjunto.discard(2) # remover um valor

# fazer a união dos conjuntos
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)

# criar uma intersecção, pegar o valor presente em ambos os conjuntos
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)

# mostrar os numero que aparecem apenas no primeiro conjunto
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca)
print(conjunto_diferenca2)

# diferença simetrica mostra os valores que só tem em cada conjunto
conjunto_diff_simerica = conjunto.symmetric_difference(conjunto2)
print(conjunto_diff_simerica)

# pertinencia quando um conjunto é um subconjunto do outro
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
# retorna verdadeiro pq o conjunto a esta dentro do conjunto b
print(conjunto_subset)
# retorna falso pq o conjunto b possui mais valores ou valores diferentes do conjunto a
conjunto_subset2 = conjunto_b.issubset(conjunto_a)
print(conjunto_subset2)

# o super conjunto é quando um elemento tem todos os valores do outro
# o conjunto b é um super conjunto do conjunto a, pois tem todos os valores dentro dele
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)

# para tirar a duplicidade de uma lista, basta converter ela em conjunto
lista_duplicidade = ['gato', 'gato', 'cachorro', 'cachorro', 'pato', 'elefante']
print(lista_duplicidade)
conjunto_semduplicidade = set(lista_duplicidade)
print(conjunto_semduplicidade)

# converter o conjunto em lista novamente
lista_animais = list(conjunto_semduplicidade)
print(lista_animais)