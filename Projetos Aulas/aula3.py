a = int(input('Primeiro bimestre: '))
while a > 10:
    a = int(input('Nota invalida, digite a nota correta: '))
b = int(input('segundo bimestre: '))
while b > 10:
    b = int(input('Nota invalida, digite a nota correta: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
    c = int(input('Nota invalida, digite a nota correta: '))
d = int(input('Quarto bimestre: '))
while d > 10:
    d = int(input('Nota invalida, digite a nota correta: '))

media = ( a + b + c + d) / 4
print('A média do aluno é {}' .format(media))

# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}' .format(media))
# else:
#     print('Alguma nota foi digitada errada!')

# a = int(input('Entre com um valor: '))
# b = int(input('Entre com um valor: '))
# resto_a = a % 2
# resto_b = a % 2

# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um numero par')
# else:
#     print('Não foi digitado um numero par')

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('O maior número é: {}' .format(a))
# elif b > a and b > c:
#     print('O maior número é: {}' .format(b))
# else:
#     print('O maior número é c: {}' .format(c))
# print('Final do programa')