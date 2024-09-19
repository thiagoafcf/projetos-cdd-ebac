import requests

# Definir caminho do arquivo
caminho = r"C:\Users\Windows 10\Downloads\produtos_informatica.xlsx"
'''
O r antes da string é necessário para que o Python a entenda como uma raw string, ou seja,
para interpretá-la literalmente e ignorar possíveis caracteres especiais que possam 
representar um comando ou caracter de escape, como \n.
'''


def enviar_arquivo(file_path):

    # Enviar arquivo para o servidor e salvar a resposta da requisição
    requisicao = requests.post('https://file.io', files={'file': open(file_path, 'rb')})
    saida_requisicao = requisicao.json()
    print(saida_requisicao)

    # Isola a chave 'link' e salva em uma variável
    url = saida_requisicao['link']
    print('Arquivo enviado. Link para acesso:', url)
    return url


def receber_arquivo(file_url):
    requisicao = requests.get(file_url)

    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
            print('Arquivo baixado com sucesso.')
    else:
        print('Erro ao baixar o arquivo.', requisicao.json())


def enviar_arquivo_chave(file_path):
    # Informa a chave de API para autorização
    api_key = 'XPMDT2R.FTYS2GQ-ZGHMHN2-G2SSQTB-0SXRTTB'

    requisicao = requests.post(
        'https://file.io',
        files={'file': open(file_path, 'rb')},
        headers={'Authorization': api_key}  # Inclui a chave de autorização na requisição
    )
    saida_requisicao = requisicao.json()

    print(saida_requisicao)
    url = saida_requisicao['link']
    print('Arquivo enviado com chave. Link para acesso:', url)
    return url


# link = enviar_arquivo(caminho)
# receber_arquivo(link)
link_chave = enviar_arquivo_chave(caminho)
receber_arquivo(link_chave)
