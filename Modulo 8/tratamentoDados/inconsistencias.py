import pandas as pd
import numpy as np
import re

# Solução para separar a cidade da coluna endereço usando uma função completa.
# Optei por deixar ativa a solução com lambda.
# def extrair_cidade(texto):
#     try:
#         # Pega o trecho antes do estado e depois do CEP, que será a cidade
#         trecho_cidade = texto.split(' / ')[0].rsplit(' ', 0)[0]
#         cidade = re.split(r'\d{5}-?\d{3}', trecho_cidade)[-1].strip()
#         return cidade
#     except:
#         return 'desconhecido'


pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('clientes_remove_outliers.csv')

print(df.head())
print(df.tail())

# MASCARAR DADOS PESSOAIS
df['cpf_mascara'] = df['cpf'].apply(lambda cpf: f'{cpf[:3]}.***.***-{cpf[-2]}')

# CORRIGIR DATAS
df['data'] = pd.to_datetime(df['data'], format='%Y-%m-%d', errors='coerce')

data_atual = pd.to_datetime('today')
df['data_atualizada'] = df['data'].where(df['data'] < data_atual, pd.to_datetime('1900-01-01'))
# Essa data foi uma data criada. Poderíamos também deixar o campo em branco ou mesmo ajustar a data pela idade, que pode
# estar certa
df['idade_ajustada'] = data_atual.year - df['data_atualizada'].dt.year
# O código da linha seguinte serve para corrigir a idade para se a pessoa já fez aniversário naquele ano ou não.
# Ele pode retornar 0 (falso) ou 1 (verdadeiro). Ele então utiliza esse valor para subtrair ou não a idade.
df['idade_ajustada'] -= ((data_atual.month <= df['data_atualizada'].dt.month)
                         & (data_atual.day < df['data_atualizada'].dt.day)).astype(int)
df.loc[df['idade_ajustada'] > 100, 'idade_ajustada'] = np.nan
# Loc "seleciona" a linha e coluna do dado encontrado. Nesse caso, vamos localizar os valores que vão dar mais de 100
# baseado na regra que determinamos e substituir a idade ajustada por um valor nulo.

# CORRIGIR CAMPOS COM MÚLTIPLAS INFORMAÇÕES
df['endereco_curto'] = df['endereco'].apply(lambda x: x.split('\n')[0].strip())
df['bairro'] = df['endereco'].apply(lambda x: x.split('\n')[1].strip() if len(x.split('\n')) > 1 else 'desconhecido')
df['cep'] = df['endereco'].apply(
    lambda x: x.split('\n')[2].split(' ')[0].replace('-', '') if len(x.split('\n')) > 1 else 'desconhecido')
# df['cidade'] = df['endereco'].apply(extrair_cidade)
df['cidade'] = df['endereco'].apply(
    lambda x: re.split(r'\d{5}-?\d{3}', x.split(' / ')[0])[-1].strip()
    if re.search(r'\d{5}-?\d{3}', x) else 'desconhecido')
df['estado_sigla'] = df['endereco'].apply(
    lambda x: x.split(' / ')[-1].strip() if len(x.split('\n')) > 1 else 'desconhecido')

# VERIFICANDO A FORMATAÇÃO DO ENDEREÇO
df['endereco_curto'] = df['endereco_curto'].apply(lambda x: 'endereço inválido' if len(x) > 50 or len(x) < 5 else x)

# CORRIGIR DADOS ERRÔNEOS
df['cpf'] = df['cpf'].apply(lambda x: x if len(x) == 14 else 'CPF inválido')

estados_br = [
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS',
    'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC',
    'SP', 'SE', 'TO'
]
df['estado_sigla'] = df['estado_sigla'].str.upper().apply(lambda x: x if x in estados_br else 'DESCONHECIDO')

print('Dados tratados:\n', df.head())

df['cpf'] = df['cpf_mascara']
df['idade'] = df['idade_ajustada']
df['endereco'] = df['endereco_curto']
df['estado'] = df['estado_sigla']
df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'bairro', 'cep', 'cidade', 'estado']]
df_salvar.to_csv('clientes_tratados.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_tratados.csv'))
