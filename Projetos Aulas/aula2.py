a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultado = ('Soma: {s}. \nSubtracao: {sub}.  \ndivisao: {d}. \nesto: {r}'
      .format(s=soma,
              sub=subtracao,
              m=multiplicacao,
              d=divisao,
              r=resto)) #forma correta de usar o print

print(resultado)

# print('Soma: ' + str(soma))
# print(multiplicacao)
# print(int(divisao))
# print(resto)