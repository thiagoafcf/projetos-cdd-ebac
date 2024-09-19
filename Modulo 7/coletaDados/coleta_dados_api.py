# # Definir caminho do arquivo
# caminho = r"C:\Users\Windows 10\Downloads\produtos_informatica.xlsx"
# '''
# O r antes da string é necessário para que o Python a entenda como uma raw string, ou seja,
# para interpretá-la literalmente e ignorar possíveis caracteres especiais que possam
# representar um comando ou caracter de escape, como \n.
# '''

import requests


def enviar_arquivo(file_path):
    # Requisição para enviar arquivo para o servidor e salvar a resposta da requisição
    requisicao = requests.post('https://file.io', files={'file': open(file_path, 'rb')})
    saida_requisicao = requisicao.json()
    print(saida_requisicao)

    # Verificação de sucesso de envio
    if requisicao.ok:
        print(saida_requisicao)
        url = saida_requisicao['link']  # Isola a chave 'link' e salva em uma variável
        print('Arquivo enviado com sucesso. Link para acesso:', url)
    else:
        print('Erro ao enviar o arquivo.', requisicao.json())


def receber_arquivo(file_url):
    # Requisição para solicitar o conteúdo do link informado
    requisicao = requests.get(file_url)

    # Verificação de sucesso de recebimento
    if requisicao.ok:
        with open('arquivo_baixado.xlsx', 'wb') as file:
            file.write(requisicao.content)
            print('Arquivo baixado com sucesso.')
    else:
        print('Erro ao baixar o arquivo.', requisicao.json())


def enviar_arquivo_chave(file_path):
    # Informa a chave de API para autorização
    api_key = 'XPMDT2R.FTYS2GQ-ZGHMHN2-G2SSQTB-0SXRTTB'

    # Requisição para enviar arquivo para o servidor e salvar a resposta da requisição
    requisicao = requests.post(
        'https://file.io',
        files={'file': open(file_path, 'rb')},
        headers={'Authorization': api_key}  # Inclui a chave de autorização na requisição
    )
    saida_requisicao = requisicao.json()

    # Verificação de sucesso de envio
    if requisicao.ok:
        print(saida_requisicao)
        url = saida_requisicao['link']
        print('Arquivo enviado com chave. Link para acesso:', url)
    else:
        print('Erro ao enviar o arquivo.', requisicao.json())


'''
As funções "solicitar... " foram incluídas com try/except para aumentar a modularização 
do código e melhorar o tratamento dos erros.
'''


# Função para tratar erros no envio de arquivo sem chave
def solicitar_envio():
    caminho_arquivo = input('Por favor, informe o caminho completo do arquivo: ').strip()
    try:
        enviar_arquivo(caminho_arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado. Verifique o caminho informado.')
    except Exception as e:
        print(f'Ocorreu um erro ao enviar o arquivo: {e}')


# Função para tratar erros no envio de arquivo com chave
def solicitar_envio_chave():
    caminho_arquivo = input('Por favor, informe o caminho completo do arquivo: ').strip()
    try:
        enviar_arquivo_chave(caminho_arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado. Verifique o caminho informado.')
    except Exception as e:
        print(f'Ocorreu um erro ao enviar o arquivo: {e}')


# Função para tratar erros no recebimento de arquivo
def solicitar_receber_arquivo():
    url_arquivo = input('Por favor, informe a URL do arquivo a ser baixado: ').strip()
    try:
        receber_arquivo(url_arquivo)
    except ValueError:
        print('URL inválida. Por favor, verifique a URL informada.')
    except Exception as e:
        print(f'Ocorreu um erro ao receber o arquivo: {e}')


def menu_principal():
    # Loop para manter o menu principal aberto
    while True:
        resposta_menu = int(input('\nOlá! Escolha uma das opções: \n'
                                  '1- Enviar arquivo sem chave\n'
                                  '2- Enviar arquivo com chave\n'
                                  '3- Receber arquivo\n'
                                  '4- Sair do programa\n').strip())

        # Ações com a resposta para o menu
        match resposta_menu:
            case 1:
                solicitar_envio()

            case 2:
                solicitar_envio_chave()

            case 3:
                solicitar_receber_arquivo()

            case 4:
                print('Saindo do programa...')
                break

            case _:
                print('Opção inválida. Por favor, escolha uma opção válida (1-4).')


menu_principal()
