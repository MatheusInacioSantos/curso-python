
lista = [1, 10]
arquivo = open('teste.txt', 'r')

try:
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]

except ZeroDivisionError:
    print('Não é possível realizar uma divisão por zero!')
except IndexError:
    print('Erro ao acessar um indice inválido da lista')
except Exception as ex:
    print('Erro desconhecido. Erro {}' .format(ex))
else:
    print('Não ocorreu excessão')

# executa mesmo se der erro
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()