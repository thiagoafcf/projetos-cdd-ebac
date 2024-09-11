import requests
from bs4 import BeautifulSoup

url = 'https://wiki.python.org.br/AprendaMais'
requisicao = requests.get(url)
extracao = BeautifulSoup(requisicao.text, 'html.parser')

# Exibir o texto
# print(extracao.text.strip())

# Filtrar exibição pela tag
# for linha_texto in extracao.find_all('h2'):
#     titulo = linha_texto.text.strip()
#     print('Titulo:', titulo)

# # Desafio 1: Contar a quantidade de tags <h2> (títulos secundários) e <p> (parágrafos) da página
# count_h2 = 0
# count_p = 0
#
# for linha_texto in extracao.find_all(['h2', 'p']):  # Busca em toda a página as tags do argumento
#     if linha_texto.name == 'h2':
#         count_h2 += 1
#     elif linha_texto.name == 'p':
#         count_p += 1
#
# print('Quantidades de tags h2:', count_h2)
# print('Quantidades de tags p:', count_p)

# Desafio 2: Exibir o texto das tags h2 e p
# text_h2 = ''
# text_p = ''
# count_h2 = 0
# count_p = 0
#
# for linha_texto in extracao.find_all(['h2', 'p']):
#     if linha_texto.name == 'h2':
#         text_h2 = linha_texto.text.strip()
#         count_h2 += 1
#         print('\nTítulo', count_h2, ':', text_h2)
#     elif linha_texto.name == 'p':
#         text_p = linha_texto.text.strip()
#         count_p += 1
#         print('\nParágrafo', count_p, ':', text_p)

# Exibir tags aninhadas
for titulo in extracao.find_all('h2'):
    print('\nTitulo:', titulo.text.strip())
    for link in titulo.find_next_siblings('p'):
        for a in link.find_all('a', href=True):
            print('Texto link:', a.text.strip(), ' | URL:', a["href"])