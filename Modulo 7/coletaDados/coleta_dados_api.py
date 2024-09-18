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


link = enviar_arquivo(caminho)
receber_arquivo(link)
