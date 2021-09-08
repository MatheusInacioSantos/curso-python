

def escrever_arquivo(texto):
    # Pode ser criado o arquivo através do seu caminho ex:
    # diretorio = 'C:\Users\Matheus\Documents\Projetos Python\teste.txt'
    # arquivo = open(diretorio, 'w') # o 'w' sobrescreve o texto, o 'a' insere textos

    arquivo = open('teste.txt', 'w') # o 'w' sobrescreve o texto, o 'a' insere textos
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a') # o 'w' sobrescreve o texto, o 'a' insere textos
    arquivo.write(texto)
    arquivo.close()

def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r') # o 'r' é para leitura de arquivo
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum( [ int(i) for i in notas ] ) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/Users/Matheus/Documents/')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo, 'C:/Users/Matheus/Documents/Projetos Python/Nova pasta')


if __name__ == '__main__':
    lista_media = media_notas('notas.txt')
    print(lista_media)
    # copia_arquivo('notas.txt')
    move_arquivo('notas.txt')
    # escrever_arquivo('Primeira linha \n')
    # aluno = 'Marcelo, 8, 4, 9, 10\n'
    # atualizar_arquivo('notas.txt', aluno)
    # ler_arquivo('teste.txt')