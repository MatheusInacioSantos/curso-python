import requests

def retorna_dados_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json/' .format(cep))
    print(response.status_code)
    print(response.text)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/' . format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text

if __name__ == '__main__':
    # retorna_dados_cep('01001000')
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon)
    # print(dados_pokemon['sprites']['front_shiny'])
    response = retorna_response('https://globallab.org/en/#.YQWt88tKjIU')
    print(response)