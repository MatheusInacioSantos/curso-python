


lista = [10, 30, 15, 7]
lista_animais = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

# Ordena uma lista de forma crescente
lista.sort()
lista_animais.sort()
print(lista)
print(lista_animais)

# Ordena uma lista de forma descrecente
lista.reverse()
print(lista)

# criando uma tupla, os valores inseridos nao podem ser mudados

tupla = (1, 3, 6, 8)
# retornar quantos elementos tem na tupla ou lista
print(len(tupla))

# Convertendo lista em tupla
tupla_animal = tuple(lista_animais)
print(tupla_animal)

# Converter tupla em lista
lista_nova = list(tupla_animal)
print(lista_nova)
# # print(lista_animais[1])
#
# soma = 0
# for x in lista:
#     print(x)
#     soma += x
# print(soma)
#
# print(max(lista_animais))
#
# if 'lobo' in lista_animais:
#     print('Exite lobo na lista')
# else:
#     print('Não existe lobo na lista')
#     lista_animais.append('lobo')
#     print(lista_animais)
# # o pop retira o ultimo inserido na lista, caso queira um especifico, coloque a posição q desejar
# lista_animais.pop()
# print(lista_animais)
#
# lista_animais.remove('elefante')
# print(lista_animais)