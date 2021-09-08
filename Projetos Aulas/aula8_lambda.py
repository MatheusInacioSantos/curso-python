contador_letras = lambda lista: [len(x) for x in lista]
lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(5, 10))
print(subtracao(5, 10))
# dicionario 
calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multipicacao = calculadora['multiplicacao']
print(soma(10, 5))
print(multipicacao(10, 3))