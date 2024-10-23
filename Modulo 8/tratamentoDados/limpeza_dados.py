import pandas as pd
import numpy as np

df = pd.read_csv('clientes_bruto.csv')

pd.set_option('display.width', None)  # Remove o limite de largura da coluna
print(df.head())
print(df.tail())

# Remove dados
df.drop('pais', axis=1, inplace=True)  # Remove uma coluna e já executa no DF
# df.drop(2, axis=0, inplace=True)  # Remove uma linha e já executa no DF

# Normalizar campos de texto (Idealmente se escolhe um dos tipos de tratamento)
df['nome'] = df['nome'].str.title()  # A primeira letra de cada palavra vai ser escrita de forma maiúscula
df['endereco'] = df['endereco'].str.lower()  # Todas as letras minúsculas
df['estado'] = df['estado'].str.strip().str.upper()  # Remove espaços e deixa todas as letras maiúsculas

# Converter tipos de dados
# df['idade'] = df['idade'].astype(int)  # Código passado em aula, mas que não funcionou nesse DF por conta dos NaN
df['idade'] = pd.to_numeric(df['idade'], errors='coerce').astype('Int64')
# Já nesse segundo código, ele converte o que ele consegue para inteiro, mas ainda mantém os NaN

print('Valores nulos antes:\n', df.isnull().sum())
print(df.shape)

# Substitui valores inválidos por nulos
df['cpf'] = df['cpf'].replace('cpf_invalido', np.nan)
df['endereco'] = df['endereco'].replace('endereco_invalido', np.nan)

print('Valores nulos com inválidos:\n', df.isnull().sum())
print(df.shape)

# Tratar valores nulos (ausentes)
df_fillna = df.fillna(0)  # Substituir valores nulos por 0
df_dropna = df.dropna()  # Remover registros com valores nulos
df_dropna4 = df.dropna(thresh=4)  # Manter registro com no mínimo 4 valores não nulos
df = df.dropna(subset=['cpf'])  # Remover registro com CPF nulo

print('Valores nulos depois:\n', df.isnull().sum())  # Um sum() só mostra o total de cada coluna
print(df.shape)  # Aqui mostra que a quantidade de linhas reduziu o mesmo tanto de valores de CPF nulos
print('Nulos com fillna:', df_fillna.isnull().sum().sum())  # Dois sum() mostra a somatória dos totais
print('Nulos com dropna:', df_dropna.isnull().sum().sum())
print('Nulos com dropna4:', df_dropna4.isnull().sum().sum())
print('Nulos com CPF:', df.isnull().sum().sum())

df.fillna({'estado': 'DESCONHECIDO'}, inplace=True)  # Substitui os valores nulos de estado por Desconhecido
df.fillna({'nome': 'Não Informado'}, inplace=True)
df['endereco'] = df['endereco'].fillna('endereço não informado')
# Faz o mesmo que as linhas de cima, só que de outro jeito
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean().astype(int))
# Preenche os nulos com a média (impacta menos a análise)

# Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

# Tratar dados duplicados
print('Quantidade de dados atual: ', df.shape[0])  # Especificando o 0, mostra só linhas
df.drop_duplicates()  # Remove todos os duplicados
df.drop_duplicates(subset='cpf', inplace=True)  # Remove duplicados somente da coluna
print('Quantidade removendo duplicados: ', len(df))  # Outra forma de mostrar o número de linhas

print('Dados limpos: \n', df)

# Salvar Dataframe
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']  # Podia ter feito direto também quando criou essas colunas

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('clientes_limpeza.csv', index=False)

print('Novo DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))
