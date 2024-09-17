import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')


# Exibir o texto
def exibir_texto_extracao(extracao_exibir):
    print(extracao_exibir.text.strip())


# Filtrar exibição pela tag
def exibir_tag(extracao_tag):
    for linha_texto in extracao_tag.find_all('h2'):
        titulo = linha_texto.text.strip()
        print('Titulo:', titulo)


# Desafio 1: Contar a quantidade de tags <h2> (títulos secundários) e <p> (parágrafos) da página
def contar_tags(extracao_contar):
    count_h2 = 0
    count_p = 0

    for linha_texto in extracao_contar.find_all(['h2', 'p']):  # Busca em toda a página as tags do argumento
        if linha_texto.name == 'h2':
            count_h2 += 1
        elif linha_texto.name == 'p':
            count_p += 1

    print('Quantidade de tags h2:', count_h2)
    print('Quantidade de tags p:', count_p)


# Desafio 2: Exibir o texto das tags h2 e p
def exibir_texto_tags(extracao_texto_tags):
    text_h2 = ''
    text_p = ''
    count_h2 = 0
    count_p = 0

    for linha_texto in extracao_texto_tags.find_all(['h2', 'p']):
        if linha_texto.name == 'h2':
            text_h2 = linha_texto.text.strip()
            count_h2 += 1
            print('\nTítulo', count_h2, ':', text_h2)
        elif linha_texto.name == 'p':
            text_p = linha_texto.text.strip()
            count_p += 1
            print('\nParágrafo', count_p, ':', text_p)


# Exibir tags aninhadas
def exibir_aninhadas(extracao_aninhada):
    for titulo in extracao_aninhada.find_all('h2'):
        print('\nTitulo:', titulo.text.strip())
        for link in titulo.find_next_siblings('p'):
            for a in link.find_all('a', href=True):
                print('Texto link:', a.text.strip(), ' | URL:', a["href"])


# exibir_texto_extracao(extracao)
# exibir_tag(extracao)
# contar_tags(extracao)
exibir_texto_tags(extracao)
# exibir_aninhadas(extracao)
